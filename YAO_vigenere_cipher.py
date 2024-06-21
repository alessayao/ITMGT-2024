def vigenere_cipher(message, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message_length = len(message)
    message_index_letter = 0 
    message_final=""
    keynumber=0
    lenkeynum =0
    while len(key) < len(message):
        key += key[lenkeynum]
        lenkeynum +=1
    

    while message_length !=0:
        message_letter= message[message_index_letter]
        shift = alphabet.index(key[keynumber])
        if shift >=26:
            shift = shift%26
        else:
            shift = shift
        if message_letter ==" ":
            newletter = str(" ")
            message_index_letter +=1
            message_length-=1
            message_final += newletter
            keynumber = keynumber +1
        else:
            newletterindex= int(alphabet.index(message_letter))
            newletter = alphabet[newletterindex + shift]
            message_index_letter +=1
            message_length-=1
            message_final +=newletter
            keynumber = keynumber +1
    return message_final

