# Test suite for ConfidenceAssessorTool

import os
import json
import tempfile
import shutil
import unittest
from pathlib import Path

from smolagents.sses.tools.confidence_tool import ConfidenceAssessorTool

class TestConfidenceAssessorTool(unittest.TestCase):
    """Test case for ConfidenceAssessorTool"""
    
    def setUp(self):
        """Set up test environment"""
        self.test_dir = tempfile.mkdtemp()
        self.tool = ConfidenceAssessorTool(memory_path=self.test_dir)
        
    def tearDown(self):
        """Clean up test environment"""
        shutil.rmtree(self.test_dir)
        
    def test_confidence_assessment_basic(self):
        """Test basic confidence assessment"""
        task = "Calculate 2 + 2"
        result = self.tool(task)
        
        # Check basic structure
        self.assertIn("level", result)
        self.assertIn("score", result)
        self.assertIn("factors", result)
        
        # Check factors
        self.assertIn("task_clarity", result["factors"])
        self.assertIn("reference_quality", result["factors"])
        self.assertIn("domain_knowledge", result["factors"])
        
        # Check file was created
        files = os.listdir(self.test_dir)
        self.assertEqual(len(files), 1)
        
        # Check content
        with open(os.path.join(self.test_dir, files[0]), "r") as f:
            content = json.load(f)
            self.assertEqual(content["task"], task)
            
    def test_confidence_levels(self):
        """Test different confidence levels"""
        # High confidence case - specific math task
        task_high = "Calculate the compound interest on $1000 at 5% for 5 years"
        result_high = self.tool(task_high, domain="finance")
        
        # Medium confidence case - general question
        task_medium = "Explain how neural networks work"
        result_medium = self.tool(task_medium)
        
        # Low confidence case - vague question
        task_low = "Why?"
        result_low = self.tool(task_low)
        
        # Check levels
        self.assertEqual(result_high["level"], "high")
        self.assertGreaterEqual(result_high["score"], 0.85)
        
        self.assertEqual(result_medium["level"], "medium")
        self.assertGreaterEqual(result_medium["score"], 0.6)
        self.assertLess(result_medium["score"], 0.85)
        
        self.assertEqual(result_low["level"], "low")
        self.assertLess(result_low["score"], 0.6)
        
    def test_domain_specific_confidence(self):
        """Test domain-specific confidence assessments"""
        finance_task = "Calculate the return on investment for a stock portfolio"
        math_task = "Solve the quadratic equation: x^2 + 5x + 6 = 0"
        research_task = "Analyze recent papers on transformers in NLP"
        
        finance_result = self.tool(finance_task, domain="finance")
        math_result = self.tool(math_task, domain="math")
        research_result = self.tool(research_task, domain="research")
        
        # Check domain knowledge factor
        self.assertGreater(finance_result["factors"]["domain_knowledge"], 0.7)
        self.assertGreater(math_result["factors"]["domain_knowledge"], 0.7)
        self.assertGreater(research_result["factors"]["domain_knowledge"], 0.7)

if __name__ == "__main__":
    unittest.main()
