"""
Word Occurrences
Estimate: 1hour
Actual:45 minutes
"""
word_counts = {}
text = input("Enter a string: ")
words = text.split()
for word in words:
    word = word.strip('.,!?').lower()
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
max_width = max(len(word) for word in word_counts)
for word, count in sorted(word_counts.items()):
    print(f"{word:{max_width}} : {count}")
