text = open("Harry Potter 1 - Sorcerer's Stone.txt").readlines()
for line in text:
    line = line.strip()
    words = line.split(" ")
    words = [word for word in words if word.startswith("a")]
    new_line = " ".join(words)
    print(new_line)
