# Q3). Python Program to Detect if Two Strings are Anagrams
str1="ababa"
str2="babaa"
if len(str1) !=len(str2):
    print("not anagram")
else:
    for i in str1:
        if i in str2:
            continue
        else:
            print("Not Anagram")
    else:
        print("Anagram")
            
    
