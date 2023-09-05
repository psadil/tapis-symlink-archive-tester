from pathlib import Path

file = Path("file").absolute()
file.touch()
Path("link").absolute().symlink_to(file)
