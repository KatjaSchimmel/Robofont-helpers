#define y-value that will be checked, check for points higher than defined y-value, mark those glyphs

font = CurrentFont()

xheight = font.info.xHeight #y-value to be checked for
overshoot = 1556
y_coordinates = []
print("x-height", xheight)
lowercase_rounds = ["o", "n", "uni037B"]
lowercase_straights = ["omegacyrillic", "idotless", "kgreenlandic"]
# print(lowercase_rounds)
# print(lowercase_straights)

for g in lowercase_rounds:
    for contour in font[g]:
        for seg in contour:
            for point in seg:
                # y_coordinates = point.y
                values = g, point.y
                y_coordinates.append(values)
print(y_coordinates)

# values = y_coordinates.split("] ")
# print(values)
    
# for value in y_coordinates:
#     print(y_coordinates[0])
#     values.extend((g, y_coordinates))
# print(values)

# print(g, max(y_coordinates))
                # print(g, point.y)

# # print and mark straight glyphs that are bigger then x-height
# for g in lowercase_straights:
#     for contour in font[g]:
#         for seg in contour:
#             for point in seg:
#                 if point.y > xheight:
#                     print(">>>>>", g, point.x, point.y)
#                     font[g]._set_markColor([1, 0, 0, 0.5])
                    
# # print and mark round glyphs that are bigger then overshoot
# for g in lowercase_rounds:
#     for contour in font[g]:
#         for seg in contour:
#             for point in seg:
#                 if point.y > xheight:
#                     print(">>>>>", g, point.x, point.y)
#                     font[g]._set_markColor([1, 0, 0, 0.5])