from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import click


def _default_registry_path() -> Path:
    return Path("registry.json")


def _default_install_root() -> Path:
    return Path("installed")


def load_registry(registry_path: str | Path) -> dict:
    path = Path(registry_path)
    if not path.exists():
        return {"packages": []}
    return json.loads(path.read_text(encoding="utf-8"))


def search_registry(query: str, registry_path: str | Path) -> list[dict]:
    payload = load_registry(registry_path)
    q = query.lower().strip()
    results = []
    for package in payload.get("packages", []):
        haystack = " ".join([
            str(package.get("name", "")),
            str(package.get("description", "")),
            " ".join(package.get("tags", []) or []),
        ]).lower()
        if q in haystack:
            results.append(package)
    return results


def install_package(package_name: str, registry_path: str | Path, install_root: str | Path) -> dict:
    payload = load_registry(registry_path)
    package = next((pkg for pkg in payload.get("packages", []) if pkg.get("name") == package_name), None)
    if package is None:
        raise ValueError(f"Package not found: {package_name}")

    destination = Path(install_root) / package_name
    destination.mkdir(parents=True, exist_ok=True)
    manifest = {
        "name": package_name,
        "installed_at": datetime.now(timezone.utc).isoformat(),
        "source": package.get("install", {}).get("source", "unknown"),
        "install": package.get("install", {}),
        "package": package,
    }
    (destination / "install.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest


@click.group()
@click.option("--registry", "registry_path", default=str(_default_registry_path()), show_default=True, type=click.Path(path_type=Path))
@click.option("--install-root", default=str(_default_install_root()), show_default=True, type=click.Path(path_type=Path))
@click.pass_context
def cli(ctx: click.Context, registry_path: Path, install_root: Path):
    """Registry for AI agents and skills."""
    ctx.ensure_object(dict)
    ctx.obj["registry_path"] = registry_path
    ctx.obj["install_root"] = install_root


@cli.command()
@click.argument("query")
@click.pass_context
def search(ctx: click.Context, query: str):
    results = search_registry(query, ctx.obj["registry_path"])
    if not results:
        click.echo(f"No packages found for: {query}")
        return
    for package in results:
        click.echo(f"{package['name']}: {package.get('description', '').strip()}")


@cli.command()
@click.argument("package")
@click.pass_context
def install(ctx: click.Context, package: str):
    manifest = install_package(package, ctx.obj["registry_path"], ctx.obj["install_root"])
    click.echo(f"Installed {manifest['name']} -> {ctx.obj['install_root'] / manifest['name']}")


if __name__ == "__main__":
    cli()
