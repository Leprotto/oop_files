import os


file_paths = [
    r'C:\Users\Maria\PycharmProjects\oop_files\1.txt',
    r'C:\Users\Maria\PycharmProjects\oop_files\2.txt',
    r'C:\Users\Maria\PycharmProjects\oop_files\3.txt'
]
file_data = {}
for file_path in file_paths:
    with open(file_path, encoding='utf-8') as file:
        lines = file.readlines()
        line_count = len(lines)
        file_content = f"{os.path.basename(file_path)}\n{line_count}\n" + ''.join(lines).strip()
        file_data[line_count] = file_content

sorted_files = sorted(file_data.items(), key=lambda x: x[0])

with open('combined.txt', 'w', encoding='utf-8') as combined_file:
    for key, file_content in sorted_files:
        combined_file.write(file_content)
        combined_file.write('\n')