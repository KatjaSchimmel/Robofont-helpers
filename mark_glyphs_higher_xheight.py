#define y-value that will be checked, check for points higher than defined y-value, mark those glyphs

font = CurrentFont()

xheight = font.info.xHeight #y-value to be checked for
overshoot = 1556
y_coordinates = []
values = []
print("x-height", xheight)
print("overshoot", overshoot)
lowercase_rounds = ["o", "n", "uni037B"]
lowercase_straights = ["omegacyrillic", "idotless", "kgreenlandic"]
# print(lowercase_rounds)
# print(lowercase_straights)

for g in lowercase_rounds:
    for contour in font[g]:
        for seg in contour:
            for point in seg:            
                values.append((g,point.y)) #all y coordinates

values.sort()
singlevalues = list(dict.fromkeys(values))
print(singlevalues)


#find highest point in glyph
# print and mark glyphs higher or lower then x-height/overshoot

            # y_coordinates.append(values) # should be only the max values

# for value in y_coordinates:
#     # print(value[1])
#     if value[1] > overshoot:
#         print(value[0], value[1])
# # now we just need to check the max values instead all of them



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