#!/usr/bin/env python

"""
Smolagents Self-Evolving System Setup Script
This script sets up a basic environment for using SSES.
"""

import os
import sys
import argparse
from pathlib import Path

def setup_directories(base_path="./memory"):
    """Set up memory directories"""
    base_path = Path(base_path)
    
    # Create main directories
    directories = [
        "thoughts",
        "confidence",
        "evaluations",
        "patterns",
        "embeddings",
        "performance",
        "benchmarks"
    ]
    
    for directory in directories:
        dir_path = base_path / directory
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created directory: {dir_path}")
        
    return base_path

def create_example_script(base_path):
    """Create an example script"""
    example_script = """# SSES Example Script

from smolagents.sses.coordinator.core_coordinator import CoreCoordinator
from smolagents.agents import CodeAgent

# You would replace this with your actual model
class MockModel:
    def generate(self, prompt):
        return "This is a mock response for testing SSES."

# Create coordinator with core layer tools
coordinator = CoreCoordinator(memory_path="./memory")

# Create an agent with the tools
agent = coordinator.create_agent(
    agent_class=CodeAgent,
    model=MockModel()
)

# Run a task
result = agent.run("Calculate the compound interest on $1000 at 5% for 5 years")
print(result)

# List memory paths
paths = coordinator.get_memory_paths()
print("\nMemory paths:")
for name, path in paths.items():
    print(f"  - {name}: {path}")
"""
    
    script_path = Path("./example-sses.py")
    with open(script_path, "w") as f:
        f.write(example_script)
        
    print(f"Created example script: {script_path}")
    return script_path

def main():
    parser = argparse.ArgumentParser(description="Set up SSES environment")
    parser.add_argument(
        "--memory", 
        default="./memory", 
        help="Base path for memory directories"
    )
    parser.add_argument(
        "--skip-example", 
        action="store_true", 
        help="Skip creating the example script"
    )
    
    args = parser.parse_args()
    
    print("Setting up SSES environment...")
    
    # Create directories
    base_path = setup_directories(args.memory)
    
    # Create example script
    if not args.skip_example:
        script_path = create_example_script(base_path)
    
    print("\nSetup complete! Here's how to get started:")
    print("\n1. Install smolagents with development dependencies:")
    print("   pip install -e \".[dev]\"")
    
    if not args.skip_example:
        print("\n2. Run the example script:")
        print(f"   python {script_path}")
    
    print("\n3. For more information, see README-SSES.md")

if __name__ == "__main__":
    main()
