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
        print("---")
    except OSError as err:
        print(f"Error opening file '{file_path}': {err}")
    finally:
        if file is not None:
            file.close()
            print(f"File '{file_path}' closed.")
            print()

    if content is None:
        return

    print("Transform data:")
    print("---")
    print()

    transformed_lines: list[str] = [
        line + "#" for line in content.splitlines()
    ]
    transformed_content: str = "\n".join(transformed_lines)
    transformed_content += "\n"
    print(transformed_content)

    print("---")

    file_name: str = input("Enter new file name (or empty): ")
    if not file_name:
        print("Not saving data.")
    else:
        file_to_write: typing.IO[str] | None = None
        try:
            file_to_write = open(file_name, "w")
            file_to_write.write(transformed_content)
        except OSError as err:
            print(f"Error opening file '{file_name}': {err}")
        finally:
            if file_to_write is not None:
                file_to_write.close()
                print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
