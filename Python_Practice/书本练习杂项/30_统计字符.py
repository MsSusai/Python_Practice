sentence = "Life is short, we need Python"
sentence = sentence.lower()

counts = {}
# for char in sentence:
#     if char in counts:
#         counts[char] += 1
#     else:
#         counts[char] = 1

for char in sentence:
    counts[char] = counts.get(char, 0) + 1

for key, value in counts.items():
    print(key, value)
