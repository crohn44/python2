title = "TYPE ME IN AN X PATTERN COOL CODE WOW VERY AWESOME"
spacing = ""
inversespacing = (len(title) - 1) * " "
spacingcounter = 0
counter = 0

while counter < len(title):
    if counter < (len(title))/2:
        print(spacing + title[counter] + inversespacing + title[counter])
        spacingcounter += 1
        inversespacing = (len(inversespacing) - 2) * " "
    elif (len(title))/2 < counter:
        print(spacing + title[counter] + inversespacing + title[counter])
        spacingcounter += -1
        inversespacing = (len(inversespacing) + 2) * " "
    else:
        print(spacing + title[counter])
        spacingcounter += -1
        inversespacing = (len(inversespacing) + 1) * " "
        
    
    spacing = spacingcounter * " "
    counter += 1
    
    