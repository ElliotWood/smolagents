# Test suite for ThinkTool

import os
import json
import tempfile
import shutil
import unittest
from pathlib import Path

from smolagents.sses.tools.think_tool import ThinkTool

class TestThinkTool(unittest.TestCase):
    """Test case for ThinkTool"""
    
    def setUp(self):
        """Set up test environment"""
        self.test_dir = tempfile.mkdtemp()
        self.tool = ThinkTool(memory_path=self.test_dir)
        
    def tearDown(self):
        """Clean up test environment"""
        shutil.rmtree(self.test_dir)
        
    def test_think_records_thought(self):
        """Test that thoughts are recorded correctly"""
        thought = "This is a test thought for thinking"
        result = self.tool._think(thought)
        
        # Check result
        self.assertIn("Thought recorded", result)
        
        # Check file was created
        files = os.listdir(self.test_dir)
        self.assertEqual(len(files), 1)
        
        # Check content
        with open(os.path.join(self.test_dir, files[0]), "r") as f:
            content = f.read()
            self.assertIn(thought, content)
            
    def test_think_with_confidence_action(self):
        """Test that confidence assessment works"""
        # Mock confidence tool
        mock_confidence_tool = lambda x: {"level": "high", "score": 0.9}
        
        # Add to evolution tools
        self.tool.evolution_tools = {"confidence": mock_confidence_tool}
        
        thought = "This is a thought for confidence assessment"
        result = self.tool._think(thought, action="assess_confidence")
        
        # Check result
        self.assertEqual(result, {"level": "high", "score": 0.9})
        
        # Check file content
        files = os.listdir(self.test_dir)
        with open(os.path.join(self.test_dir, files[0]), "r") as f:
            content = f.read()
            self.assertIn("Confidence Assessment", content)
            self.assertIn("high", content)
            
    def test_register_evolution_tools(self):
        """Test registering evolution tools"""
        tools = {
            "confidence": lambda x: {"level": "high", "score": 0.9},
            "evaluation": lambda x: {"score": 7.5}
        }
        
        result = self.tool.register_evolution_tools(tools)
        self.assertIn("Registered 2", result)
        self.assertEqual(len(self.tool.evolution_tools), 2)
        self.assertIn("confidence", self.tool.evolution_tools)
        self.assertIn("evaluation", self.tool.evolution_tools)

if __name__ == "__main__":
    unittest.main()
