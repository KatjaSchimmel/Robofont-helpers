# Marks composites, components, mixed and transformed components 

# Works in Robofont Version 1 and 3
# RF version check
from mojo.roboFont import version
three = None
if version.startswith('3'):
    three = True
else:
    three = False

#predefined mark colors
color = None #Reset color in the beginning
mixed_color = (1,1,0,0.4)
comp_color = (1,0,1,0.4)
ref_color = (0,1,1,0.4)
transformed_color = (1,0,0,0.4) #scaled, mirrored, transformed components
empty_color = (0,0,1,0.8)
     
def paint_mark(glyph, color):
    if three:
        glyph.markColor = color
    else:
        glyph.mark = color

def paint(current_glyph_name, font):
    paint_mark(glyph, comp_color)
    for comp in font[current_glyph_name].components:
        if comp.baseGlyph not in font:
            paint_mark(font[current_glyph_name], empty_color)
            print(comp.glyph.name,': component', comp.baseGlyph,  'is empty') 
        else:
            paint_mark(font[comp.baseGlyph], ref_color)

def transformed(current_glyph_name, font):
     if comp.transformation[0] == 1.0 and comp.transformation[3] == 1.0:
         pass
     else:
        print(comp.glyph.name,': component', comp.baseGlyph,  'is mirrored or scaled')
        paint_mark(glyph, transformed_color)
        #more than one transformed component in glyph > show it in one entry

for font in AllFonts():
    for glyph in font:
        paint_mark(glyph, color)
        if glyph.components and glyph.contours:
            paint_mark(glyph, mixed_color)
        elif glyph.components and len(glyph.contours) == 0:
            paint(glyph.name, font)
            for comp in glyph.components:
                transformed(glyph.name, font)