# Example usage of ConfidenceAssessorTool

import os
import sys
import json
import tempfile
from pathlib import Path

# Add src to path for import
sys.path.append(str(Path(__file__).parent.parent))

from smolagents.sses.tools.confidence_tool import ConfidenceAssessorTool
from smolagents.sses.tools.think_tool import ThinkTool
from smolagents.agents import CodeAgent

# Create temporary directory for thoughts
temp_dir = tempfile.mkdtemp()
confidence_path = Path(temp_dir) / "confidence"
thoughts_path = Path(temp_dir) / "thoughts"
os.makedirs(confidence_path, exist_ok=True)
os.makedirs(thoughts_path, exist_ok=True)

# Create tools
confidence_tool = ConfidenceAssessorTool(memory_path=confidence_path)
think_tool = ThinkTool(memory_path=thoughts_path)

# Register confidence tool with think tool
think_tool.register_evolution_tools({"confidence": confidence_tool})

# Create agent with tools
def main():
    # You would normally use a real LLM model here
    class MockModel:
        def generate(self, prompt):
            # Very simplified mock response
            return "I need to assess my confidence in solving this task."
    
    # Create mock agent
    agent = CodeAgent(
        tools=[think_tool, confidence_tool],
        model=MockModel()
    )
    
    # Example tasks with different confidence levels
    tasks = [
        "Calculate the compound interest on $1000 at 5% for 5 years",
        "Explain how neural networks work",
        "Why is the sky blue?"
    ]
    
    # Assess confidence for each task
    for task in tasks:
        print(f"\nTask: {task}")
        
        # Direct assessment
        confidence = confidence_tool(task)
        print(f"Direct confidence assessment: {confidence['level']} ({confidence['score']:.2f})")
        
        # Assessment through think tool
        thought = f"I need to solve: {task}. Let me assess my confidence."
        confidence_through_think = think_tool._think(thought, action="assess_confidence")
        print(f"Think tool confidence: {confidence_through_think['level']} ({confidence_through_think['score']:.2f})")
        
    # List recorded assessments
    print("\nRecorded confidence assessments:")
    for file in os.listdir(confidence_path):
        filepath = confidence_path / file
        with open(filepath, "r") as f:
            data = json.load(f)
            print(f"  - {file}: {data['level']} ({data['score']:.2f})")
        
    print(f"\nConfidence assessments are stored in: {confidence_path}")
    print(f"Thoughts are stored in: {thoughts_path}")
    
    # Clean up temporary directory
    print("\nNote: In a real application, don't delete these directories.")
    print(f"Temporary directory {temp_dir} will be cleaned up automatically.")

if __name__ == "__main__":
    main()
