#define y-value that will be checked, check for points higher than defined y-value, mark those glyphs

font = CurrentFont()

capHeight = font.info.capHeight #y-value to be checked for
print("Cap Height", capHeight)
blueValues = font.info.postscriptBlueValues
print("Blue Values", blueValues)
#blue zone for cap Height-overshoot is most likely last value
overshoot_capHeight = blueValues[-1]
print("Overshoot", overshoot_capHeight)

# print points that are over capHeight and mark glyph if true
for g in font.selection:
    for contour in font[g]:
        for seg in contour:
            for point in seg:
                if point.y > overshoot_capHeight:
                    print(">>>>>", g, point.x, point.y)
                    font[g]._set_markColor([1, 0, 0, 0.5])