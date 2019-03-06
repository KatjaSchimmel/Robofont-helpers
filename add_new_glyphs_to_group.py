#add new glyphs to a group
#look up group for specific glyph, see if new glyphs are already in the group, if not > add new glyphs

font = CurrentFont()

base_glyph = 'f'
new_glyphs = ('longs', 'g', 'r')

for group_name, members in font.groups.items():
    #find groups that contain f
    if base_glyph in members:
        #if the group already contains the new glyphs > do nothing
        #else > add new glyphs by removing the group name, return the list of group members, add new glyphs to this list, generate a new group with the old name but updated members
        if not any(g in new_glyphs for g in members):
            old_members = font.groups.pop(group_name)
            updated_members = old_members + new_glyphs
            font.groups[group_name] = updated_members
        
