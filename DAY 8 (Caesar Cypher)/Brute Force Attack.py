alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input("Type your message: \n").lower()

def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount # 7 -> 9
        shifted_position %= len(alphabet)
        #shifted_position = shifted_position % len(alphabet)
        cipher_text += alphabet[shifted_position]
        
    return cipher_text

for i in range(27):
    print(f"Brute Force Output={encrypt(text, i)}")
