# Convert HTML to Luna:
# Ex: 
# HTML: '<div></div><div><p><img /></p><b></b></div>'  <<<--- note the space in <img />
# Luna: 'DIV([])DIV([P([IMG({})]), B([])])'


def htmlToLuna(html):
    output = ""
    x = 1
    stack = 0
    while x < len(html):
        if html[x] == '/':
            if output[-2:] == ', ':
                output = output[:-2]
            output += '])'
            stack -= 1
            if stack == 1:
                output += ', '
            x += 2
        elif html[x] == 'd':
            output += 'DIV(['
            stack += 1
            x += 5
        elif html[x] == 'p':
            output += 'P(['
            stack += 1
            x += 3
        elif html[x] == 'b':
            output += 'B(['
            stack += 1
            x += 3
        elif html[x] == 'm':
            output += 'IMG({})'
            x += 6
        else:
            x += 1
    return output

print htmlToLuna('<div></div><div><p><img /></p><b></b></div>')