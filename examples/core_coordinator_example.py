# Example usage of CoreCoordinator

import os
import sys
import tempfile
from pathlib import Path

# Add src to path for import
sys.path.append(str(Path(__file__).parent.parent))

from smolagents.sses.coordinator.core_coordinator import CoreCoordinator
from smolagents.agents import CodeAgent
from smolagents.tools import Tool

# Example calculator tool
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

# Create temporary directory for memory
temp_dir = tempfile.mkdtemp()

# Create coordinator
def main():
    coordinator = CoreCoordinator(memory_path=temp_dir)
    
    # List available tools
    tools = coordinator.get_tools()
    print(f"Core layer tools ({len(tools)}):")  
    for tool in tools:
        print(f"  - {tool.name}: {tool.description}")
    
    # Create additional tool
    calculator_tool = CalculatorTool()
    
    # You would normally use a real LLM model here
    class MockModel:
        def generate(self, prompt):
            # Very simplified mock response that uses our tools
            return """
            Let me think about this problem first.
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
    
    # Run agent on example task
    print("\nRunning agent on example task...")
    result = agent.run("Calculate the compound interest on $1000 at 5% for 5 years")
    print(f"Agent result: {result}")
    
    # List memory paths
    paths = coordinator.get_memory_paths()
    print("\nMemory paths:")
    for name, path in paths.items():
        print(f"  - {name}: {path}")
        if os.path.exists(path):
            files = os.listdir(path)
            if files:
                print(f"    Files: {len(files)}")
                for file in files:
                    print(f"      - {file}")
    
    # Clean up temporary directory
    print("\nNote: In a real application, don't delete these directories.")
    print(f"Temporary directory {temp_dir} will be cleaned up automatically.")

if __name__ == "__main__":
    main()
