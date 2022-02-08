from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#testing the functionality of the index method
# index = alphabet.index('d')
# print(index)

def caesar(text, shift,direction):
    text_list = list(text)
    i = 0
    for char in text_list:
        if char in alphabet:
            index = alphabet.index(char)
            if direction == 'encode':
                shifted_index = index + shift
            elif direction == 'decode':
                shifted_index = index - shift
                
            if shifted_index > 25 and direction == 'encode':
                index = shifted_index - 26
                text_list[i] = alphabet[index]
            elif shifted_index < 0 and direction == 'decode':
                index = shifted_index + 26
                text_list[i] = alphabet[index]
            else:
                text_list[i] = alphabet[shifted_index]
            i += 1
        else:
            text_list[i] = char
            i +=1
    text_list = ''.join(text_list)      
    print(f"Here's the {direction}d result: {text_list}")

caesar(text=text, shift=shift, direction=direction)
