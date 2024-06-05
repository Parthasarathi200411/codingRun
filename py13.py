def find_common_and_modify(str1, str2):
    common_char = set(str1) & set(str2)
    str2_modified = ''
    for char in str2:
        if char in common_char:
            str2_modified += char * 2
        else:
            str2_modified += char
    str1_modified = ''.join([char.upper() if char in common_char else '' for char in str1])
    return str1_modified, str2_modified

def get_vowels_without_repetition(string):
    vowels = set('aeiouAEIOU')
    return list(set(filter(lambda char: char in vowels, string)))

def get_words_from_user(chars):
    words = []
    for char in chars:
        word = input(f"Enter a word for character '{char}': ")
        words.append(word)
    return words

def process_words(words):
    lengths = []
    for word in words:
        length = len(word)
        lengths.append(length)
        if length % 2 == 0:
            word = word.upper()
        else:
            ascii_sum = sum(ord(c) for c in word)
            if is_prime(ascii_sum):
                print(f"Sum of ASCII values ({ascii_sum}) of '{word}' is prime.")
            else:
                print(f"Sum of ASCII values ({ascii_sum}) of '{word}' is not prime.")
    return lengths

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Main program
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

modified_string1, modified_string2 = find_common_and_modify(string1, string2)

print("Modified first string:", modified_string1)
print("Modified second string:", modified_string2)

length_string1 = len(modified_string1)
length_string2 = len(modified_string2)

print("Length of the first string:", length_string1)
print("Length of the second string:", length_string2)

vowels = get_vowels_without_repetition(string1 + string2)
print("Vowels without repetition:", vowels)

words = get_words_from_user(vowels)
print("Words entered:", words)

word_lengths = process_words(words)
print("Lengths of words:", word_lengths)