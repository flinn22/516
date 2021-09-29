#24
from nltk.book import * #From Natural Language Toolkit's book module, load all items
V = set(text6) #Let the V(ocabulary) equal the set of all the types in Text 6, Monty Python and the Holy Grail
ise_words = [w for w in V if w.endswith('ise')] #Let "ise_words" equal the set of all w(ords) such that a w(ord) is an element of the V(ocabulary) and has the property of ending in -ise.
print(ise_words) # Print the "ise_words"
z_words = [w for w in V if 'z' in w]  #Let "z_words" equal the set of all w(ords) such that a w(ord) is an element of the V(ocabulary) and has the property of containing the letter "z".
print(z_words) # Print the "z_words"
pt_words = [w for w in V if 'pt' in w] #Let "pt_words" equal the set of all w(ords) such that a w(ord) is an element of the V(ocabulary) and has the property of containing the letters "pt".
print(pt_words) # Print the "pt_words"
titlecase_words = [w for w in V if w.istitle()]  #Let "titlecase_words" equal the set of all w(ords) such that a w(ord) is an element of the V(ocabulary) and has the property of starting with a capital letter.
print(titlecase_words) # Print the "titlecase_words"

#25
sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore'] #Let our sent(ence) equal a list of the words in the tongue-twister, "She sells seashells by the seashore."
V = set(sent) #Let the V(ocabulary) equal the set of all the types in our sent(ence).
sh_words = [w for w in V if w.startswith('sh')] #Let "sh_words" equal the set of all w(ords) such that a w(ord) is an element of the V(ocabulary) and has the property of beginning with the letters "sh".
print(sh_words) #Print the "sh_words."
for index in range(len(sent)): #For each index (meaning item) within (the range of) our sentence...  (Len tells the loop to iterate through it until the index equals the length of the list, our sentence.)
    if len(sent[index]) > 4: #If the length of an index/item in the sentence is greater than 4 letters... 
        print(sent[index]) #...then print that index/item from the sentence. 