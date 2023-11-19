def interfaceworkerdict(days_colors):
    count_colors = {}
    color_percentages = {}
    percentage_string = ""
    for day in days_colors:
        if days_colors[day] not in count_colors:
            count_colors[days_colors[day]] = 1 
        else:
            count_colors[days_colors[day]] += 1
    for color in count_colors:
        color_percentages[color] = count_colors[color]/len(days_colors) * 100
                                                
    for color in color_percentages:
        percentage_string += (color + ": " + str(color_percentages[color]) + '% ,')
    return percentage_string
    
def interfaceworkerlist(days_colors):
    count_colors = {}
    color_percentages = {}
    percentage_string = ""
    for color in days_colors:
        if color not in count_colors:
            count_colors[color] = 1 
        else:
            count_colors[color] += 1
    for color in count_colors:
        color_percentages[color] = count_colors[color]/len(days_colors) * 100
                                                
    for color in color_percentages:
        percentage_string += (color + ": " + str(color_percentages[color]) + '% ,')
    return percentage_string
    
    

    
