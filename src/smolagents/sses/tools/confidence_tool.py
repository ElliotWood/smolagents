# ConfidenceAssessorTool Implementation
# This file implements the ConfidenceAssessorTool class for assessing agent confidence

import datetime
import json
import os
import re
from pathlib import Path

from smolagents.tools import Tool


class ConfidenceAssessorTool(Tool):
    """Tool for assessing agent confidence"""

    def __init__(self, memory_path="./memory/confidence"):
        self.name = "assess_confidence"
        self.description = "Assess your confidence in handling this task"
        self.inputs = {
            "task_description": {
                "type": "string",
                "description": "The task to assess confidence for"
            },
            "domain": {
                "type": "string",
                "description": "Optional domain for the task",
                "nullable": True
            }
        }
        self.output_type = "object"
        self.memory_path = Path(memory_path)
        os.makedirs(self.memory_path, exist_ok=True)
        self.is_initialized = True

    def forward(self, task_description, domain=None):
        """Assess confidence for a given task"""
        factors = self._analyze_factors(task_description, domain)
        confidence_score = self._calculate_confidence(factors)

        # Create assessment object
        assessment = {
            "task": task_description,
            "domain": domain,
            "factors": factors,
            "score": confidence_score,
            "level": "high" if confidence_score > 0.85 else "medium" if confidence_score > 0.6 else "low",
        }

        # Save assessment
        self._save_assessment(assessment)

        return assessment

    def _analyze_factors(self, task_description, domain=None):
        """Analyze confidence factors for a task"""
        factors = {}

        # Task clarity
        word_count = len(task_description.split())
        question_marks = task_description.count("?")
        specific_terms = sum(
            1 for term in ["calculate", "find", "analyze", "compare", "explain"] if term in task_description.lower()
        )

        factors["task_clarity"] = min(
            1.0, 0.5 + 0.1 * specific_terms + (0.4 if word_count > 10 else 0.2) - (0.1 if question_marks > 2 else 0)
        )

        # Reference quality
        url_count = len(re.findall(r"https?://\S+", task_description))
        reference_terms = sum(
            1 for term in ["reference", "according to", "as stated in", "cited"] if term in task_description.lower()
        )

        factors["reference_quality"] = min(1.0, 0.5 + 0.2 * url_count + 0.1 * reference_terms)

        # Domain knowledge
        factors["domain_knowledge"] = 0.7  # Default baseline

        if domain:
            domain_specific_terms = {
                "finance": ["interest", "investment", "stock", "rate", "market", "capital"],
                "math": ["equation", "calculate", "formula", "solve", "computation"],
                "research": ["study", "paper", "review", "literature", "analysis"],
                "creative": ["story", "design", "write", "create", "generate"],
            }

            if domain in domain_specific_terms:
                term_count = sum(1 for term in domain_specific_terms[domain] if term in task_description.lower())
                factors["domain_knowledge"] = min(1.0, 0.7 + 0.05 * term_count)

        return factors

    def _calculate_confidence(self, factors):
        """Calculate overall confidence score from factors"""
        weights = {"task_clarity": 1.0, "reference_quality": 0.8, "domain_knowledge": 1.2}

        weighted_sum = sum(factors[k] * weights[k] for k in factors)
        weight_sum = sum(weights.values())

        return weighted_sum / weight_sum

    def _save_assessment(self, assessment):
        """Save confidence assessment to file"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_id = "".join(filter(lambda x: x not in (" ", ":", "-"), timestamp))[-8:]
        filename = f"{timestamp}_{unique_id}.json"
        filepath = self.memory_path / filename

        with open(filepath, "w") as f:
            json.dump(assessment, f, indent=2)

        return filepath


# Example usage
if __name__ == "__main__":
    # Create tool
    tool = ConfidenceAssessorTool("./test_memory/confidence")

    # Test basic functionality
    result = tool.forward("Calculate the compound interest on $2000 at 3% for 5 years", domain="finance")
    print(json.dumps(result, indent=2))

    # Test with different task
    result = tool.forward("What is the meaning of life?")
    print(json.dumps(result, indent=2))
