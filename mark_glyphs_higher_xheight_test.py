font = CurrentFont()

xheight = font.info.xHeight #y-value to be checked for
overshoot = 1556
y_coordinates = []
glyphs = []
lowercase_rounds = {"o", "n"}

for g in lowercase_rounds:
    for contour in font[g]:
        for seg in contour:
            for point in seg:
                glyphs.append((g))
                # find max y value
                y_coordinates.append((str(point.y))) #needs to be in quotes
print(y_coordinates)
print(glyphs)

res = dict(zip(glyphs, y_coordinates)) 
print(res)

# y_coordinates.sort()

# print(y_coordinates)