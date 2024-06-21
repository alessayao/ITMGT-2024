def shift_letter(letter, shift):
    mylist = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    if letter == " ":
        final = str(" ")
    else:
        placement = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"].index(letter)
        if shift>=26:
            remainder = shift%26
            final = mylist[placement + remainder]
        else:
            final = mylist[placement+shift]

    return final

print(shift_letter("H",90))