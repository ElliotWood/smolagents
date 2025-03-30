import pytest
import yaml
from pathlib import Path

REQUIRED_WORKFLOWS = [
    ".github/workflows/tests.yml",
    ".github/workflows/quality.yml",
    ".github/workflows/build_documentation.yml"
]

class TestGitHubActions:
    @pytest.mark.parametrize("workflow_path", REQUIRED_WORKFLOWS)
    def test_workflow_files_exist(self, workflow_path):
        path = Path(workflow_path)
        assert path.exists(), f"Missing workflow file: {workflow_path}"
        assert path.is_file(), f"Path is not a file: {workflow_path}"

    @pytest.mark.parametrize("workflow_path", REQUIRED_WORKFLOWS)
    def test_workflow_valid_yaml(self, workflow_path):
        with open(workflow_path) as f:
            try:
                yaml.safe_load(f)
            except yaml.YAMLError as e:
                pytest.fail(f"Invalid YAML in {workflow_path}: {str(e)}")

    def test_ci_workflow_contents(self):
        path = Path(".github/workflows/tests.yml")
        with open(path) as f:
            workflow = yaml.safe_load(f)
            
        assert "tests" in workflow["name"].lower()
        assert "on" in workflow
        assert "push" in workflow["on"]
        assert "pull_request" in workflow["on"]
        
        jobs = workflow["jobs"]
        assert "test" in jobs
        assert "steps" in jobs["test"]
        
        steps = jobs["test"]["steps"]
        assert any(step.get("uses", "").startswith("actions/checkout") for step in steps)
        assert any("pytest" in step.get("run", "") for step in steps)