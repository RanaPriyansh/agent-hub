# Thielon Agent Hub

Registry and marketplace for AI agents and skills. Discover, rate, and install agent capabilities. Think "PyPI for agents".

## Features

- **Registry**: Search and discover agents/skills
- **Installation**: One-command install: `thielon-hub install resume-builder`
- **Versioning**: Semantic versioning, dependency management
- **Rating**: Community ratings, reviews, trust scores
- ** Monetization**: Paid skills marketplace (future)
- **Verification**: Verify agent identity and safety checks

## Quick Start

```bash
# Install hub CLI
pip install thielon-agent-hub

# Search for agents
thielon-hub search resume

# Install an agent/skill
thielon-hub install ai-resume-builder

# List installed
thielon-hub list
```

## Architecture

```
thielon-hub/
├── Registry API (FastAPI)
├── Package index (SQLite + S3)
├── Verification service (safety checks)
├── Rating system (community + algorithmic)
└── CLI client (thielon-hub)
```

## Why

The agent ecosystem needs a package manager. This hub provides:
- Central discovery for agent capabilities
- Trust via identity verification and ratings
- Easy installation and updates
- Monetization path for agent developers

## License

MIT
