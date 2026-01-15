
def main():
    color1 = "pink"
    color2 = "teal"
    print(f"1) Use {color2} to roll a ball.\n")
    choice1 = input("1, 2, or 3? ")
    if choice1 == "1":
     print("2) Make the ball flat.\n")
    elif choice1 == "2":
     print("2) Form the ball into an egg shape.\n")
    else:
     print("2) Keep it round.\n")
    print(f"3) Use {color2} to roll two thin ropes.\n")
    choice2 = input("A or B? ")
    if choice2 == "A":
     print("4) Pinch off pieces of the thin ropes to make and attach spots.\n")
    else:
     print("4) Use the ropes to make stripes.\n")
     print("5) Add two tiny dots for eyes on the front.")
    choice3 = input()
    print(f"6) Write {choice3} on the name card.")

if __name__ == "__main__":
    main()
