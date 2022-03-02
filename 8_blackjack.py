import random as rand

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print("Welcome to BALCKJACK")

def pick(cards):
    card = rand.choice(cards)
    return card
def game():
    your_cards = [pick(cards), pick(cards)]
    print(f"Your cards are card: {your_cards}")

    computer_card = [pick(cards), pick(cards)]
    comp_first_card = computer_card[0]
    print(f"Computer first card: {comp_first_card}")

    ano = input("Type 'y' to get another card, type'n' to pass: ")

    end_game = False
    while not end_game: 
        if ano == 'y':
            computer_card.append(pick(cards))
            your_cards.append(pick(cards))
            if sum(your_cards) > 21 and sum(computer_card) <= 21 :
                print(f"{your_cards}: You")
                print(f"{computer_card}: computer")
                print("You lose")
            elif sum(your_cards) <= 21 and sum(computer_card) > 21 :
                print(f"{your_cards}: You")
                print(f"{computer_card}: computer")
                print("You win")
        else:
            print(f"Your final hand: {your_cards}")
            print(f"Computer final hand: {computer_card}")
            if sum(your_cards) > 21 and sum(computer_card) <= 21 :
                print("You lose")
            elif sum(your_cards) < 21 and sum(computer_card) > 21 :
                print("You win")
            elif sum(your_cards) <= 21 and sum(computer_card) <= 21:
                if sum(your_cards) > sum(computer_card):
                    print("You win") 
                elif sum(your_cards) < sum(computer_card):
                    print("You lose")
                elif sum(your_cards) == sum(computer_card) :
                    print("Draw")
            
        cont = input("Do you want to play another game of Blackjack, type 'y' or 'n': ")
        if cont == 'n':
            end_game = True
            print("Goodbye")
            break
        elif cont == 'y':
            game()

game()
        


