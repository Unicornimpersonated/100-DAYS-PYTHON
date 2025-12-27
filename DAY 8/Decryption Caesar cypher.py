alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Enter shift number: \n"))

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function,shift each letter of the 'original_text' forwards in the alphabet by the
#  'shift_amount' and print the encrypted text.

# hello 2

def encrypt(original_text, shift_amount):   
    cipher_text=""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount # 7 -> 9
        shifted_position %= len(alphabet)
        #shifted_position = shifted_position % len(alphabet)
        cipher_text += alphabet[shifted_position]

    return cipher_text

result = encrypt(text, shift) 

print(f"Here is the encoded result: {result}")


# TODO-4: What happens when you try to shift z forwards by 9?Can you fix code?
# solution: use modulo to get the remainder, take shifted_position % 26

# TODO-3: Call the 'encrypt()' function and pass in the user inputs.You should be



#TODO-1:Create a function called decrypt()  that takes original text  and shift amount as 2 inputs

#TODO-2: Inside the decrypt() function, shift each letter of the original text towards in the alphabets 
        # backwards by the shift_amount and print decrypted_text
 
def decrypt(cipher_text, shift_amount): # variable cipher_text in encrypt() and decrypt() are different
    original_text = ""
    for letter in cipher_text:
        shifted_position = alphabet.index(letter) - shift_amount # 9 -> 7
        shifted_position %= len(alphabet)
        #shifted_position = shifted_position % len(alphabet)
        original_text +=  alphabet[shifted_position]

    return original_text

print(f"Here is the decrypted result:{decrypt(result, shift_amount= shift)}")


#TODO-3: 1. Combine the encrypt() and decrypt() functions into a single functions called caesar()
        #2. USe the value of the user chosen direction variable to determine which functionality to use.
        #3. Use the caesar functionality instead of encrypt/decrypt and pass in all 3 variables direction/text/shift

def caesar(original_text,shift_amount,encode_or_decode):
    original_text = ""
    for letter in cipher_text:
        if encode_or_decode == "decode":
            shift_amount *= -1

        shifted_position = alphabet.index(letter) +  shift_amount # 9 -> 7
        shifted_position %= len(alphabet)
        #shifted_position = shifted_position % len(alphabet)
        original_text +=  alphabet[shifted_position]
