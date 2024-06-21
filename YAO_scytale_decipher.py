def scytale_decipher(message, shift):
    newindexlist=[""]
    newindexlist.remove("")
    nilo=0
    finalindexlist =[""]
    finalindexlist.remove("")
    final_messageo=""
    for i in range (0,len(message)):
        if i==0:
            newletterindexd = 0
            newindexlist.append(newletterindexd)
        else: 
            newletterindexd= i
            newindexlist.append(newletterindexd)
    for num in range (0, shift):
        finalindexlist+=newindexlist[num::(shift)]
    while (nilo)!= len(message):
        newnumber = int(finalindexlist[nilo])
        newletteri= message[newnumber]
        nilo +=1
        final_messageo+=newletteri
    return final_messageo