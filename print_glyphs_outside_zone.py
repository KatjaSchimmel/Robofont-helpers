font = CurrentFont()

xHeight = font.info.xHeight #y-value to be checked for 
checkZone = 140 #most glyphs that seem to small end at around 1488 units, x-height - 1400 = 136
bluezone = 30 #the bluezone for lc is 30 units, but defined bigger in fontinfo
overshoot = font.info.xHeight + bluezone 
zoneAbove = overshoot+checkZone
zoneBelow = xHeight-checkZone
 
pointAbove = {}
pointBelow = {}

lowercase = ["b", "omegacyrillic", "idotless", "kgreenlandic","o", "n", "uni037B"]
#glyphs that should be checked

for g in lowercase: 
    for contour in font[g]:
        for cIdx, seg in enumerate(contour):
            for pIdx, point in enumerate(seg):
                if point.type != 'offcurve':
                    if point.y < xHeight and point.y >= zoneBelow:
                        if g not in pointBelow.keys():
                            pointBelow[g] = [(point.x, point.y)]
                    if point.y > overshoot and point.y <= zoneAbove:
                        if g not in pointAbove.keys():
                            pointAbove[g] = [(point.x, point.y)]
                        
print(pointBelow)
print(pointAbove)

#export list as txt file