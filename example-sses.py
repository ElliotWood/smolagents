# SSES Example Script

from smolagents.sses.coordinator.core_coordinator import CoreCoordinator
from smolagents.agents import CodeAgent
from smolagents.models import ChatMessage, MessageRole

# Proper mock model that implements the expected interface
class MockModel:
    def __init__(self):
        self.model_id = "MockModel"
        self.last_input_token_count = 0
        self.last_output_token_count = 0
    
    def __call__(self, messages, stop_sequences=None, **kwargs):
        self.last_input_token_count = 10  # Mock token count
        self.last_output_token_count = 20  # Mock token count
        
        print("Model called with messages:", messages)
        if stop_sequences:
            print("Stop sequences:", stop_sequences)
            
        # Return a proper ChatMessage object
        return ChatMessage(
            role=MessageRole.ASSISTANT,
            content="```python\n# Code to calculate compound interest\nprincipal = 1000\nrate = 0.05\ntime = 5\n\n# Calculate compound interest\namount = principal * (1 + rate) ** time\ninterest = amount - principal\n\nprint(f\"Compound interest on ${principal} at {rate*100}% for {time} years is ${interest:.2f}\")\nprint(f\"Total amount: ${amount:.2f}\")\n\nfinal_answer(amount)\n```<end_code>",
        )
    
    def to_dict(self):
        """Return a dictionary representation of the model."""
        return {
            "class": "MockModel",
            "data": {
                "model_id": self.model_id,
                "last_input_token_count": self.last_input_token_count,
                "last_output_token_count": self.last_output_token_count,
            }
        }

# Create coordinator with core layer tools
coordinator = CoreCoordinator(memory_path="./memory")

# Create an agent with the tools
agent = coordinator.create_agent(
    agent_class=CodeAgent,
    model=MockModel()
)

# Run a task
try:
    result = agent.run("Calculate the compound interest on $1000 at 5% for 5 years")
    print("Result:", result)
except Exception as e:
    print(f"Error running agent: {e}")
    import traceback
    traceback.print_exc()

# List memory paths
paths = coordinator.get_memory_paths()
print("Memory paths:")
for name, path in paths.items():
    print(f"  - {name}: {path}")
