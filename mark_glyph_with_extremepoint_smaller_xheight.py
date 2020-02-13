font = CurrentFont()

xheight = font.info.xHeight #y-value to be checked for
print("xheight:", xheight)

lowercase = ["kgreenlandic"]
y_coordinates = []

for g in lowercase:
    for contour in font[g]:
        for seg in contour:
            for point in seg:
                #oncurve points in glyph
                if point.type == 'line':
                    # print(point.y)
                    y_coordinates.append((point.y))
                if point.type == 'curve':
                    # print(point.y)
                    y_coordinates.append((point.y))
y_coordinates.sort()
max_y = max(y_coordinates)
if max_y < xheight:
    print('ohno, glyph is smaller then x-height')
    print(">>>>>", g, point.x, point.y)
    font[g]._set_markColor([1, 0, 0, 0.5])