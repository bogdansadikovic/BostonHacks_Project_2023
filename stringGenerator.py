import math

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
        color_percentages[color] = int(count_colors[color] / len(days_colors) * 100)

    for color in color_percentages:
        percentage_string += (color + ": " + str(color_percentages[color]) + '% ,')

    #converts all instances of colors to their hex counterpart for ease of DALLE
    percentage_string = percentage_string.replace('RED','#F7251C')
    percentage_string = percentage_string.replace('GREEN', '#227F19')
    percentage_string = percentage_string.replace('BLUE', ' #000EF9')
    percentage_string = percentage_string.replace('VIOLET', '#E886EB')
    percentage_string = percentage_string.replace('ORANGE', '#FBA72F')
    percentage_string = percentage_string.replace('GREY', '#808080')

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
        color_percentages[color] = count_colors[color] / len(days_colors) * 100

    for color in color_percentages:
        percentage_string += (color + ": " + str(color_percentages[color]) + '% ,')

    #converts all instances of colors to their hex counterpart for ease of DALLE
    percentage_string = percentage_string.replace('RED','#F7251C')
    percentage_string = percentage_string.replace('GREEN', '#227F19')
    percentage_string = percentage_string.replace('BLUE', ' #000EF9')
    percentage_string = percentage_string.replace('VIOLET', '#E886EB')
    percentage_string = percentage_string.replace('ORANGE', '#FBA72F')
    percentage_string = percentage_string.replace('GREY', '#808080')
    
    return percentage_string
