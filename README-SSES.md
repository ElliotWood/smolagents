# Smolagents Self-Evolving System (SSES)

## Overview

The Smolagents Self-Evolving System (SSES) extends the existing Smolagents framework using a tool composition approach to enable agent evolution through prompt specialization, confidence assessment, and index-based evaluation. By implementing functionality as tools rather than through inheritance, SSES provides modular capabilities while preserving compatibility with the core framework.

## Core Philosophy

1. **Extend, Don't Replace**: Build on existing Smolagents patterns
2. **Composition Over Inheritance**: Implement features as tools rather than through complex inheritance
3. **Layered Adoption**: Enable incremental complexity adoption
4. **Version Control Integration**: Leverage git for tracking evolution
5. **Progressive Enhancement**: Start with minimal viable tools and enhance iteratively

## Implementation Layers

The system is designed with three implementation layers of increasing complexity:

### Core Layer (Current Implementation)

Essential tools with minimal overhead:
- **ThinkTool**: Integration point for explicit reasoning and evolution
- **ConfidenceAssessorTool**: Evaluates agent confidence for tasks

This layer allows agents to think explicitly about their problem-solving process and assess their confidence in handling specific tasks.

### Evolution Layer (Coming Soon)

Versioning and specialization mechanisms:
- **PromptVersioningTool**: Manages prompt versioning with git
- **EvaluationTool**: Comprehensive evaluation framework
- **KnowledgeRepositoryTool**: Extracts and validates patterns

### Advanced Layer (Coming Soon)

Sophisticated discovery and optimization:
- **SpecializationTool**: Creates domain-specific agents
- **DomainDiscoveryTool**: Identifies domains through clustering
- **TaskRouterTool**: Routes tasks to specialized agents

## Getting Started

### Installation

To install the SSES extension, clone the repository and install in development mode:

```bash
git clone https://github.com/ElliotWood/smolagents.git
cd smolagents
pip install -e ".[dev]"
```

### Basic Usage

Here's a simple example using the Core Layer:

```python
from smolagents.sses.coordinator.core_coordinator import CoreCoordinator
from smolagents.agents import CodeAgent
import anthropic  # or any supported model

# Set up a model (using Anthropic as example)
model = anthropic.Anthropic(api_key="your_api_key")

# Create coordinator with core layer tools
coordinator = CoreCoordinator(memory_path="./memory")

# Create an agent with the tools
agent = coordinator.create_agent(
    agent_class=CodeAgent,
    model=model
)

# Run a task
result = agent.run("Calculate the compound interest on $1000 at 5% for 5 years")
print(result)
```

### Directory Structure

All memory is stored in a versioned structure:

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

## Current Status

The SSES project is under active development. Currently, the Core Layer is implemented and functional. The Evolution and Advanced Layers are planned for future releases.

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
