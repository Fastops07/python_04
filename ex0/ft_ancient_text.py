import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
    file_path: str = sys.argv[1]
    file: typing.IO[str] | None = None
    print(f"Accessing file '{file_path}'")

    try:
        file = open(file_path, "r")
        content: str = file.read()
        print("---\n")
        print(content)
        print("\n---")
    except OSError as err:
        print(f"Error opening file '{file_path}': {err}")
    finally:
        if file is not None:
            file.close()
            print(f"File '{file_path}' closed.")


if __name__ == "__main__":
    main()
