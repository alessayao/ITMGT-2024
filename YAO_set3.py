'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    relationship_status = ""
    if from_member in social_graph[to_member]["following"] : 
        if to_member in social_graph[from_member]["following"]:
            relationship_status ="friends"
        else:
            relationship_status ="followed by"
    else:
        if to_member in social_graph[from_member]["following"]:
            relationship_status = "follower"
        else:
            relationship_status = "no relationship"

    return relationship_status


def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    vertical = []
    vertical_winner = ""
    horizontal_winner =""
    diagonal = []
    backdiagonal= []
    diagonal_winner = ""
    final_winner =""

    #arrangement
    
    #vertical string
    for i in range (0,len(board)):
        for j in range (0, len(board)):
            if board[i][j] =='':
                vertical += "E"
            else:
                vertical += board[i][j]
    
    #diagonal string
    for m in range (0, len(board)):
        for n in range (0, len(board)):
            if m == n:
                diagonal_letter = board[m][n]
                diagonal += diagonal_letter
    for w in range (0,len(board)):
        for q in range ((-(len(board))),0):
            if w == (-(q+1)):
                diagonal_letter_back = board[w][q]
                backdiagonal += diagonal_letter_back
    
    # Start of the winner finding
    
    #vertical winner
    for k in range (0,len(board)):
        if vertical[k::len(board)].count('X') == len(board):
            vertical_winner += "X"
        elif vertical[k::len(board)].count('O') ==len(board):
            vertical_winner += "O"
        else:
            vertical_winner +=""
    
    #horizontal winner
    for l in range (0,len(board)):
        if board[l].count('X')==len(board):
            horizontal_winner += "X"
        elif board[l].count('O')==len(board):
            horizontal_winner += "O"
        else:
            horizontal_winner +=""

    #diagonal winner
    if diagonal.count('X')== len(board):
        diagonal_winner = "X"
    elif diagonal.count('O') == len(board):
        diagonal_winner = "O"
    else: 
        if backdiagonal.count('X')== len(board):
            diagonal_winner = "X"
        elif backdiagonal.count('O') == len(board):
            diagonal_winner = "O"
        else:
            diagonal_winner = ""

    if vertical_winner == "X":
        final_winner += "X"
    elif vertical_winner == "O":
        final_winner += "O"
    elif horizontal_winner =="X":
        final_winner += "X"
    elif horizontal_winner =="O":
        final_winner+="O"
    elif diagonal_winner =="X":
        final_winner+= "X"
    elif diagonal_winner == "O":
        final_winner+= "O"
    else: 
        final_winner = "NO WINNER"

    return final_winner

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    location_lists = list(route_map.keys())
    start_place =0
    end_place =0
    minutes =0
    
    list_values = list(route_map.values())
    
    
    for i in range (0,len(location_lists)):
        if location_lists[i][0] == first_stop:
            start_place +=i 
        else:
            start_place +=0
    for j in range (0,len(location_lists)):
        if location_lists[j][1] == second_stop:
            end_place +=j
        else:
            end_place +=0 
    if start_place <= end_place:
        for k in range (start_place,end_place+1):
            stop_min = list_values[k]['travel_time_mins']
            minutes += stop_min
    else: 
        for l in range (0,end_place+1):
            stop_min = list_values[l]['travel_time_mins']
            minutes += stop_min
        for p in range (start_place,len(location_lists)):
            stop_min = list_values[p]['travel_time_mins']
            minutes += stop_min

    return minutes