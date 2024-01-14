def count_vowels(word):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in word:
        if char in vowels:
            vowel_count += 1

    return vowel_count

input_word = input("Enter a word: ")
result = count_vowels(input_word)
print(f"The number of vowels in '{input_word}' is: {result}")