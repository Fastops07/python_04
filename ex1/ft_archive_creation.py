import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    file_path: str = sys.argv[1]
    file: typing.IO[str] | None = None
    content: str | None = None
    print(f"Accessing file '{file_path}'")

    try:
        file = open(file_path, "r")
        content = file.read()
        print("---\n")
        print(content)
        print("\n---")
    except OSError as err:
        print(f"Error opening file '{file_path}': {err}")
    finally:
        if file is not None:
            file.close()
            print(f"File '{file_path}' closed.")
            print()

    if content is None:
        return

    transformed_lines: list[str] = [
        line + "#" for line in content.splitlines()
    ]
    transformed_content: str = "\n".join(transformed_lines)

    print("Transform data:")
    print("---\n")
    print(transformed_content)
    print("\n---")

    try:
        file_name: str = input("Enter new file name (or empty): ").strip()
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        return

    if not file_name:
        print("Not saving data.")
    else:
        file_to_write: typing.IO[str] | None = None
        try:
            print(f"Saving data to '{file_name}'")
            file_to_write = open(file_name, "w")
            file_to_write.write(transformed_content)
            print(f"Data saved in file '{file_name}'.")
        except OSError as err:
            print(f"Error opening file '{file_name}': {err}")
        finally:
            if file_to_write is not None:
                file_to_write.close()


if __name__ == "__main__":
    main()
