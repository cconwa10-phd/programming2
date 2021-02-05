#Ciara Conway - cconwa10@uncc.edu
#Assignment 1

import math as m

def user_input_first_layer(): #This is the initil input that shows the list and forces the user to choose a viable option
    choice = ["Ants", "Polygon", "Beethoven","Colors", "Hair"]
    while True:
        try:
            print(choice)
            answer = input("Welcome to 'random conversions', please select from the list above\n")
        except ValueError:
            print("This is not a viable option, please select from the list")
        else:
            for i in range(0,len(choice)): #This loop runs through the list of 5 functions and prints a - until condition is met
                if answer != choice[i]: #If not a viable option goes to the try block and repeats
                    print("-")
                else:
                    return answer #returns the answer to be called on again

def user_input_second_layer():#Try/Except Loop for User input that is used for specific ranges depending on the conversion choice
    while True:
        try:
            answer_2 = float(input("Input:\n"))
        except ValueError:
            print("This is not a viable option, please try again")
        else:
            if int(answer_2) > 500 or int(answer_2) < 1: #makes sure the answer is between the two values
                print("This is not a viable option, your input must be between 1 and 500")
            else:
                return answer_2 #returns the answer to be called on again

def user_input_third_layer():#Try/Except Loop for User input
    while True:
        try:
            answer_3 = float(input("Input:\n")) #makes sure the answer is a number
        except ValueError:
            print("This is not a viable option, please try again")
        else:
            return answer_3 #Returns the answer to be called on again


def entire_user_input(): #This is the core function that will be called by the main function, depending on user input
    user_input = user_input_first_layer()
    if user_input == "Ants":
        ant_conversion()
    elif user_input == "Polygon":
        polygon_conversion()
    elif user_input == "Beethoven":
        composition_music()
    elif user_input == "Colors":
        wavelength_colors()
    elif user_input == "Hair":
        hair()

def ant_conversion(): #Does 4 separate conversions dealing with weight(lbs, kg)
    print("Wonderful! You have chosen 'Ants'. Did you know Formic Acid was discovered and isolated in dead ants and that\nthe trivial name comes from the latin word for ant Formica?")
    print("Please insert your weight in lbs")
    weight_lbs = user_input_second_layer()
    conversion_factor = 1000000
    weight_kg = float(weight_lbs)/2.205
    ant_weight_kg = 2.5/conversion_factor
    if weight_lbs <= 150:
        ants = (weight_kg/ant_weight_kg)
        print("You weigh the equivalent of", ants, "ants.")

    elif weight_lbs <= 200:
        ant_strength = weight_lbs * 50
        print("If you had the strength of an ant you could carry", ant_strength,"lbs.")

    elif weight_lbs <= 300:
        ant_strength = ant_weight_kg * 50
        ant_carry = (weight_kg/ant_strength)
        print("It would require only", ant_carry,"ants to carry you.")

    else:
        formic_reserves = weight_kg*0.03
        print("If you had Formic Acid reverses like an ant, based on body mass, you would have",formic_reserves,"kg in your body.")
        print("The LD-50 for Formic Acid is 700mg - 1100mg/1kg.")


def polygon_conversion(): #Does 5 separate area/vol calculations depending on number input
    print("Wonderful! You have chosen 'Polygon'. Viral shells come in many geometric shapes and sizes, but did you know a common form is a regular icosahedron?")
    print("Please provide a length between 1cm - 500cm.\n Provide the number only.")
    length_cm = user_input_second_layer()
    if length_cm <= 100:
        area_triangle = (m.sqrt(3)/4)*(length_cm**2)
        vol_triangle = (m.sqrt(3)/4)*(length_cm**3)
        print("With the length provided:",length_cm, "cm")
        print("The following area of an equilateral triangle was calculated to be", area_triangle,"cm^2")
        print("The following volume of an equilateral triangular prism was calculated to be", vol_triangle,"cm^3")

    elif length_cm <= 200:
        area_square = (length_cm**2)
        vol_square = (length_cm**3)
        print("With the length provided:",length_cm, "cm")
        print("The following area of a square was calculated to be", area_square,"cm^2")
        print("The following volume of a cube was calculated to be", vol_square,"cm^3")

    elif length_cm <= 300:
        area_pentagon = ((1/4)*m.sqrt(5*(5+2*m.sqrt(5)))*length_cm**2)
        vol_pentagon = ((1/4)*m.sqrt(5*(5+2*m.sqrt(5)))*length_cm**3)
        print("With the length provided:",length_cm, "cm")
        print("The following area of a pentagon was calculated to be", area_pentagon,"cm^2")
        print("The following volume of a pentagonal prism was calculated to be", vol_pentagon,"cm^3")

    elif length_cm <= 400:
        area_pentagon = (((3*m.sqrt(3))/2)*length_cm**2)
        vol_pentagon = (((3*m.sqrt(3))/2)*length_cm**3)
        print("With the length provided:",length_cm, "cm")
        print("The following area of a hexagon was calculated to be", area_pentagon,"cm^2")
        print("The following volume of a hexagonal prism was calculated to be", vol_pentagon,"cm^3")

    else:
        vol_icosahedron = ((5*(3+m.sqrt(5))/12)*length_cm**3)
        print("With the length provided:",length_cm, "cm")
        print("The following volume of an icosahedron was calculated to be", vol_icosahedron,"cm^3")
        print("Poliovirus, rhinovirus, and adenovirus have this structure.")


