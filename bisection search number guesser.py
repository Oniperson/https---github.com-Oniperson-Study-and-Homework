x = 100
low = 0 
high = x
answer = "i"

print ("please think of a number betwenn 1 and 100")

while answer != "c":
    guess = (low + high)/2
    print ("is your number " + str(guess))
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly: ")
    if answer == ("h"):
        high = guess
    elif answer == ("l"):
        low = guess
    elif answer == ("c"):
        print ("haha gottum")
        break
    else:
        print ("Sorry, that aint an option, bud")
