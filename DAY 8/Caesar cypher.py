alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Enter shift number: \n"))

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function,shift each letter of the 'original_text' forwards in the alphabet by the
#  'shift_amount' and print the encrypted text.

# hello 2
def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount # 7 -> 9
        shifted_position %= len(alphabet)
        #shifted_position = shifted_position % len(alphabet)
        cipher_text += alphabet[shifted_position]

    print(f"Here is the encoded result: {cipher_text}")

# TODO-4: What happens when you try to shift z forwards by 9?Can you fix code?
# solution: use modulo to get the remainder, take shifted_position % 26

# TODO-3: Call the 'encrypt()' function and pass in the user inputs.You should be
encrypt(original_text=text,shift_amount= shift)

# riqumuijmjm