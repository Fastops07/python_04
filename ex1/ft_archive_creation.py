import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    file_path: str = sys.argv[1]
    file: typing.IO[str] | None = None
    content: str | None = None
    print(f"Accessing file '{file_path}'")

    try:
        file = open(file_path, "r")
        content = file.read()
        print("---\n\n")
        print(content)
        print("\n---")
    except OSError as err:
        print(f"Error opening file '{file_path}': {err}")
    finally:
        if file is not None:
            file.close()
            print(f"File '{file_path}' closed.")

    if content is None:
        return 

    print("Transform data:")
    print("---")
    print()

    transformed_data:list[str] = [line + "#" for line in content.splitlines()]
    
    for line in transformed_data:
        print(line)
        
    print("\n---")

    file_name :str = input("Enter new file name (or empty): ")
    if file_name:
        print("Not saving data.")
    # else:
        # try open write close 
if __name__ == "__main__":
    main()

