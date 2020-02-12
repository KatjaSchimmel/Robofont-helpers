font = CurrentFont()

xheight = font.info.xHeight #y-value to be checked for
overshoot = 1556
y_coordinates = []

lowercase_rounds = {"o"}

for g in lowercase_rounds:
    for contour in font[g]:
        for seg in contour:
            for point in seg:
                y_coordinates.append((g))
                y_coordinates.append((point.y))
# print(y_coordinates)
# y_coordinates.sort()
print(y_coordinates)

def Convert(y_coordinates): 
    res_dct = {y_coordinates[i]: y_coordinates[i + 1] for i in range(0, len(y_coordinates), 2)} 
    return res_dct 
          
# Driver code 
print(Convert(y_coordinates)) 

# y_coordinates.sort()

# print(y_coordinates)