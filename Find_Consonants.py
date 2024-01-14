def count_consonanats(word):
    consonants = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    consonants_count = 0

    for char in word:
        if char in consonants:
            consonants_count += 1

    return consonants_count

input_word = input("Enter a word: ")
result = count_consonanats(input_word)
print(f"The number of consonanats in '{input_word}' is: {result}")