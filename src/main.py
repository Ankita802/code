import os

def count_file_stats(filepath):
    if not os.path.isfile(filepath):
        return f"File '{filepath}' does not exist."

    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    lines = content.split('\n')
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_chars = len(content)

    return {
        "File": filepath,
        "Lines": num_lines,
        "Words": num_words,
        "Characters": num_chars
    }

if __name__ == "__main__":
    result = count_file_stats("example.txt")
    print(result)
