sent = input("Enter a sentence ")

def count_words(sent):
    words  = sent.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
result = count_words(sent)

def count_characters(sent):
    char = {}
    for c in sent:
        if c in char:
            char[c] += 1
        else:
            char[c] = 1
    return char
char_result = count_characters(sent)

def count_vowelsconsonants(sent):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for c in sent:
        if c in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    return vowel_count, consonant_count
vowel_result, consonant_result = count_vowelsconsonants(sent)

def most_frequent(sent):
    check = input("Enter word to check frequency ")
    check = sent.split()
    word_count = {}
    for word in check:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count 

def remove_duplicates(sent):
    words = sent.split()
    unique_words = set(words)
    return unique_words
unique_result = remove_duplicates(sent)

def display_aplhabetical(sent):
    words = sent.split()
    sorted_words = sorted(words)
    return sorted_words
alphabetical_result = display_aplhabetical(sent)

def reverse_sentence(sent):
    words = sent.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)
reversed_result = reverse_sentence(sent)

def total_words(sent):
    words = sent.split()
    return len(words)

while True:
    print("\n Word Analyzer Menu:")
    print("1. Count words")
    print("2. Count characters")
    print("3. Count vowels and consonants")
    print("4. Most frequent word")
    print("5. Remove duplicates")
    print("6. Display words in alphabetical order")
    print("7. Reverse sentence")
    print("8. Total words")
    print("9. Exit")
    choice = input("Enter choice ")

    if choice == "1":
        count_words(sent)
        print("Word Count: ", result)
    elif choice == "2":
        count_characters(sent)
        print("Character Count: ", char_result)
    elif choice == "3":
        count_vowelsconsonants(sent)
        print("Vowel Count: ", vowel_result)
        print("Consonant Count: ", consonant_result)
    elif choice == "4":
        count_words(sent)
        print("Most Frequent Word: ", most_frequent(sent))
    elif choice == "5":
        remove_duplicates(sent)
        print("Unique Words: ", unique_result)
    elif choice == "6":
        display_aplhabetical(sent)
        print("Words in Alphabetical Order: ", alphabetical_result)
    elif choice == "7":
        reverse_sentence(sent)
        print("Reversed Sentence: ", reversed_result)
    elif choice == "8":
        print("Total Words: ", total_words(sent))
    elif choice == "9":
        print("Exiting")
        break
    else:
        print("Invalid choice. Please try again.")
