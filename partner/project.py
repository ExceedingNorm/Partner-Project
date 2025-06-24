"""Project management utilities for Partner app."""
from pathlib import Path
import subprocess
from typing import Iterable


class Project:
    """Represents a software project on disk."""

    def __init__(self, root: Path) -> None:
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)

    def init_git(self) -> None:
        """Initialize a git repository if one does not exist."""
        if not (self.root / ".git").exists():
            subprocess.run(["git", "init"], cwd=self.root, check=True)

    def create_files(self, files: Iterable[str]) -> None:
        """Create empty files inside the project root."""
        for file in files:
            path = self.root / file
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch(exist_ok=True)

    def commit_all(self, message: str) -> None:
        """Commit all changes with the given commit message."""
        subprocess.run(["git", "add", "-A"], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-m", message], cwd=self.root, check=True)

