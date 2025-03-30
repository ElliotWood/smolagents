# Test suite for CoreCoordinator

import os
import tempfile
import shutil
import unittest
from pathlib import Path

from smolagents.sses.coordinator.core_coordinator import CoreCoordinator

class TestCoreCoordinator(unittest.TestCase):
    """Test case for CoreCoordinator"""
    
    def setUp(self):
        """Set up test environment"""
        self.test_dir = tempfile.mkdtemp()
        self.coordinator = CoreCoordinator(memory_path=self.test_dir)
        
    def tearDown(self):
        """Clean up test environment"""
        shutil.rmtree(self.test_dir)
        
    def test_initialize_tools(self):
        """Test that tools are initialized correctly"""
        tools = self.coordinator.tools
        
        # Check tool types
        self.assertIn("think", tools)
        self.assertIn("confidence", tools)
        
        # Check tool names
        self.assertEqual(tools["think"].name, "think")
        self.assertEqual(tools["confidence"].name, "assess_confidence")
        
    def test_get_tools(self):
        """Test that get_tools returns the correct tools"""
        tools = self.coordinator.get_tools()
        
        # Check list
        self.assertEqual(len(tools), 2)
        self.assertEqual(tools[0].name, "think")  # Assuming order is preserved
        self.assertEqual(tools[1].name, "assess_confidence")
        
    def test_memory_directory_creation(self):
        """Test that memory directories are created"""
        paths = self.coordinator.get_memory_paths()
        
        # Check paths
        self.assertIn("thoughts", paths)
        self.assertIn("confidence", paths)
        
        # Check directories exist
        self.assertTrue(os.path.exists(paths["thoughts"]))
        self.assertTrue(os.path.exists(paths["confidence"]))
        
    def test_create_agent(self):
        """Test agent creation with tools"""
        # Mock agent class
        class MockAgent:
            def __init__(self, tools, model):
                self.tools = tools
                self.model = model
                
        # Mock model
        mock_model = "mock_model"
        
        # Create agent
        agent = self.coordinator.create_agent(MockAgent, mock_model)
        
        # Check agent setup
        self.assertEqual(agent.model, mock_model)
        self.assertEqual(len(agent.tools), 2)  # Should have think and confidence tools
        
    def test_create_agent_with_additional_tools(self):
        """Test agent creation with additional tools"""
        # Mock agent class
        class MockAgent:
            def __init__(self, tools, model):
                self.tools = tools
                self.model = model
                
        # Mock model and tool
        mock_model = "mock_model"
        mock_tool = type('MockTool', (), {'name': 'mock_tool'})()
        
        # Create agent with additional tool
        agent = self.coordinator.create_agent(
            MockAgent, 
            mock_model, 
            tools=[mock_tool]
        )
        
        # Check agent setup
        self.assertEqual(len(agent.tools), 3)  # Should have think, confidence, and mock tools
        tool_names = [tool.name for tool in agent.tools]
        self.assertIn("think", tool_names)
        self.assertIn("assess_confidence", tool_names)
        self.assertIn("mock_tool", tool_names)

if __name__ == "__main__":
    unittest.main()
