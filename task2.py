def main():
    color1 = "blue"
    color2 = "red"
    print(f"1) Use {color2} to roll a ball.\n")
    choice1 = input(" 1, 2, or 3 ?")
    if choice1 == "response to test":
     print("2) Make the ball flat.\n")
    elif choice1 == "response to test": 
     print("2) Form the ball into an egg shape.\n")
    else: 
     print("2) Keep it round.\n")
    print(f"3) Use {color1} to roll two thin ropes.\n")
    choice2 = input(" A or B ?\n")
    if choice2 == "response to test":
     print("4) make skinny legs.\n")
    # Remember you are checking equality to a string. You must use quotes.
    if choice2 == "response to test":
     print("4) Pinch off pieces of the thin ropes to make and attach spots.\n")
    else:
     print("4) Use the ropes to make stripes.\n")
     print("5) Add two tiny dots for eyes on the front.\n")
    choice3 = input(" ")
    print(f"6) Write {choice3} on the name card.\n")

if __name__ == "__main__":
    main()
