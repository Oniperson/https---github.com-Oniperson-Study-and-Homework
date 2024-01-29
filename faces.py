def convert():
    x = input("How are you feeling today? ")
    replaced = x.replace(":)", "🙂").replace(":(", "🙁")
    print(replaced)

convert()