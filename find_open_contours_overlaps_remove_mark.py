#checks the glyphs for overlapping points, open contours and overlapping contours
#removes overlapping contours if set to "True"
remove_overlaps = False 

color = None #reset color
color_overl_contour = 0.5,0.5,1,0.2 #blau
color_overl_point = 1,0.5,1,0.4 #rosa
color_open_contour = 0.8,0.5,1,1 #lila

def is_empty(errors):
    if errors:
        return False
    else:
        return True

def mark_glyph(glyph_name, color):
    font[glyph_name].markColor = color  
    
def unpackPoint(pt):
    return glyph.name, (pt.x, pt.y)

# def is_open(glyph):
#     # based on https://stackoverflow.com/questions/16505456/how-exactly-does-the-python-any-function-work/16505590
#     # is true if any of the contours in the glyph is open
#     return any(c.open == True for c in glyph.contours)    

#checks for errors and marks them        
for font in AllFonts():
    
    overlappingContours = []
    overlappingPoints = [] #list of glyphnames with overlapping points
    openContours = []
      
    for glyph in font:
        mark_glyph(glyph.name, color)
        #checks for open contours
        # based on https://stackoverflow.com/questions/16505456/how-exactly-does-the-python-any-function-work/16505590
        # is true if any of the contours in the glyph is open
        if any(c.open == True for c in glyph.contours):
            openContours.append(glyph.name)
            mark_glyph(glyph.name, color_open_contour)      
        #checks for overlapping contours, in glyphs with closed contours
        else:
            if glyph.hasOverlap():
                overlappingContours.append(glyph.name)
                mark_glyph(glyph.name, color_overl_contour)
                if remove_overlaps == True:
                    glyph.removeOverlap() 
            #checks for overlapping points, in glyphs with closed contours     
            glyphOverlappingPoints = {} #dict of keys (key = index of contour + coordinates of overlapping points)
            for index, contour in enumerate(glyph):
                if len(contour) == 1: 
                    continue            
                prev = unpackPoint(contour[-1].onCurve)
                for segment in contour:
                    point = unpackPoint(segment.onCurve) 
                    if point == prev:
                        if index not in glyphOverlappingPoints.keys():
                            glyphOverlappingPoints[index] = set() #set contains only unique elements
                        glyphOverlappingPoints[index].add(point[1]) #adds the x and y coordinates of the point to the dict
                        # print(glyphOverlappingPoints, glyph.name)
                        mark_glyph(glyph.name, color_overl_point)
                    prev = point 
            if len(glyphOverlappingPoints.keys()) > 0:
                overlappingPoints.append(glyph.name) #adds the glyphname of the keys to the list

    if is_empty(overlappingContours):
        print('no overlapping Contours! phew!')
    else:
        print('overlapping Contours in: ', overlappingContours)        

    if is_empty(overlappingPoints):
        print('no overlapping Points! whoop whoop!')
    else:
        print('overlapping Points in: ', overlappingPoints)
    
    if is_empty(openContours):
        print('no open Contours! yeeei!')
    else:
        print('open Contours in: ', openContours)

