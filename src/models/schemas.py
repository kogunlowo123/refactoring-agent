"""Refactoring Agent - Domain-Specific Schemas."""

from datetime import datetime
from uuid import UUID, uuid4
from typing import Any, Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Chat request."""
    message: str
    conversation_id: UUID | None = None
    stream: bool = False
    context: dict[str, Any] | None = None


class ChatResponse(BaseModel):
    """Chat response."""
    message: str
    conversation_id: UUID
    message_id: UUID
    sources: list[dict[str, Any]] = []
    tool_results: list[dict[str, Any]] = []
    model: str
    latency_ms: float
    timestamp: datetime


class StreamChunk(BaseModel):
    """Streaming response chunk."""
    chunk: str
    conversation_id: UUID
    done: bool = False


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    uptime_seconds: float
    agent: str
    features: list[str]


class SmellDetectionRequest(BaseModel):
    """SmellDetectionRequest for Refactoring Agent."""
    file_paths: list[str]
    language: str
    max_complexity: int = 15


class CodeSmell(BaseModel):
    """CodeSmell for Refactoring Agent."""
    file_path: str
    line: int
    smell_type: str
    severity: str
    description: str
    suggested_refactoring: str


class RefactoringResult(BaseModel):
    """RefactoringResult for Refactoring Agent."""
    transformation: str
    files_changed: list[str]
    tests_passed: bool
    rollback_available: bool

