from random import choices


print("Welcome to Cipher")
print("Encrypt your texts \n")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
'u', 'v', 'w', 'x', 'y', 'z']


def cipher(plain_text, shift_amount, cipher_choice):
    encrypted_text = ""
    if cipher_choice == 'decode':
        shift_amount *= -1
    for i in plain_text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + shift_amount
            new_i = alphabet[new_position]
            encrypted_text += new_i
        else:
            encrypted_text += i
    print(f"The {choice}d text is {encrypted_text}\n")

should_continue = True

while should_continue:
    choice = input("Enter encode for Encryption or decode for Decrypt: ")
    options = ['decode', 'encode']
    if choice in options:
        text = input("Enter your message here: ").lower()
        shift = int(input("Enter the shift amount: "))
        shift = shift % 26
        cipher(plain_text=text, shift_amount=shift, cipher_choice=choice)
    else:
        break
    cont = input("Do you want to continue: Yes or no: ")
    if cont == 'no':
        should_continue = False
        print("Goodbye.........")
    