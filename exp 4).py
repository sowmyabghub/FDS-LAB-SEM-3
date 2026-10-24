import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import gutenberg

# Download required resources (run once, they will be cached)
nltk.download('gutenberg')
nltk.download('punkt')
nltk.download('punkt_tab')   # ✅ this fixes the LookupError

# Load the text from the Gutenberg corpus
sample = gutenberg.raw("austen-emma.txt")  # You can change to another text if needed

# Tokenize the sample text
tokens = word_tokenize(sample)

# Create a list of the first 50 tokens
wlist = [tokens[i] for i in range(50)]

# Calculate the frequency of each word in the list
wordfreq = [wlist.count(w) for w in wlist]

# Print the word-frequency pairs
print("Pairs\n" + str(list(zip(wlist, wordfreq))))
