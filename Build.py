import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

# NOT WORKING RN
setup(
    name="psgroEngine Scene Replayer",
    version="0.0.1",
    description="Pygame module based psgroEngine Scene replayer testing",
    author="SONGRO STUDIO_",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": [
                "README.md",
                "LICENSE",
                "requirements.txt",
                "src",
                "GameSetting.py",
            ],
        }
    },
    executables=[Executable("Main.py", base=base)],
)