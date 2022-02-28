import random

print("Welcome!!!")

rock = '''
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        '''
paper = '''
            _______
        ---'   ____)____
                  ______)
                  _______)
                 _______)
        ---.__________)
        '''

scissors = '''
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        '''

lst = [rock, paper, scissors, 3]


while True:
    player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors (3 to quit):"))

    comp = random.randint(0,2)
    if player or comp not in lst:
        print("Invalid choice")
        break
    
    print("You chose:")
    print(lst[player])


    if player == 3:
        break
    
    print("Computer chose:")
    print(lst[comp])

    if comp == 0 and player == 0:
        print("It is a draw")
    elif comp == 1 and player == 1:
        print ("It is a draw")
    elif comp == 2 and player == 2:
        print("It is a draw")
    elif comp == 0 and player == 1:
        print("You win")
    elif comp == 0 and player == 2:
        print("Computer wins")
    elif comp == 1 and player == 0:
        print("Computer wins")
    elif comp == 1 and player == 2:
        print("You win")
    elif comp == 2 and player == 0:
        print("You win")
    elif comp == 2 and player == 1:
        print("Computer wins")
