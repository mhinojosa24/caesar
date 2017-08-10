def alphabet_position(letter):
    if letter.isupper(): 
        letter = (ord(letter)-65) 
        return letter
        
    else: 
        letter = (ord(letter)-97) 
        return letter           
    return letter

def rotate_character(char, rot):
    if char.isalpha() == False:
        return char
    orig_pos = alphabet_position(char)
    
    if (orig_pos + rot) > 26: rotation = (orig_pos + rot) % 26
    else: rotation = (orig_pos + rot)% 26
        
    if char.isupper() == True: return chr(rotation + 65)
    else: return  chr(rotation + 97)

def encrypt(text, rot):
    new_text = ''
    for chr in text:
        new_text += rotate_character(chr, rot) 
    return new_text

def main():
    message = input("Enter a message: ")
    rot_num = int(input("Enter number"))
    print(encrypt(message, rot_num))
    
if __name__ == "__main__":
    main()




      