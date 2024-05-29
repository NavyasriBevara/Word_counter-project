def count(elements):
    # if there exists a key as "elements" then simply
    # increase its value.
    if elements in dictionary:
        dictionary[elements] += 1
 
    # if the dictionary does not have the key as "elements"
    # then create a key "elements" and assign its value to 1.
    else:
        dictionary.update({elements: 1})
 
 
# driver input to check the program.
 
Sentence = input()
sent=Sentence.strip()
# Declare a dictionary
dictionary = {}
punc='''/.,<>?:;\{}[]-_!~`@#$%^&*()'''
for ele in sent:
    if ele in punc:
        sent=sent.replace(ele," ")

# split all the word of the string.
lst = sent.split()
print(f"Total number of words in given text:{ len(lst)}")
 
# take each word from lst and pass it to the method count.
for elements in lst:
    count(elements)
print(f"Frequency of Each word in a given text:")
# print the keys and its corresponding values.
for allKeys in dictionary:
    print (f"{allKeys}:{ dictionary[allKeys]}")
    
