scoresArray=[]
value=0
for elements in array:
    if value == elements:
        continue
    else:
        scoresArray.append(elements)
        value=elements
