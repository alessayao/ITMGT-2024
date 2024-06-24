def relationship_status(from_member, to_member, social_graph):
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