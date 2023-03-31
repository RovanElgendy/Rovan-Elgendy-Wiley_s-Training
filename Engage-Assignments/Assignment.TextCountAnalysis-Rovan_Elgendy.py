# Rovan Elgendy 12.03.2023
# Step 7: Perform a count analysis on the text without punctuation characters.
import string

s="""Imagine a vast sheet of paper on which straight Lines, Triangles, Squares, Pentagons, Hexagons, and other figures, instead of remaining fixed in their places, move freely about, on or in the surface, but without the power of rising above or sinking below it, very much like shadows - only hard and with luminous edges - and you will then have a pretty correct notion of my country and countrymen. Alas, a few years ago, I should have said "my universe": but now my mind has been opened to higher views of things."""
# Step 1
s_lower=s.lower()
print('the string in lower case letters : ',s_lower)
# Step 2
words=s_lower.split()
print('the string splitted:',words);print('the total number of words with punctuations: ',len(words))
#Step 3
listing=list()
words_dictionary=dict()
punctuation_list=list(string.punctuation)
for wo in words:
    if wo not in punctuation_list:
        listing.append(wo)
print('the list is:',listing);print('the number of words are: ',len(listing))
# Step 4
for each_word in listing:
    words_dictionary[each_word]=words_dictionary.get(each_word,0)+1
print(words_dictionary)
# Step 5
dist=set(words)
print('the distinct words: ',dist)
print('the number of distinct words: ',len(dist))