def composition_music(): #converts a sting of numbers to notes in A minor
    print("Wonderful! You have chosen 'Beethoven'. Did you know Beethoven composed most of his work in C-minor?")
    print("Please give a string of numbers. You can list the first 30 digits of Pi for all I care.\n No decimals please!")
    num = user_input_third_layer()
    string_num = str(num)
    music = []

    for i in range(0, len(string_num) - 1): #For loop goes through each value, the minus 1 is to ensure it ends at the last input
        if string_num[i] == "0" or string_num[i] == "9":
            music.append("C")
        elif string_num[i] == "2" or string_num[i] == "4":
            music.append("F")
        elif string_num[i] == "1":
            music.append("D")
        elif string_num[i] == "3":
            music.append("E-Flat")
        elif string_num[i] == "5":
            music.append("B-Flat")
        elif string_num[i] == "6":
            music.append("A-Flat")
        elif string_num[i] == "7" or string_num[i] == "8":
            music.append("G")

    print("With your wonderful string of numbers I was able to convert it to a wonderful diddy. \nOne Beethoven would be proud of if he could hear it.")
    print(music)
    print("Might need an instrument of sorts to play or you can hum it out if you have perfect pitch")


def wavelength_colors(): #matches wavelength to the visible color or not visible range
    print("Wonderful! You have chosen 'Colors'. Did you know Sir Isaac Newton was one of the first scientists to pass white light through\na prism and see the spectrum of visible colors and document his findings?\n He published his findings in a work called Opticks.")
    print("Provide a number between 370 nm and 710 nm. Just the number please, no units.")
    wavelength = user_input_third_layer()
    if wavelength <= 380:
        print("Your entry of", wavelength, "nm, is in the ultraviolet range which is 380 nm or less")

    elif wavelength <= 450:
        print("Your entry of", wavelength, "nm, corresponds to the color Violet (381nm to 450nm)")

    elif wavelength <= 485:
        print("Your entry of", wavelength, "nm, corresponds to the color Blue (451nm to 485nm)")

    elif wavelength <= 500:
        print("Your entry of", wavelength, "nm, corresponds to the color Cyan (486nm to 500nm)")

    elif wavelength <= 565:
        print("Your entry of", wavelength, "nm, corresponds to the color Green (501nm to 565nm)")

    elif wavelength <= 590:
        print("Your entry of", wavelength, "nm, corresponds to the color Yellow (566nm to 590nm)")

    elif wavelength <= 625:
        print("Your entry of", wavelength, "nm, corresponds to the color Orange (591nm to 625nm)")

    elif wavelength <= 740:
        print("Your entry of", wavelength, "nm, corresponds to the color Red (626nm to 740nm)")

    else:
        print("Your entry of", wavelength, "nm, is in the infared range which is 741 nm or more")


def hair(): #by length of hair given, calculates the length of each hair end on end
    print("Estimate how long your hair is. Please estimate length in inches")
    length = user_input_second_layer()
    length_m = length*0.0254*100000
    length_km = length_m/1000
    if length <= 0.4:
        print("Based on the length you gave in addition to the average number of hairs on a human head...")
        print("If all of your hairs were set end to end they would measure",length_km,"km.")

    elif length <= 0.7:
        print("Based on the length you gave in addition to the average number of hairs on a human head...")
        print("If all of your hairs were set end to end they would measure",length_km,"km.")
        print("This is the distance range of a 'Fun Run'(1 mile) if not more, if you call running 'fun'.")

    elif length <= 2.5:
        print("Based on the length you gave in addition to the average number of hairs on a human head...")
        print("If all of your hairs were set end to end they would measure",length_km,"km.")


    elif length <= 3:
        print("Based on the length you gave in addition to the average number of hairs on a human head...")
        print("If all of your hairs were set end to end they would measure",length_km,"km.")
        print("This is the distance range of a 7K, or the distance needed to hatch an alolan pokemon in PokemonGo.")

    elif length <= 7.9:
        print("Based on the length you gave in addition to the average number of hairs on a human head...")
        print("If all of your hairs were set end to end they would measure",length_km,"km.")

    elif length <= 8.5:
        print("Based on the length you gave in addition to the average number of hairs on a human head...")
        print("If all of your hairs were set end to end they would measure",length_km,"km.")
        print("This is the distance range of a 21K, or a half-marathon.")

    else:
        print("Based on the length you gave in addition to the average number of hairs on a human head...")
        print("If all of your hairs were set end to end they would measure",length_km,"km.")



def main(): #Main function that gives the flow of the program
    entire_user_input()



if __name__ == '__main__':
    main()








