# select two points on a stem
# check direction of the contour (horizontal or vertical)
# draw a horizontal or vertical guideline in the middle between those points

font = CurrentFont()
glyph = CurrentGlyph()
points_selected = []

#find coordinates of selected points and add them to list
for contour in glyph:
    for seg in contour:
        for point in seg:
            if point.selected:
                points_selected.append((point.x, point.y))
                    
if len(points_selected) == 0:
    print('!!! no points selected !!!')
elif len(points_selected) == 1:
    print('!!! select one more point !!!')
elif len(points_selected) >= 3:
    print('!!! too many points selected !!!')
    
elif len(points_selected) == 2:
    
    def middle(distance):
        return distance / 2
        
    def starting_point(coordinate): 
        if p1[coordinate] > p2[coordinate]:
            sp = p2[coordinate]
        elif p2[coordinate] > p1[coordinate]:
            sp = p1[coordinate]
        else: # points are at the same x value
            sp = p2[coordinate]
        return sp
        
    def guide_position(p, middle):
        return p + middle #adding x or y value of middle to the first point
        
    #assigning coordinates to points
    p1 = points_selected[0]
    p2 = points_selected[1]
        
    #defining the distance and middle between points
    distance_x = abs(p2[0]-p1[0])
    distance_y = abs(p2[1]-p1[1])
    middle_x = middle(distance_x)
    middle_y = middle(distance_y)
    
    #x and y will be used as 'coordinate' and be placed in []
    x = 0 # x = 0 because the x-value is the first value of p1 and p2
    y = 1 # x = 1 because the y-value is the second value of p1 and p2
    p_x = starting_point(x)
    p_y = starting_point(y)
    
    guide_x = guide_position(p_x, middle_x)
    guide_y = guide_position(p_y, middle_y)
    
    # check area around points (north, east, south, west) to decide contour direction
    p1n = (p1[0], p1[1]+1)
    p1e = (p1[0] +1, p1[1])
    p1s = (p1[0], p1[1]-1)
    p1w = (p1[0] -1, p1[1])   

    p2n = (p2[0], p2[1]+1)
    p2e = (p2[0] +1, p2[1])
    p2s = (p2[0], p2[1]-1)
    p2w = (p2[0] -1, p2[1])
    
    v_guidelines = [] #vertical guidelines
    h_guidelines = [] #horizontal guidelines
    
    #adding all existing guidelines to a list
    for guidelines in glyph:
        guidelines = list(glyph.guidelines)
        for guideline in guidelines:
            # split x and y coordinates of the guidelines and add them to the list of horizontal or vertical guidelines
            v_guidelines.append(guideline.x)
            h_guidelines.append(guideline.y)
    
    # draw a horizontal or vertical guideline depending on which points are inside and outside the contour of the glyph
    if any (guide_x in v_guidelines for guideline in guidelines): #check list of vertical guidelines if there is already a guideline at this position
        print('gibtsscho')
    elif glyph.pointInside((p1w)) == True and glyph.pointInside((p1e)) == False and glyph.pointInside((p2e)) == True and glyph.pointInside((p2w)) == False: 
        print(glyph.name, ', ', 'p1', p1,', p2', p2, ', vertical stem, ', 'width:', distance_x,', middle guide at x', guide_x)
        glyph.appendGuideline((guide_x,-100), 90)    
    elif glyph.pointInside((p1e)) == True and glyph.pointInside((p1w)) == False and glyph.pointInside((p2w)) == True and glyph.pointInside((p2e)) == False: 
        print(glyph.name, ', ', 'p1', p1,', p2', p2,', vertical stem, ', 'width:', distance_x,', middle guide at x', guide_x)
        glyph.appendGuideline((guide_x,-100), 90)
    
    if any (guide_y in h_guidelines for guideline in guidelines): #check list of horizontal guidelines if there is already a guideline at this position
        print('gibtsscho')
    elif glyph.pointInside((p1n)) == True and glyph.pointInside((p1s)) == False and glyph.pointInside((p2s)) == True and glyph.pointInside((p2n)) == False: 
        print(glyph.name, ', ', 'p1', p1,', p2', p2, ', horizontal stem, ', 'width:', distance_y,', middle guide at y', guide_y)
        glyph.appendGuideline((-100, guide_y), 0) 
    elif glyph.pointInside((p1s)) == True and glyph.pointInside((p1n)) == False and glyph.pointInside((p2n)) == True and glyph.pointInside((p2s)) == False: 
        print(glyph.name, ', ', 'p1', p1,', p2', p2, ', horizontal stem, ', 'width:', distance_y,', middle guide at y', guide_y)
        glyph.appendGuideline((-100, guide_y), 0)

