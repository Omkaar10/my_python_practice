def getCount(inputStr):
    # your code here
    num_vowels = 0
    list_vowel=['a','e','i','o','u'] #created a list for iterating the for loop
    for vowel in list_vowel:
        num_vowels+=inputStr.count(vowel) #making use of the list of vowels to check its occurrence and adding it to the num_vowels
    return num_vowels
