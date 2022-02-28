import random as rand

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/      
''')

stages = [
'''
  +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
========='''
,
'''  
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========='''
,
''' 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
'''
,
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(stages[6])

words = ['better', 'malawi', 'monk', 'huge']

cword = rand.choice(words)

lenword = len(cword)

# print(f'Chosen word is {cword}')

display = []
for l in range(lenword):
    display += '_'
print(display)

live = 6

endgame = False
while not endgame:
    chosen_word = input('Guess a letter: ').lower()

    if len(chosen_word) < 2:
        for l in range(lenword):
            p = cword[l]
            if chosen_word == p:
                display[l] = chosen_word
        if chosen_word not in cword:
            live -=1
            print(f'Your guess "{chosen_word}" is not in the word. You lose a life')
        if chosen_word in cword:
            print(f"You already guessed '{chosen_word}'")
        print(f'You have {live} lives remaining')
        print(stages[live])
        print(display)

        if live == 0:
            endgame = True
            print('You lose')

        if '_' not in  display:
            endgame = True
            print('You win')
    else:
        print('Please guess a letter at a time')
        break
