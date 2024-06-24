def eta(first_stop, second_stop, route_map):
    

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