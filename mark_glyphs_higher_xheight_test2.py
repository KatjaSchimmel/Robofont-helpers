#define y-value that will be checked, check for points higher than defined y-value, mark those glyphs

font = CurrentFont()

xheight = font.info.xHeight #y-value to be checked for
overshoot = 1556
print("xheight:", xheight, "/ overshoot:", overshoot)

lowercase_rounds = ['o', 'n', 'uni037B']
list_of_values = []
y_coordinates = []



# print points that are over capHeight and mark glyph if true
for g in lowercase_rounds:
    for contour in font[g]:
        for seg in contour:
            for point in seg:
                # print(g, point.y)
                y_coordinates.append((g, point.y))
                y_coordinates.sort()
print(y_coordinates)
                
            #     for highest_point in point:
            #         print(highest_point)
                    
                # if point.y in range(xheight, overshoot):
                #     print(">>>>>", g, point.x, point.y)
                # if point.y > overshoot:
                #     print(">>>>>", g, point.x, point.y)
                #     font[g]._set_markColor([1, 0, 0, 0.5])
                
                
                # if point.y < overshoot:
                #     print(">>>>>", g, point.x, point.y)
                #     font[g]._set_markColor([1, 0, 0, 0.5])