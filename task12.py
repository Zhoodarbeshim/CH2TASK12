word = "word"
letter = word.count("f")

if "f" not in word:
    print("None")
if "f" in word:
    if letter == 1:
        print(word.index("f"))