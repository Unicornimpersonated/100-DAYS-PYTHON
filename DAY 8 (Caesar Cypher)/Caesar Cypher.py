alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Enter shift number: \n"))


#TODO-3: 1. Combine the encrypt() and decrypt() functions into a single functions called caesar()
        #2. USe the value of the user chosen direction variable to determine which functionality to use.
        #3. Use the caesar functionality instead of encrypt/decrypt and pass in all 3 variables direction/text/shift

def caesar(original_text,shift_amount,encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
          
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount # 9 -> 7
        shifted_position %= len(alphabet)
        #shifted_position = shifted_position % len(alphabet)
        output_text +=  alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)