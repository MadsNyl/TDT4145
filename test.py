file_path = 'hovedscenen.txt'
search_word = 'Balkong'

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if line == "Balkong":
            print(f'"{search_word}" found in the file.')
    else:
        print(f'"{search_word}" not found in the file.')