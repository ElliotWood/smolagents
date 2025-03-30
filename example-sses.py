# SSES Example Script

from smolagents.sses.coordinator.core_coordinator import CoreCoordinator
from smolagents.agents import CodeAgent

# You would replace this with your actual model
class MockModel:
    def generate(self, prompt):
        return "This is a mock response for testing SSES."

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
