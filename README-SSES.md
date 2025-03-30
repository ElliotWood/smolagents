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

## RACI Matrix

This RACI (Responsible, Accountable, Consulted, Informed) matrix defines roles and responsibilities for the SSES project:

| Activity/Deliverable | AI Assistant | Human (Elliot) |
|----------------------|--------------|----------------|
| **Project Management** |  |  |
| Task Prioritization | R/A | C/I |
| Risk Management | R/A | C/I |
| Decision Escalation | R | A |
| Progress Reporting | R/A | I |
| **Development** |  |  |
| Code Implementation | R/A | I |
| Technical Design | R/A | C |
| Architecture Decisions | R | A |
| Documentation | R/A | I |
| **Quality Assurance** |  |  |
| Test Planning | R/A | I |
| Test Execution | R/A | I |
| Independent Evaluation | R/A | I |
| Bug Fixing | R/A | C |
| **Release Management** |  |  |
| Version Control | R/A | I |
| Release Preparation | R | A |
| Deployment | R | A |
| Release Notes | R/A | C |
| **Phase 0: Repository Setup** |  |  |
| Repository Structure | R/A | I |
| GitHub Actions Configuration | R/A | I |
| Memory Versioning System | R/A | C |
| Benchmark Implementation | R/A | C |
| **Phase 1: Core Layer** |  |  |
| ThinkTool Implementation | R/A | I |
| ConfidenceAssessorTool Implementation | R/A | I |
| Core Layer Integration | R/A | I |
| Core Layer Testing | R/A | I |
| **Phase 2: Evolution Layer** |  |  |
| PromptVersioningTool Implementation | R/A | I |
| EvaluationTool Implementation | R/A | I |
| KnowledgeRepositoryTool Implementation | R/A | I |
| Evolution Layer Integration | R/A | I |
| Evolution Layer Testing | R/A | I |
| **Phase 3: Advanced Layer** |  |  |
| SpecializationTool Implementation | R/A | I |
| DomainDiscoveryTool Implementation | R/A | I |
| TaskRouterTool Implementation | R/A | I |
| Advanced Layer Integration | R/A | I |
| Advanced Layer Testing | R/A | I |
| **Phase 4: Integration and Release** |  |  |
| Full Integration | R/A | C |
| Final Benchmarking | R/A | I |
| Complete Documentation | R/A | C |
| Final Release | R | A |

### RACI Definition
- **R (Responsible)**: Who performs the work
- **A (Accountable)**: Who ultimately answers for the activity
- **C (Consulted)**: Who provides input before and during the activity
- **I (Informed)**: Who is kept up-to-date on progress

## Decision Escalation Criteria

The AI Assistant will escalate to the Human (Elliot) in the following situations:

1. **Critical Design Decisions**: Fundamental architectural choices that significantly impact the system design
2. **Technical Roadblocks**: Challenges that cannot be resolved within the AI's capabilities
3. **Quality Issues**: Significant quality concerns that might compromise system integrity
4. **Scope Changes**: Any proposed changes to the project scope or objectives
5. **External Dependencies**: Issues involving integration with external systems
6. **Risk Elevation**: When a previously identified risk changes in severity or probability
7. **Release Approval**: Final approval for releases

## Implementation Plan

The implementation follows a phased approach:

1. **Phase 0**: Repository Setup (Complete)
2. **Phase 1**: Core Layer Implementation (Complete)
3. **Phase 2**: Evolution Layer Implementation (In Progress)
4. **Phase 3**: Advanced Layer Implementation (Planned)
5. **Phase 4**: Integration and Release (Planned)

Each phase includes:
- Implementation of components
- Testing and validation
- Documentation
- Independent evaluation

## Quality Metrics

The project aims to meet the following quality metrics:

- Test coverage > 90% for all components
- Documentation for all public APIs
- Performance benchmarks for each layer
- Successful execution of all test suites
- Completion of independent evaluations

## Current Status

The SSES project is under active development. Currently, the Core Layer is implemented and functional. The Evolution and Advanced Layers are planned for future releases.

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.