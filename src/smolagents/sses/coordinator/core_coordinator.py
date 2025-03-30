# CoreCoordinator Implementation
# This file implements the CoreCoordinator class for coordinating core layer tools

import os
from pathlib import Path


class CoreCoordinator:
    """Coordinates core layer tools"""

    def __init__(self, memory_path="./memory"):
        self.memory_path = Path(memory_path)
        self.tools = self._initialize_tools()

    def _initialize_tools(self):
        """Initialize core layer tools"""
        from smolagents.sses.tools.confidence_tool import ConfidenceAssessorTool
        from smolagents.sses.tools.think_tool import ThinkTool

        thoughts_path = self.memory_path / "thoughts"
        confidence_path = self.memory_path / "confidence"

        os.makedirs(thoughts_path, exist_ok=True)
        os.makedirs(confidence_path, exist_ok=True)

        # Create tools
        think_tool = ThinkTool(memory_path=thoughts_path)
        confidence_tool = ConfidenceAssessorTool(memory_path=confidence_path)

        # Register confidence tool with think tool
        think_tool.register_evolution_tools({"confidence": confidence_tool})

        return {"think": think_tool, "confidence": confidence_tool}

    def get_tools(self):
        """Get list of tools for agent"""
        return list(self.tools.values())

    def create_agent(self, agent_class, model, tools=None):
        """Create agent with core layer tools"""
        agent_tools = tools or []
        agent_tools.extend(self.get_tools())

        return agent_class(tools=agent_tools, model=model)

    def get_memory_paths(self):
        """Get paths to memory directories"""
        return {"thoughts": self.memory_path / "thoughts", "confidence": self.memory_path / "confidence"}


# Example usage
if __name__ == "__main__":
    # Create coordinator
    coordinator = CoreCoordinator("./test_memory")

    # Get tools
    tools = coordinator.get_tools()
    print(f"Initialized {len(tools)} tools:")
    for tool in tools:
        print(f"  - {tool.name}")
