# Memory processor for GitHub Actions
# This script processes memory directory changes and generates changelogs

import os
import json
import yaml
import datetime
import glob
from pathlib import Path

class MemoryProcessor:
    """Processes memory changes and generates changelogs"""
    
    def __init__(self, memory_path="./src/smolagents/sses/memory"):
        self.memory_path = Path(memory_path)
        self.changelog_path = self.memory_path / "changelog.md"
        
    def process_changes(self):
        """Process memory directory changes"""
        # Check if changelog exists
        if not self.changelog_path.exists():
            with open(self.changelog_path, "w") as f:
                f.write("# SSES Memory Changelog\n\n")
                f.write("This file tracks changes to the memory directories.\n\n")
        
        # Get latest changes
        changes = self._collect_changes()
        
        # Update changelog
        self._update_changelog(changes)
        
        return changes
    
    def _collect_changes(self):
        """Collect changes from memory directories"""
        changes = {}
        now = datetime.datetime.now()
        
        # Memory directories to check
        directories = [
            "thoughts",
            "confidence",
            "evaluations",
            "patterns",
            "embeddings",
            "performance",
            "benchmarks"
        ]
        
        # Check each directory for new files
        for directory in directories:
            dir_path = self.memory_path / directory
            if not dir_path.exists():
                continue
                
            # Get all files modified in the last hour
            recent_files = []
            for file_path in dir_path.glob("*.*"):
                if file_path.name == "README.md":
                    continue
                    
                mtime = datetime.datetime.fromtimestamp(file_path.stat().st_mtime)
                if (now - mtime).total_seconds() < 3600:  # Last hour
                    recent_files.append(file_path)
                    
            if recent_files:
                changes[directory] = recent_files
                
        return changes
    
    def _update_changelog(self, changes):
        """Update changelog with new changes"""
        if not changes:
            return
            
        # Read existing content
        with open(self.changelog_path, "r") as f:
            content = f.read()
            
        # Add new entry
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"## Changes - {timestamp}\n\n"
        
        for directory, files in changes.items():
            entry += f"### {directory.capitalize()}\n\n"
            
            for file_path in files:
                file_info = f"- `{file_path.name}`"
                
                # Add summary for JSON files
                if file_path.suffix == ".json":
                    try:
                        with open(file_path, "r") as f:
                            data = json.load(f)
                            
                        if "task" in data:
                            file_info += f": {data['task'][:50]}..."
                        elif "domain" in data:
                            file_info += f": Domain - {data['domain']}"
                    except:
                        pass
                        
                # Add summary for markdown files
                elif file_path.suffix == ".md":
                    try:
                        with open(file_path, "r") as f:
                            lines = f.readlines()
                            
                        for line in lines:
                            if line.startswith("# "):
                                file_info += f": {line[2:].strip()}"
                                break
                    except:
                        pass
                        
                entry += file_info + "\n"
                
            entry += "\n"
            
        # Write updated content
        with open(self.changelog_path, "w") as f:
            f.write(entry + content)
        
        print(f"Updated changelog with {sum(len(files) for files in changes.values())} files")

# When run directly
if __name__ == "__main__":
    processor = MemoryProcessor()
    changes = processor.process_changes()
    
    print("Memory Processor Results:")
    for directory, files in changes.items():
        print(f"  {directory}: {len(files)} files")
