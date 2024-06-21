def caesar_cipher(message, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message_length = len(message)
    message_index_letter = 0 
    message_final=""
    if shift >=26:
        shift = shift%26
    else:
        shift = shift
    while message_length !=0:
        message_letter= message[message_index_letter]
        if message_letter ==" ":
            newletter = str(" ")
            message_index_letter +=1
            message_length-=1
            message_final += newletter
        else:
            newletterindex= int(alphabet.index(message_letter))
            newletter = alphabet[newletterindex + shift]
            message_index_letter +=1
            message_length-=1
            message_final +=newletter
    return message_final
