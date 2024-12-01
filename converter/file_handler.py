def read_file(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read().strip()

def save_results(filename: str, results: dict):
    with open(filename, 'w') as file:
        file.write("Результати конвертації:\n")
        for key, value in results.items():
            file.write(f"{key}: {value}\n")
