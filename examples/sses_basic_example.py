# SSES Basic Example
# This script demonstrates basic usage of the SSES Core Layer

import os
import sys
import tempfile
from pathlib import Path

# Add src to path for import
sys.path.append(str(Path(__file__).parent.parent))

from smolagents.sses.coordinator.core_coordinator import CoreCoordinator
from smolagents.agents import CodeAgent
from smolagents.tools import Tool

# Create temporary directory for memory
temp_dir = tempfile.mkdtemp()
print(f"Using temporary directory: {temp_dir}")

# Simple calculator tool for testing
class CalculatorTool(Tool):
    """Simple calculator tool"""
    
    def __init__(self):
        super().__init__(
            name="calculator",
            description="Performs basic calculations",
            function=self._calculate
        )
        
    def _calculate(self, expression):
        """Evaluate a mathematical expression"""
        try:
            return str(eval(expression))
        except Exception as e:
            return f"Error: {str(e)}"

# Create coordinator
def main():
    coordinator = CoreCoordinator(memory_path=temp_dir)
    print(f"Initialized CoreCoordinator with memory path: {temp_dir}")
    
    # Create additional tool
    calculator_tool = CalculatorTool()
    
    # Mock model for testing
    # In a real application, you would use a real model like:
    # model = AnthropicModel(api_key="your_api_key") 
    # or
    # model = OpenAIModel(api_key="your_api_key")
    class MockModel:
        def generate(self, prompt):
            # Simplified mock response
            return """
            I'll solve this step by step.
            ```python
            think("To calculate compound interest, I need to use the formula A = P(1 + r/n)^(nt)")
            confidence = assess_confidence("Calculate compound interest")
            if confidence['level'] == 'high':
                principal = 1000
                rate = 0.05
                time = 5
                result = calculator(f"{principal} * (1 + {rate}) ** {time}")
                final_answer(f"The compound interest on $1000 at 5% for 5 years is ${result}")
            else:
                final_answer("I don't have enough confidence to calculate this.")
            ```
            """
    
    # Create agent
    agent = coordinator.create_agent(
        agent_class=CodeAgent,
        model=MockModel(),
        tools=[calculator_tool]
    )
    print("Created agent with core tools and calculator tool")
    
    # Example task
    task = "Calculate the compound interest on $1000 at 5% for 5 years"
    print(f"\nRunning agent on task: {task}")
    
    # Run agent
    result = agent.run(task)
    print(f"\nAgent result: {result}")
    
    # List memory paths and files
    paths = coordinator.get_memory_paths()
    print("\nMemory paths and files:")
    for name, path in paths.items():
        print(f"  - {name}: {path}")
        if os.path.exists(path):
            files = os.listdir(path)
            if files:
                print(f"    Files: {len(files)}")
                for file in files:
                    print(f"      - {file}")
    
    # Cleanup notice
    print(f"\nTemporary directory {temp_dir} will be cleaned up when the process exits.")
    print("In a real application, you would use a persistent directory for memory.")

if __name__ == "__main__":
    main()
