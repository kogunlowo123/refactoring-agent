"""Test configuration for Refactoring Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "refactoring-agent", "category": "Software Engineering"}
