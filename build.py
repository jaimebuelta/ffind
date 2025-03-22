import os
import subprocess
from pathlib import Path
from hatchling.build import build_package

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

def build_package_with_man_pages(*args, **kwargs):
    """Build the package and include man pages."""
    # First run the standard build
    build_package(*args, **kwargs)
    
    # Then install man pages if we're in install mode
    if kwargs.get('install', False):
        install_man_pages()

if __name__ == "__main__":
    build_package_with_man_pages() 