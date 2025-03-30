import os
import yaml
from pathlib import Path

class RepositoryEvaluator:
    def __init__(self, repo_path="c:/repo/smolagents"):
        self.repo_path = Path(repo_path)
        self.results = {
            'directory_structure': {},
            'github_actions': {},
            'memory_versioning': {},
            'benchmarks': {}
        }
        self.load_checklist()

    def load_checklist(self):
        checklist_path = self.repo_path/'memory/evaluations/checklist.yaml'
        with open(checklist_path) as f:
            self.checklist = yaml.safe_load(f)

    def evaluate_directory_structure(self):
        required_dirs = self.checklist['evaluation_criteria']['directory_structure'][0]['required_directories']
        self.results['directory_structure']['missing'] = [
            str(d) for d in required_dirs 
            if not (self.repo_path/d).exists()
        ]
        
        init_files = list(self.repo_path.glob('src/**/__init__.py'))
        self.results['directory_structure']['init_files'] = len(init_files) > 10

    def evaluate_github_actions(self):
        workflow_files = list((self.repo_path/'.github/workflows').glob('*.yml'))
        self.results['github_actions']['count'] = len(workflow_files)
        self.results['github_actions']['has_versioning'] = any(
            'sses-memory' in f.read_text() 
            for f in workflow_files
        )

    def evaluate_memory_versioning(self):
        memory_dir = self.repo_path/'memory'
        self.results['memory_versioning']['version_files'] = {
            'changelog': (memory_dir/'CHANGELOG.md').exists(),
            'versions': len(list(memory_dir.glob('v*'))),  # Pattern changed to v*
            'git_integration': (memory_dir/'.git').exists()
        }

    def evaluate_benchmarks(self):
        benchmark_dir = self.repo_path/'memory/benchmarks'
        self.results['benchmarks'] = {
            'test_cases': len(list(benchmark_dir.glob('*.json'))),
            'has_comparisons': (benchmark_dir/'comparisons').exists()
        }

    def generate_report(self):
        report = "# Repository Evaluation Report\n\n"
        report += "## Dependencies Status\n"
        report += "- SSES-6 (Fork): Done\n- SSES-7 (Dirs): Done\n- SSES-8 (GH Actions): Done\n- SSES-9 (Benchmarks): Done\n- SSES-25 (Tests): Backlog\n\n"
        
        report += "## Directory Structure\n"
        report += f"- Missing directories: {self.results['directory_structure'].get('missing', [])}\n"
        report += f"- Init files present: {self.results['directory_structure'].get('init_files', False)}\n\n"
        
        report += "## GitHub Actions\n"
        report += f"- Workflow files: {self.results['github_actions'].get('count', 0)}\n"
        report += f"- Memory versioning integrated: {self.results['github_actions'].get('has_versioning', False)}\n\n"
        
        report += "## Memory Versioning\n"
        report += f"- Changelog exists: {self.results['memory_versioning']['version_files']['changelog']}\n"
        report += f"- Stored versions: {self.results['memory_versioning']['version_files']['versions']}\n"
        report += f"- Git integration: {self.results['memory_versioning']['version_files']['git_integration']}\n\n"
        
        report += "## Benchmarks\n"
        report += f"- Benchmark cases: {self.results['benchmarks']['test_cases']}\n"
        report += f"- Comparison data: {self.results['benchmarks']['has_comparisons']}\n\n"
        
        report += "## Recommendations\n"
        report += "1. Complete SSES-25 test suite implementation\n"
        report += "2. Add version rollback mechanism documentation\n"
        report += "3. Standardize benchmark comparison format"
        
        return report

if __name__ == "__main__":
    evaluator = RepositoryEvaluator()
    evaluator.evaluate_directory_structure()
    evaluator.evaluate_github_actions()
    evaluator.evaluate_memory_versioning()
    evaluator.evaluate_benchmarks()
    print(evaluator.generate_report())