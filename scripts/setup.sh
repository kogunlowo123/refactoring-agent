#!/bin/bash
set -euo pipefail
echo "Setting up Refactoring Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
