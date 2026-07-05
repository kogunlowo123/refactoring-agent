# Refactoring Agent Architecture

Intelligent code refactoring agent that identifies code smells, suggests behavior-preserving transformations, executes safe refactorings with rollback capability, and verifies correctness through automated test execution.

## Domain Tools

- **detect_code_smells**: Analyze codebase for code smells and anti-patterns
- **suggest_refactoring**: Suggest specific refactoring transformations
- **execute_refactoring**: Apply a refactoring transformation with safety checks
- **verify_behavior**: Run tests to verify refactoring preserved behavior
- **calculate_complexity**: Calculate cyclomatic and cognitive complexity metrics
- **extract_method**: Extract a code block into a named method