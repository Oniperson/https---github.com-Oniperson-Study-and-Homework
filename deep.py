def question():
    x = str.lower(input("What is the answer to great question of life the universe and everything? "))
    if x == "42":
        print("yes.")
    elif x == ("fourty two"):
        print("yes.")
    elif x == ("fourty-two"):
        print("yes.")
    else:
        print("no.")


question()

