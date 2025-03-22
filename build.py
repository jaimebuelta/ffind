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

if __name__ == "__main__":
    install_man_pages() 