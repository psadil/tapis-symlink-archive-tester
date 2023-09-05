import argparse
from pathlib import Path


def main(root: Path) -> None:
    file = root / "file"
    file.touch()
    link = root / "link"
    link.symlink_to(file)

    print(f"{file=}")
    print(f"{link=}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)

    args = parser.parse_args()
    main(root=args.root)
