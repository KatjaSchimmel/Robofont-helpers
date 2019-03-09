#checks the font for overlapping points by looping through all the points of a contour and checking their coordinates

font = CurrentFont()
overlappingPoints = {}
#dict of overlapping points
color = 0,0.8,1,0.4

def unpackPoint(pt):
    return glyph.name, pt.x, pt.y
    
def mark_glyph(glyph_name, color):
    font[glyph_name].markColor = color  

for glyph in font:
    for index, contour in enumerate(glyph):# index counts through the contours in the glyph
        if len(contour) == 1: # counts trhough the glyphs
            continue #if there is a contour detected go on with the script            
        prev = unpackPoint(contour[-1].onCurve) #prev is the first starting point of every contour in the glyph
        for segment in contour:
            point = unpackPoint(segment.onCurve) # point contains all the on curve points of all contours in all glyphs
            if point == prev:
                if index not in overlappingPoints:
                    overlappingPoints[index] = set() #creates a set. sets contain only unique elements
                overlappingPoints[index].add(point) #adds one of the points with the same coordinates to the dict
                mark_glyph(glyph.name, color)
            prev = point #equals the elements of prev and points

print(overlappingPoints)

