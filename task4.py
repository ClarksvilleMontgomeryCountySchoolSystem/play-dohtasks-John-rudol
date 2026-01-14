
"""
ANSWER BOX - Copy the strings you need:

"standing up or flopped down?"
") Keep it round.\n"
") Attach two pieces using {color2} hanging downward.\n"
") Name this creation: "Dog""
") Roll a smaller ball using {color1} for the head.\n"
"hot dog or round like a ball?"
") Roll a ball using {color1} for the body.\n"
") Attach two pointed pieces using {color2} upright.\n"
") Attach the head to the body.\n"
") Add four legs using {color1}, a small tail using {color2}, two eyes, and a nose.\n"
") Stretch it out.\n"
"""

def main():
    color1 = "blue"
    color2 = "red"
    print(f"1)Roll a ball using {color1} for the body\n")
    choice1 = input("This will be the body. Do you want it stretched long like a got dog or kept round like a ball?")
    if choice1 == "response to test":
     print("2)Stretch it out.\n")
    else:
     print("2) Keep it round\n")
    print(f"3) Roll a smaller ball using {color1} for the head.\n")
    print(f"4)Attach the head to the body.\n")
    choice2 = input("5)The ears go on the head. Do you want them standing up or flopped down?\n")
    if choice2 == "response to test":
     print(f"5) Attach two pointed pieces using {color2} upright.\n")
    else:
     print(f"6)Attach two pieces using {color2} hanging downward.\n")
    print(f"7) Add four legs using {color1}, a small tail using {color2}, two eyes, and a nose.\n")
    print("Name this creation: Dog")


if __name__ == "__main__":
    main()
