# ThinkTool Implementation
# This file implements the ThinkTool class for explicit reasoning

import datetime
import json
import os
from pathlib import Path

from smolagents.tools import Tool


class ThinkTool(Tool):
    """Tool for agent to think and reason explicitly"""

    def __init__(self, memory_path="./memory/thoughts"):
        self.name = "think"
        self.description = "Use this tool to think through problems step by step"
        self.inputs = {
            "thought": {
                "type": "string",
                "description": "The thought process to record"
            },
            "action": {
                "type": "string",
                "description": "Action to perform (reflect, assess_confidence, evaluate, extract_patterns)"
            }
        }
        self.output_type = "string"
        self.memory_path = Path(memory_path)
        self.evolution_tools = {}
        os.makedirs(self.memory_path, exist_ok=True)
        self.is_initialized = True

    def forward(self, thought, action="reflect"):
        """Record thought process and handle actions"""
        # Create unique filename
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_id = "".join(filter(lambda x: x not in (" ", ":", "-"), timestamp))[-8:]
        filename = f"{timestamp}_{unique_id}.md"
        filepath = self.memory_path / filename

        # Write thought to file
        with open(filepath, "w") as f:
            f.write(f"# Thought Process\n\n{thought}\n")

        # Handle specific actions based on available tools
        result = f"Thought recorded: {thought[:50]}..."

        if action != "reflect" and hasattr(self, "evolution_tools") and self.evolution_tools:
            if action == "assess_confidence" and "confidence" in self.evolution_tools:
                confidence = self.evolution_tools["confidence"](thought)
                with open(filepath, "a") as f:
                    f.write(f"\n## Confidence Assessment\n\n{json.dumps(confidence, indent=2)}\n")
                return confidence

            if action == "evaluate" and "evaluation" in self.evolution_tools:
                evaluation = self.evolution_tools["evaluation"](thought)
                with open(filepath, "a") as f:
                    f.write(f"\n## Evaluation\n\n{json.dumps(evaluation, indent=2)}\n")
                return evaluation

            if action == "extract_patterns" and "knowledge" in self.evolution_tools:
                patterns = self.evolution_tools["knowledge"].extract_patterns(thought)
                with open(filepath, "a") as f:
                    f.write(f"\n## Extracted Patterns\n\n{json.dumps(patterns, indent=2)}\n")
                return patterns

        return result

    def register_evolution_tools(self, tools_dict):
        """Register evolution tools for integration"""
        self.evolution_tools = tools_dict
        return f"Registered {len(tools_dict)} evolution tools"


# Example usage
if __name__ == "__main__":
    # Create tool
    tool = ThinkTool("./test_memory/thoughts")

    # Test basic functionality
    result = tool._think("I need to solve this step by step. First, I'll...")
    print(result)
