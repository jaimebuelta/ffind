import os
import subprocess
from pathlib import Path

def install_man_pages():
    """Install man pages during package installation."""
    man_dir = Path(__file__).parent / "man_pages"
    install_script = man_dir / "install.sh"
    
    if install_script.exists():
        cmd = subprocess.Popen(
            [str(install_script)],
            stdout=subprocess.PIPE,
            cwd=str(man_dir),
            universal_newlines=True,
            env=dict(os.environ)
        )
        output = cmd.communicate()[0]
        print(output)

def build_hook(build_data):
    """Hook called during the build process."""
    # Add man pages to the build data
    man_dir = Path(__file__).parent / "man_pages"
    if man_dir.exists():
        build_data['artifacts'].extend([
            str(man_dir / "ffind.1"),
            str(man_dir / "install.sh")
        ])

def install_hook(install_data):
    """Hook called during installation."""
    install_man_pages()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        # Simulate build hook
        build_data = {"artifacts": []}
        build_hook(build_data)
        print("Build artifacts:", build_data["artifacts"])
    else:
        # Run install hook
        install_hook({}) 