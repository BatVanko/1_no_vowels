# vowels_list = ['a', 'o', 'u', 'e', 'i']
# text = input()
# no_vowels = [el for el in text if el not in vowels_list]
# print("".join(no_vowels))

vowels_list = ['a', 'o', 'u', 'e', 'i']
text = input()
no_vowels = list(filter(lambda x: x not in vowels_list, text))
print("".join(no_vowels))
