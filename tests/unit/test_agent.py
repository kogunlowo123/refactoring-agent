"""Refactoring Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_detect_code_smells():
    """Test Analyze codebase for code smells and anti-patterns."""
    tools = AgentTools()
    result = await tools.detect_code_smells(file_paths="test", language="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_suggest_refactoring():
    """Test Suggest specific refactoring transformations."""
    tools = AgentTools()
    result = await tools.suggest_refactoring(code="test", smell_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_execute_refactoring():
    """Test Apply a refactoring transformation with safety checks."""
    tools = AgentTools()
    result = await tools.execute_refactoring(refactoring_type="test", target="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_verify_behavior():
    """Test Run tests to verify refactoring preserved behavior."""
    tools = AgentTools()
    result = await tools.verify_behavior(test_suite="test", affected_files="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.refactoring_agent_agent import RefactoringAgentAgent
    agent = RefactoringAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
