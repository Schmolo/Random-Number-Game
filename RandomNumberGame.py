from random import randint

def main():
    # Generate random number 0-100
    rngNumber = randint(0, 100)

    # loop until return statement
    while True:
        try:
            # Get User input and convert to Int
            inputNumber = int(input("Guess the number(0-100): "))

            # Check if the Random Number is equal to User Input. If true print "You guessed the Number correctly!" and exit the Program succesfully.
            if rngNumber == inputNumber:
                print("You guessed the Number correctly!")
                return 0

            # Else Check if Random Number is greater than User Input. If true print "The random Number is higher than {inputNumber}" and go back to User Input.
            elif rngNumber > inputNumber:
                print(f"The random Number is higher than {inputNumber}")

            # Else print "The random Number is lower than {inputNumber} and go back to User Input.
            else:
                print(f"The random Number is lower than {inputNumber}")
    
        # In Case of ValueError (if UserInput is anything than a Number) and print "Thats not a valid Number! Try something between 0 and 100" and go back to User Input.
        except ValueError: 
            print("Thats not a valid Number! Try something between 0 and 100")
        
        # In Case of KeyboardInterrupt (if User presses CTRL + C) print "You have closed this Program!" and exit Program with "return 1".
        except KeyboardInterrupt:
            print("\n You have closed this Program!")
            return 1

        # In Case of Unknown exeption print "something went wrong!" and exit Program with "return 2"
        except:
            print("something went wrong!")
            return 2

if __name__ == '__main__':
    main()

# https://docs.python.org/3/library/random.html