import re
from collections import Counter 

word_regex = re.compile(r"\w+", re.U)

text = """Mary had a little lamb, little lamb,
    little lamb, Mary had a little lamb
    whose fleece was white as snow.
    And everywhere that Mary went
    Mary went, Mary went, everywhere
    that Mary went
    The lamb was sure to go."""

# extract all words from the text, ignoring punctuation and case
words = word_regex.findall(text.lower())

# Count how many times each word appears
counts = Counter(words) # This is essentially our "bag of words"

items = list(counts.items())

# Extract word dictionary and vector representation
word_dict = dict([[items[i][0], i] for i in range(len(items))])
text_vector = [items[i][1] for i in range(len(items))]

print(text_vector)
print(word_dict)