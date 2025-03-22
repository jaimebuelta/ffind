import os
import subprocess
from pathlib import Path
from hatchling.build import BuildHookInterface

class ManPageHook(BuildHookInterface):
    def initialize(self, version, build_data):
        """Add man pages to the build data."""
        man_dir = Path(__file__).parent / "man_pages"
        if man_dir.exists():
            build_data['artifacts'].extend([
                str(man_dir / "ffind.1"),
                str(man_dir / "install.sh")
            ])

    def finalize(self, version, build_data, artifact_path):
        """Install man pages after the build."""
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