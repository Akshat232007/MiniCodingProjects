import random as r

number = int(r.randint(1,100))
guess = False
guess_count = 0

while not guess:
    guess_no = int(input("Enter Number : "))
    
    if type(guess_no) == int:
        if guess_no > number:
            print("Lower Number Please...")
            guess_count+=1
        elif guess_no < number:
            print("Higher Number Please...")
            guess_count+=1
        elif guess_no == number:
            print(f"Number of Guesses to reach to the number {number} : {guess_count}")
            guess = True
    else:
        print("Wrong Input")