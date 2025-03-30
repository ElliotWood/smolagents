# Example usage of ThinkTool

import os
import sys
import tempfile
from pathlib import Path

# Add src to path for import
sys.path.append(str(Path(__file__).parent.parent))

from smolagents.sses.tools.think_tool import ThinkTool
from smolagents.agents import CodeAgent
from smolagents.tools import Tool

# Create a simple calculator tool for testing
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

# Create temporary directory for thoughts
temp_dir = tempfile.mkdtemp()
thoughts_path = Path(temp_dir) / "thoughts"
os.makedirs(thoughts_path, exist_ok=True)

# Create tools
think_tool = ThinkTool(memory_path=thoughts_path)
calculator_tool = CalculatorTool()

# Create agent with tools
def main():
    # You would normally use a real LLM model here
    class MockModel:
        def generate(self, prompt):
            # Very simplified mock response
            return "Let me think about this problem. I'll calculate 2+2=4, so the answer is 4."
    
    # Create mock agent
    agent = CodeAgent(
        tools=[think_tool, calculator_tool],
        model=MockModel()
    )
    
    # Use the agent
    result = agent.run("Calculate 2 + 2")
    print(f"Agent result: {result}")
    
    # List recorded thoughts
    print("\nRecorded thoughts:")
    for file in os.listdir(thoughts_path):
        print(f"  - {file}")
        
    print(f"\nThoughts are stored in: {thoughts_path}")
    
    # Clean up temporary directory
    print("\nNote: In a real application, don't delete the thoughts directory.")
    print(f"Temporary directory {temp_dir} will be cleaned up automatically.")

if __name__ == "__main__":
    main()
