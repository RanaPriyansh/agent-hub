# Agent Hub

[![GitHub](https://img.shields.io/badge/GitHub-000000?logo=github)](https://github.com/RanaPriyansh/agent-hub)
[![License](https://img.shields.io/github/license/RanaPriyansh/agent-hub)](https://github.com/RanaPriyansh/agent-hub/blob/main/LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/RanaPriyansh/agent-hub)](https://github.com/RanaPriyansh/agent-hub/commits/main)

Local-first registry and installer for agent tools, skills, and infrastructure packages.

## What works now

- Search a local JSON registry
- Install a package by writing a deterministic install manifest
- Use the CLI with explicit registry and install paths
- Treat the registry as a portable catalog for agent infrastructure

## Quick start

```bash
cd /root/git-repos/agent-hub
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 agent_hub.py --registry registry.example.json search monitor
python3 agent_hub.py --registry registry.example.json --install-root installed install agent-monitor
```

## Registry format

Use a JSON file like `registry.example.json`:

```json
{
  "packages": [
    {
      "name": "agent-monitor",
      "description": "Structured telemetry and event logging for agent systems",
      "tags": ["observability", "telemetry", "agents"],
      "install": {
        "type": "git",
        "source": "https://github.com/RanaPriyansh/agent-monitor.git"
      }
    }
  ]
}
```

## CLI

Search:

```bash
python3 agent_hub.py --registry registry.example.json search monitor
```

Install:

```bash
python3 agent_hub.py --registry registry.example.json --install-root installed install agent-monitor
```

After install, the manifest is written to:

```bash
installed/<package>/install.json
```

## Why this matters

The agent internet needs package discovery and installation surfaces.

This MVP is local-first on purpose:
- easy to test
- easy to version
- easy to extend later into a remote registry or marketplace

## Validation

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

## License

MIT

---

Made with 🦀 by Thielon
