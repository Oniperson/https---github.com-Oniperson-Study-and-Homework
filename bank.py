def bank():
    x = str.lower(input("Greeting: ")).strip()
    if x.startswith("h") and x.startswith("hello") == False:
        print("20$")
    elif x.startswith("hello") and len(x) >= 5:
        print("0$")
    elif x == "hello":
        print("0$")
    else:
         print("100$")

bank()
    