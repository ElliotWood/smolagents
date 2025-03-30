# Contributing to SSES

Thank you for your interest in contributing to the Smolagents Self-Evolving System (SSES) extension! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/smolagents.git`
3. Create a new branch: `git checkout -b feature/your-feature-name`
4. Install development dependencies: `pip install -e ".[dev,sses]"`

## Project Structure

The SSES extension is organized into the following directories:

```
src/smolagents/sses/
  /coordinator/  # Layer coordinators
  /memory/       # Memory storage
  /prompts/      # Prompt templates
  /tools/        # SSES tools
  /tests/        # Test suite
```

## Development Guidelines

### Code Style

We follow the standard Python style conventions (PEP 8) with some specific requirements:

- Use Black for code formatting
- Use type hints where appropriate
- Write comprehensive docstrings for all public functions and classes

### Testing

All new features should include tests:

```bash
pytest src/smolagents/sses/tests/
```

### Pull Request Process

1. Update the documentation if necessary
2. Run the test suite to ensure your changes don't break existing functionality
3. Submit a pull request with a clear description of the changes

## Implementation Layers

When adding new features, consider which layer they belong to:

- **Core Layer**: Essential tools with minimal overhead
- **Evolution Layer**: Versioning and specialization mechanisms
- **Advanced Layer**: Sophisticated discovery and optimization

Keep each layer's components independent of higher layers.

## Memory Structure

All memory-related operations should follow the established directory structure:

```
/memory
  /thoughts       # ThinkTool outputs as markdown
  /confidence     # Confidence assessments as JSON
  /evaluations    # Evaluation results as JSON
  /patterns       # Extracted patterns as JSON
  /embeddings     # Task embeddings for domain discovery
  /performance    # Agent performance history
  /benchmarks     # Benchmark results
```

## Adding New Tools

When adding a new tool:

1. Create a new file in `src/smolagents/sses/tools/`
2. Implement the tool class extending `smolagents.tools.Tool`
3. Add unit tests in `src/smolagents/sses/tests/`
4. Add an example script in `examples/`
5. Update the appropriate coordinator to include the new tool

## Questions?

If you have any questions about contributing, please open an issue in the repository.
