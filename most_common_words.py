from collections import Counter
import gzip
import matplotlib.pyplot as plt 
import numpy as np

data = []

for line in gzip.open("text8.gz"):
    data.extend(line.strip().split())

counts = Counter(data)

sorted_counts = sorted(list(counts.items()), key=lambda x:x[1], reverse=True)

for word, count in sorted_counts[:100]:
    print(word, count)


dist = Counter(counts.values())
dist = list(dist.items())
dist.sort(key=lambda x:x[0])
dist = np.array(dist)

norm = np.dot(dist.T[0], dist.T[1])

plt.loglog(dist.T[0], dist.T[1]/norm)
plt.xlabel("count")
plt.ylabel("P(count)")
plt.title("Word frequency distribution")
plt.savefig("freq.png")

stopwords = set([word for word, count in sorted_counts[:100]])

clean_data = []

for word in data:
    if word not in stopwords:
        clean_data.append(word)

print("Original size:", len(data))
print("Clean size:", len(clean_data))