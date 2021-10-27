#18◑ Write a program to print the 50 most frequent bigrams (pairs of adjacent words) of a text, omitting bigrams that contain stopwords.
import nltk # Import the Natural Language Toolkit
from nltk.book import * # From the Natural Language Toolkit book, import all
all_text1_bigrams = [] # We're making an empty list of all the bigrams in text 1 (Moby Dick)
for i in range(len(text1)-1): # We're iterating through each word/item (i) in the range of the whole length of text 1.  The -1 at the end of the line
                                # prevents the error that would occur if the program tried to make a bigram using the last member of the list as a
                                # bigram's first member and failed to find anything after it to serve as the second member.
    bigram = [text1[i].lower(), text1[i+1].lower()] # We're manually making a list of the bigrams in the text, putting one item (made lowercase) with the item after it (also made lowercase)
    if text1[i].lower().isalpha() == False: # If the first item in the bigram doesn't consist of characters in the alphabet...
        continue  # Continue (or skip, not printing anything in the dictionary)
    elif text1[i+1].lower().isalpha() == False:  # If the second item in the bigram doesn't consist of characters in the alphabet...
        continue  # Continue (or skip, not printing anything in the dictionary)
    else:  # Otherwise...
        all_text1_bigrams.append(bigram) # We're appending or adding each remaining bigram to the list of bigrams called all_text1_bigrams 
from nltk.corpus import stopwords # We're mporting the stopwords from the NLTK corpus (Stopwords are high-frequency function words).
def mostfreqnotstopwords(text): # We're defining the most frequent bigrams consisting of non-stopwords in a text such that...
    stopwords = nltk.corpus.stopwords.words('english') # ..."stopwords" refers to stopwords from the NLTK corpus for the English language
    alist = [] # We're making an empty list
    dict = {} # We're making a dictionary, such that...
    for x in range(len(text)): # ...we'll iterate through each word in the (range of the) whole length of the text.
        if text[x][0] in stopwords: # If the first word in a bigram isn't in the stopwords, we'll...
            continue # ...continue (or skip it, not printing anything in the dictionary).
        elif text[x][1] in stopwords: # If the second word in the bigram isn't in the stopwords, we'll...
            continue # ...continue (or skip, not printing anything in the dictionary).
        else:  # Otherwise (if neither word is in the stopwords) we'll...
            alist.append(text[x]) # Append or add it to the list (of bigrams which do not contain stopwords).
# In the four lines below, we'll put contents into the dictionary by counting how many times each bigram without stopwords appears in the text.
    for bigram in alist:  # For each bigram the list of bigrams not containing stopwords which we constructed above...
        if tuple(bigram) not in dict: # ...if the tuple or bigram is not yet in the dictionary...
            dict[tuple(bigram)] = 1  # ...we'll make its count "1."
        else: # Otherwise...
            dict[tuple(bigram)] += 1 # If the tuple or bigram is already in the dictionary, we'll increase its count by 1.

    newlist = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])} # We're making a new list, for which 
    # the letter "k" stands for "key" (which refers to the tuple or bigram in the dictionary entry) and "v" stands for "value," or the number
    # of times the bigram or tuple appears in the text.
    return list(newlist)[-50:-1] # We're determining the list of the last 50 items from the new list.
    
print(mostfreqnotstopwords(all_text1_bigrams)) #From among all the bigrams from Moby Dick, we're printing the most frequent (meaning top 50) that do not contain stopwords.


# 19 ◑ Write a program to create a table of word frequencies by genre, like the one given in 1 for modals. 
# Choose your own words and try to find words whose presence (or absence) is typical of a genre. Discuss your findings.
import nltk # Import the Natural Language Toolkit
from nltk.corpus import brown # Import the Brown Corpus from the Natural Language Toolkit corpus

cfd = nltk.ConditionalFreqDist( # We're creating a conditional frequency distribution (cfd) using the 
# Brown Corpus (A cfd is collection of frequency distributions, one for each condition.)
    (genre, word) # The condition here is the genre, and the words in the corpus are the events paired
    # with a condition.  For example, according to the table below, the condition of the genre "adventure"
    # is paired with the event "I" as (adventure, I) 652 times for this corpus.
    for genre in brown.categories()  # The genres are the 15 different categories in the Brown corpus
    for word in brown.words(categories=genre)) # The words are those in the Brown corpus.
    # And for each genre, we iterate through each word in that genre to make the pairs.  One example of a pair is (adventure, I),
    # that contains the condition (i.e. "adventure") and the event (i.e. "I").

genres = ['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies', 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']
# In the line above, we're defining genres as the list of the 15 categories in the Brown Corpus.
personalpronouns = ['I', 'you', 'we', 'he', 'she', 'they', 'me', 'us', 'him', 'her', 'it', 'them']
# In the line above, we're defining personal pronouns as this list of 12 words.
cfd.tabulate(conditions=genres, samples=personalpronouns) # Here we specify which conditions to display (genre), and similarly limit the 
# samples of the words to be displayed to just the personal pronouns.  We're having the program tabulate how many times each of the personal pronouns
# occurs in each genre, displaying the results in the table below:

#                   I  you   we   he  she they   me   us  him  her   it them 
#       adventure  652  362   87  761  240  206  207   47  415  444  492  156 
#  belles_lettres  845  188  398 1174  178  488  206  167  373  281 1059  298 
#       editorial  201   83  167  268   41  148   33   64  106   37  386   67 
#         fiction  511  236   85  813  280  230  137   37  375  397  458  172 
#      government   97   74  112  120    0   92   12   24   25    3  218   63 
#         hobbies  154  383  100  155   21  177   16   23   49   16  476  127 
#           humor  239  131   32  146   58   70   56   23   48   62  162   49 
#         learned  182   39  397  328   54  338   44   79   98  129  856  149 
#            lore  265  209  132  541  232  303   58   33  167  302  566  181 
#         mystery  583  340   62  670  219  106  114   33  330  296  515  120 
#            news  179   55   77  451   42  205   29   12   93  103  363   96 
#        religion  155  100  176  137   10  115   31   59   60    8  264   74 
#         reviews   49   29   40  161   42   74    9   21   40   85  206   45 
#         romance  951  456   78  702  496  168  193   42  339  651  573  142 
# science_fiction   98   81   30  139   36   53   20    6   58   71  129   47 

# Also, the total pronouns used for each genre was calculated by hand:

# adventure	7124
# belles_lettres	10277
# editorial	2918
# fiction	6715
# gov	1509
# hobbies	2857
# humor	1782
# learned	5165
# lore	5504
# mystery	5853
# news	3176
# religion	2123
# reviews	1524
# romance	8175
# scifi	1357

# The results listed above show that the total number of pronouns was lowest
# in reviews and government documents, and highest in romance and belles lettres,
# the latter of which refers to literature in which there is an emphasis on style.
# This includes poetry and dramas.  These findings might be explained by the high
# frequency of dialogs in romance novels and belles lettres, as this often involves personal
# pronouns (Biber et al., 2000).  Government documents and reviews, on the other hand, do not do so to the 
# same degree.

# Reference
# Biber, D., Johansson, S., Leech, G., Conrad, S., & Finegan, E. (2000). Longman grammar
#      of spoken and written English. London: Longman.