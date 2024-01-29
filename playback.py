#object is to "slow down" someones speach by replacing spaces with elipses
def main():
    x = input("Type in some nonsense ")
    replaced = x.replace(" ", "...")
    print(replaced)
main()
