#mark caps with points higher than overshoot
#define y-value that will be checked, check for points higher than defined y-value, mark those glyphs

font = CurrentFont()

print(font.selection)

capHeight = font.info.capHeight
print(capHeight)
blueValues = font.info.postscriptBlueValues
print(blueValues)
#blue zone for cap Height-overshoot is most likely last value
overshoot_capHeight = blueValues[-1]
print(overshoot_capHeight)

# print points that are over capHeight and mark glyph if true
for g in font.selection:
    print(type(g))
    print(type(font.selection))
    for contour in font[g]:
        #font[g] is this glyph in this font
        for seg in contour:
            for point in seg:
                if point.y > overshoot_capHeight:
                    print(">>>>>", g, point.x, point.y)
                    font[g]._set_markColor([1, 0, 0, 0.5])