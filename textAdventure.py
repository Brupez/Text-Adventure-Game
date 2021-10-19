while True:
    answer = input("Would you like to play? (yes/no) ")

    #take answer and show it with lowercase letters and strip the text behind (yes or no)
    if answer.lower().strip() == "yes":

        answer = input("\nYou see a person asking for help, it seems he is injured, would you like to help him?\n").lower().strip()
        if answer == "yes":
            answer = input("\nIt seems that a snake bite his leg! Will you give him 'medicine' or 'carry him'?\n")

            if answer == "medicine":
                print("\nCongratulations! you saved him")

            elif answer == "carry him":
                print("\nThe snake appears and poison you too, you died. Shame...")

            else:
                print("\nInvalid choice, you lost!")

        elif answer == "no":
            print("\nThe guy needing help saw you ignore him so he draws a pistol and shoot you where you stand, GAME OVER you horrible person!")

        else:
            print("\nInvalid choice, you lost!")

    else:
        print("\nThat's to bad!")
        break