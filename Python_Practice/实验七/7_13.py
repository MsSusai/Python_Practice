sentence = input("输入一句英文：")
sentence = sentence.lower()

counts = {}
for char in sentence:
    if char.isalpha():
        counts[char] = counts.get(char, 0) + 1
print(counts)
