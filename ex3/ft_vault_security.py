def secure_archive(
    file_path: str, action: str = "read", content: str = ""
) -> tuple[bool, str]:

    if action == "read":
        try:
            with open(file_path, "r") as file:
                read_content: str = file.read()
            return (True, read_content)
        except OSError as err:
            return (False, str(err))

    elif action == "write":
        try:
            with open(file_path, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")
        except OSError as err:
            return (False, str(err))
    return (False, "Invalid action")


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    result: tuple[bool, str] = secure_archive("/not/existing/file")
    print(result)
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    result = secure_archive("/etc/master.passwd")
    print(result)
    print()

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    success: bool = result[0]
    previous_content: str = result[1]

    if success:
        result = secure_archive(
            "new_fragment.txt",
            "write",
            previous_content,
        )
    else:
        result = (False, "Could not read previous content")

    print(result)


if __name__ == "__main__":
    main()
