example = "yankee doodle went to town riding on a pony stuck a feather up his butt and called it macaroni"

vowels = ["a", "e", "i", "o", "u"]
count = 0
for letter in example:
    if letter in vowels:
        count += 1
print(count)