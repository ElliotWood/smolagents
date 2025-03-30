# SSES Example Script

from smolagents.sses.coordinator.core_coordinator import CoreCoordinator
from smolagents.agents import CodeAgent

# Define a proper mock model that implements the interface expected by Smolagents
class MockModel:
    def __call__(self, messages, *args, **kwargs):
        # The model should take messages and return a ChatMessage-like object
        return {"content": "This is a mock response for testing SSES."}

# Create coordinator with core layer tools
coordinator = CoreCoordinator(memory_path="./memory")

# Create an agent with the tools
agent = coordinator.create_agent(
    agent_class=CodeAgent,
    model=MockModel()
)

# Run a task
result = agent.run("Calculate the compound interest on $1000 at 5% for 5 years")
print(result)

# List memory paths
paths = coordinator.get_memory_paths()
print("Memory paths:")
for name, path in paths.items():
    print(f"  - {name}: {path}")
