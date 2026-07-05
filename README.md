# Refactoring Agent

[![CI](https://github.com/kogunlowo123/refactoring-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/refactoring-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Software Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Intelligent code refactoring agent that identifies code smells, suggests behavior-preserving transformations, executes safe refactorings with rollback capability, and verifies correctness through automated test execution.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `detect_code_smells` | Analyze codebase for code smells and anti-patterns |
| `suggest_refactoring` | Suggest specific refactoring transformations |
| `execute_refactoring` | Apply a refactoring transformation with safety checks |
| `verify_behavior` | Run tests to verify refactoring preserved behavior |
| `calculate_complexity` | Calculate cyclomatic and cognitive complexity metrics |
| `extract_method` | Extract a code block into a named method |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/analyze` | Analyze code for smells and metrics |
| `POST` | `/api/v1/suggest` | Suggest refactoring transformations |
| `POST` | `/api/v1/execute` | Execute a refactoring with verification |
| `POST` | `/api/v1/verify` | Verify behavior preservation |
| `POST` | `/api/v1/complexity` | Calculate complexity metrics |
| `GET` | `/api/v1/history` | View refactoring history with rollback |

## Features

- Smell Detection
- Safe Refactoring
- Behavior Preservation
- Test Verification
- Rollback Support

## Integrations

- Github Connector
- Test Runner
- Ast Parser
- Complexity Analyzer

## Architecture

```
refactoring-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── refactoring_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 6 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 6 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 4 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**LLM + AST Analysis + Test Runner**

---

Built as part of the Enterprise AI Agent Platform.
