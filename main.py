correct_count = 0
wrong_count = 0

name = input("Please enter your name: ")
print(f"\nHello {name}\n")
print("This is a math game to help you learn!\n")

print("Let's start with something simple, a 1 + 1 question :)")
print()
choice = input("What is 1 + 1: [250 or 2]? ").strip()
print()

if choice == "2":
    
    print("Good job :)")
    print()
    correct_count += 1
else:
    print("you suck lmao")
    wrong_count += 1  

if wrong_count == 0 and correct_count == 1:
    print("ok round two lets see how you do with this")
    print()
    choice = input("what if 3 X 2? [100 or 6]")

    if choice == "6":
        print()
        print("nice one, two in a row :)")
        correct_count += 1
    else:
        print("ok maybe your not that advanced, lets go easier")
        wrong_count += 1

print()
if wrong_count == 1 and correct_count == 0:
    print("ok because you suck lets make this even easier... cus you suck")
    print()
    choice = input("what is 0? [0 or 1]")

    if choice == "0":
        print("ok at least your not this stupid")
        print()
        correct_count += 1
    else:
        print()
        print("HOW ARE YOU THIS DUMB")
        print()
        print("SCREW THIS I QUIT, SEE YA")
        print()
        print("... oh and no im not showing you your score... BYE MF")
        exit()

# Show results
print(f"\nGame Over! Here's how you did:")
print(f"Correct answers: {correct_count}")
print(f"Wrong answers: {wrong_count}")
