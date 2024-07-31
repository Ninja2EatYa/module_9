def all_variants(text):
    length = len(text) + 1
    for j in range(1, length):
        for k in range(length - j):
            yield text[k: k + j]


a = all_variants("abc")
for i in a:
    print(i)