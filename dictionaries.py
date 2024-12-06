def count_word_frequency(file_name):
    with open(file_name, 'r') as file:
        words = file.read().lower().split()
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
    for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"{word}: {count}")
count_word_frequency(r"file_name")