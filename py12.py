def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def process_strings(str1, str2):
    common_chars = set(str1).intersection(set(str2))
    str1 = ''.join([char.upper() if char in common_chars else char*2 for char in str1])
    str2 = ''.join([char for char in str2 if char not in common_chars])
    return str1, str2, ''.join(sorted(set(filter(lambda x: x in 'aeiouAEIOU', str1 + str2)), key=str1.index))

def main():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    
    processed_str1, processed_str2, vowels_list = process_strings(str1, str2)
    print(f"Processed first string: {processed_str1}")
    print(f"Processed second string: {processed_str2}")
    print(f"Length of the first string: {len(processed_str1)}")
    print(f"Length of the second string: {len(processed_str2)}")
    print(f"Vowels list: {vowels_list}")
    
    words_list = []
    for char in vowels_list:
        word = input(f"Enter a word for the vowel '{char}': ")
        words_list.append(word)
    
    lengths_array = []
    for word in words_list:
        length = len(word)
        lengths_array.append(length)
        if length % 2 == 0:
            print(word.upper())
        else:
            ascii_sum = sum(ord(char) for char in word)
            print(f"Sum of ASCII values: {ascii_sum}")
            print(f"Is the sum prime? {'Yes' if is_prime(ascii_sum) else 'No'}")

if _name_ == "_main_":
 main()