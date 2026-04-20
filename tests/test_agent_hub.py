import json
import tempfile
import unittest
from pathlib import Path
from click.testing import CliRunner

import agent_hub


class AgentHubTests(unittest.TestCase):
    def test_search_registry_returns_matching_packages(self):
        with tempfile.TemporaryDirectory() as tmp:
            registry_path = Path(tmp) / "registry.json"
            registry_path.write_text(json.dumps({
                "packages": [
                    {"name": "agent-monitor", "description": "Telemetry for agents", "install": {"type": "git", "source": "https://example.com/agent-monitor.git"}},
                    {"name": "agent-hub", "description": "Registry for agents", "install": {"type": "git", "source": "https://example.com/agent-hub.git"}}
                ]
            }))
            results = agent_hub.search_registry("monitor", registry_path)
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]["name"], "agent-monitor")

    def test_install_package_records_install_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            registry_path = Path(tmp) / "registry.json"
            registry_path.write_text(json.dumps({
                "packages": [
                    {"name": "agent-monitor", "description": "Telemetry for agents", "install": {"type": "git", "source": "https://example.com/agent-monitor.git"}}
                ]
            }))
            install_root = Path(tmp) / "installed"
            result = agent_hub.install_package("agent-monitor", registry_path, install_root)
            manifest_path = install_root / "agent-monitor" / "install.json"
            self.assertEqual(result["name"], "agent-monitor")
            self.assertTrue(manifest_path.exists())
            manifest = json.loads(manifest_path.read_text())
            self.assertEqual(manifest["source"], "https://example.com/agent-monitor.git")

    def test_cli_search_and_install_work_with_explicit_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            registry_path = Path(tmp) / "registry.json"
            install_root = Path(tmp) / "installed"
            registry_path.write_text(json.dumps({
                "packages": [
                    {"name": "agent-monitor", "description": "Telemetry for agents", "install": {"type": "git", "source": "https://example.com/agent-monitor.git"}}
                ]
            }))
            runner = CliRunner()
            search_result = runner.invoke(agent_hub.cli, ["--registry", str(registry_path), "search", "monitor"])
            self.assertEqual(search_result.exit_code, 0)
            self.assertIn("agent-monitor", search_result.output)
            install_result = runner.invoke(agent_hub.cli, ["--registry", str(registry_path), "--install-root", str(install_root), "install", "agent-monitor"])
            self.assertEqual(install_result.exit_code, 0)
            self.assertIn("Installed agent-monitor", install_result.output)
            self.assertTrue((install_root / "agent-monitor" / "install.json").exists())


if __name__ == "__main__":
    unittest.main()
