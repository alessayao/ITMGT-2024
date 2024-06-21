def scytale_cipher(message, shift):
    newindexlist= [""]
    nili=0
    final_message =""
    while len(message) %shift !=0 :
        message += "_"
    for i in range (0,len(message)):
        newindex = ((i // shift) + (len(message) // shift) * (i % shift))
        newindexlist.append(newindex)
    newindexlist.remove("")
    
    while (nili)!= len(message):
        newnumber = int(newindexlist[nili])
        newletteri= message[newnumber]
        nili +=1
        final_message +=newletteri
    return final_message 