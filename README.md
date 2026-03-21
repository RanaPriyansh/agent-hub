# Agent Hub

[![GitHub](https://img.shields.io/badge/GitHub-000000?logo=github)](https://github.com/RanaPriyansh/agent-hub)
[![License](https://img.shields.io/github/license/RanaPriyansh/agent-hub)](https://github.com/RanaPriyansh/agent-hub/blob/main/LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/RanaPriyansh/agent-hub)](https://github.com/RanaPriyansh/agent-hub/commits/main)

Registry and marketplace for AI agents and skills. Discover, rate, and install agent capabilities. Think "PyPI for agents".

## Features

- **Registry**: Search and discover agents/skills
- **Installation**: One-command install: `agent-hub install resume-builder`
- **Versioning**: Semantic versioning, dependency management
- **Rating**: Community ratings, reviews, trust scores
- ** Monetization**: Paid skills marketplace (future)
- **Verification**: Verify agent identity and safety checks

## Quick Start

```bash
# Install hub CLI
pip install agent-hub

# Search for agents
agent-hub search resume

# Install an agent/skill
agent-hub install ai-resume-builder

# List installed
agent-hub list
```

## Architecture

```
agent-hub/
├── Registry API (FastAPI)
├── Package index (SQLite + S3)
├── Verification service (safety checks)
├── Rating system (community + algorithmic)
└── CLI client (agent-hub)
```

## Why

The agent ecosystem needs a package manager. This hub provides:
- Central discovery for agent capabilities
- Trust via identity verification and ratings
- Easy installation and updates
- Monetization path for agent developers

## License

MIT

---

Made with 🦀 by Thielon
