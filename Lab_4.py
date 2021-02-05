#Ciara Conway, cconwa10@uncc.edu
#Beginning of story
print("You are an Astrobiologist on an experimental expedition to Mars. Your goal is to find new life, study it, and then bring back to earth.")

while 1: #Try/Except loop to handle invalid inputs
    try:
        answer_1_input = input("Would you like to accept this mission? Yes or No?")
    except ValueError:
        print("This is not a viable option, Yes or No \n")
    else:
        if answer_1_input != "Yes" and answer_1_input != "No":
            print("This is not a viable option, please choose Yes or No")
        else:
            break

if answer_1_input == "Yes": #If/Else statement for first answer
    print("Wonderful choice, it is your lucky day. While out foraging, the crew found promising samples. Looks like you've got work to do!")
    print("You culture the sample and find there are moving unicellular microbes, the crew is excited and pressing you to further your results.")
else:
    print("Probably the best choice you could have made, you are smart and have seen enough sci-fi movies to know this is not a good idea!")

while 1: #Try/Except loop to handle invalid inputs
    try:
        answer_2_input = input("Would you like to add glucose growth serum to the cell culture? Yes or No?")
    except ValueError:
        print("This is not a viable option, Yes or No \n")
    else:
        if answer_2_input != "Yes" and answer_2_input != "No":
                print("This is not a viable option, please choose Yes or No")
        else:
            break
if answer_2_input == "Yes": #If/Else statement for second answer
    print("Whoa! Looks like the growth of the cells is beyond your expectations and are forming into something organized, complex.")
    print("You leave the new life form to grow, but it seems like something sinister is occurring, it seems intelligent.")
else:
    print("You didn't fall to peer pressure and as a result have lost your job.  Congrats! You are going back to Earth.")


while 1: #Try/Except loop to handle invalid inputs
    try:
        answer_3_input = input("With the growth becoming uncontrollable, do you terminate the life form? Yes or No?")
    except ValueError:
        print("This is not a viable option, Yes or No \n")
    else:
        if answer_3_input != "Yes" and answer_3_input != "No":
                print("This is not a viable option, please choose Yes or No")
        else:
            break
if answer_3_input == "No": #If/Else statement for third answer
    print("Well, now the life form has escaped containment and is killing crew mates one after the other.")
    print("You are the last person alive from the expedition, the only way to kill it is to shoot the life form off into deep space")
else:
    print("You may not get a Nobel Prize anytime soon, but you also just saved your crew mates")

while 1: #Try/Except loop to handle invalid inputs
    try:
        answer_4_input = input("Will you do anything necessary to expel the life form into deep space? Yes or No?")
    except ValueError:
        print("This is not a viable option, Yes or No \n")
    else:
        if answer_4_input != "Yes" and answer_4_input != "No":
                print("This is not a viable option, please choose Yes or No")
        else:
            break
if answer_4_input == "Yes": #If/Else statement for fourth answer, also END
    print("You are successful in pushing the life form out into deep space, but the only way to accomplish was to also sacrifice yourself and accompany the life form into deep space.")
    print("So now you are dead and Earth may not know, but you saved everyone.... or did you? Was the life form so smart, it was able to make it to Earth?!")
    print("Cue suspenseful music")
    print("THE END")
else:
    print("Since you have decided to stay on Mars, you will live your days in fear, constantly escaping the growing life form.")
    print("You will have to learn to grow potatoes and create water from O2 and H2, if not you will have enough supplies for 3 years")
    print("THE END")
