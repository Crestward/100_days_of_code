import random as rand

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")

difficulty = input("Please choose a difficulty. Type 'easy' or 'hard': ")

lives = 0 

if difficulty == 'easy':
    lives = 10
elif difficulty == 'hard':
    lives = 5

print(f"You have {lives} attempts remaining to guess the number")

num = rand.randint(1,100)

end_game = False
while end_game == False:
    guess = int(input("Make a guess: "))
    if guess > num:
        lives -= 1
        print("Too high")
        print("Guess again")
        print(f"You have {lives} attempts remaining to guess the number\n")
    elif guess < num:
        lives -= 1
        print("Too low")
        print("Guess again")
        print(f"You have {lives} attempts remaining to guess the number\n")
    elif guess == num:
        end_game = True
        print("Correct. You win!")
    elif lives == 0:
        end_game = True