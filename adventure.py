import time
import random
for i in range(1):
    print("Time to play the adventure game?")
    
    def print_pause(message_to_print, pause):
        print(message_to_print)
        time.sleep(pause)

answer = input("Do you want to play this test adventure game? [yes/no]")

if answer == "no":
    print("Then its Goodbye! Thank you!")

if answer == "yes":

    print("That's great!")
    print()
    answer = input("Do you want to explore a cave or jungle? [cave/jungle]")
    
    if answer == "cave":
        print("You go into the cave and see a sleeping bear")
        print()
        answer = input("Do you want to fight or ran? [fight/run]")

        if answer == "fight":
            print("Bears are really strong! You lose!Do you want to reply")

        elif answer == "run":
            print("You ran away! You win!")

        else:
            print("Invalid option, you lose!")
            

    elif answer == "jungle":
        print("You will meet a tiger and you will get eaten! You lose!")


    else:
        print("Invalid option, you lose! please reenter a valid input")


    TODAY_DATE = 14
    date = float(input("What is today's date?"))

    while date > 14:
        print("No that's not the correct date! Do you want to retry? [yes/no]")

        if answer == "yes":

         print("That's great!")
         numberList = [111, 222, 333, 444, 555]
         print("random item from the list is:",random.chioce(numberList))

         if answer == "no":
           print("The End!")

        def replay():
            play_again = input("Would you like to play again? (yes/no)").lower()
            if play_again == "yes":
                print_pause("Restarting the game...")

            elif play_again == "no":
                print_pause("Thanks for playing! Goodbye!")

            else:
                replay()
                
    answer = input("Do you want to explore a cave or jungle? [cave/jungle]")
        
    time.sleep(2)

    YOUR_AGE = 50

    date = float(input("What is your age?"))

    while YOUR_AGE < 50:
        print("No that's not the correct answer please try again! [yes/no]")

        if answer == "yes":
            print("Then lets play!")

            if answer == "no":

             print("Are you scared")
    answer = input("Do you want to explore a car or lion? [car/lion]")
    
    if answer == "car":
        print("You go into the car and you ride it")
        print()
        answer = input("Do you want to sleep or play? [sleep/play]")

        if answer == "play":
            print("Lions are really strong! You lose!Do you want to replay")

        elif answer == "run":
            print("You ran away! You win!")

        else:
            print("Invalid option, you lose!")
            


        def replay():
            play_again = input("Would you like to play again? (yes/no)").lower()
            if play_again == "yes":
                print_pause("Restarting the game...")

            elif play_again == "no":
                print_pause("Thanks for playing! Goodbye!")

            else:
                replay()
                
                
 
