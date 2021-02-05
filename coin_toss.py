#Ciara Conway, cconwa10@uncc.edu


from random import randint
#Random choice for computer
choice_program_set = ["Heads", "Tails"]
choice_program = choice_program_set[randint(0,1)]

while 1:  #Try/Except block to ensure valid options
    try:
        choice_flip = input("Please choose from the following: Heads or Tails")
    except ValueError:
        print("This is not a valid answer: Heads or Tails")
    else:
        if choice_flip != "Heads" and choice_flip != "Tail":
            print("This is not a valid answer: Heads or Tails")
        else:
            break

#Answer to the coin flip
if choice_flip == choice_program:
    print("You guessed",choice_flip,"and the answer is",choice_program)
    print("You were right!")
elif choice_flip != choice_program:
    print("You guessed",choice_flip,"and the answer is",choice_program)
    print("You were wrong!")
