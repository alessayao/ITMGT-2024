def shift_by_letter(letter, letter_shift):
    lmylist = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lshift = lmylist.index(letter_shift)
    if letter == " ":
        final = str(" ")
    else:
        placement = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"].index(letter)
        if lshift>=26:
            remainder = lshift%26
            final = lmylist[placement + remainder]
        else:
            final = lmylist[placement+lshift]

    return final

