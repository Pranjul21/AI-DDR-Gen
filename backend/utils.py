import os


def read_file(file_path: str) -> str:
    try:
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return "Not Available"

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().strip()

        return content if content else "Not Available"

    except Exception:
        return "Not Available"


def save_output(file_path: str, content: str) -> None:
    try:
        directory = os.path.dirname(file_path)
        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"Output saved at: {file_path}")

    except Exception:
        print("Error saving file")