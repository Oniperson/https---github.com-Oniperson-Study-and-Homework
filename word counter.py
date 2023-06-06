list = "Help! Not just anybody Help! You know I need someone, Help!"
list = list.split()
count = 0
help = "Help!"
for character in list:
    if character in help:
        count +=1
print (count)