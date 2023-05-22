def likes(names):
    # using the 'old' % operator to fix the values from the list into the string
    if len(names)==0:
        return "no one likes this"
    elif len(names)==1:
        return '%s likes this' %(names[0])
    elif len(names)==2:
        return '%s and %s like this' %(names[0], names[1])
    elif len(names)==3:
        return '%s, %s and %s like this' %(names[0], names[1], names[2])
    elif len(names)>3:
        return '%s, %s and %i others like this' %(names[0], names[1], len(names)-2)