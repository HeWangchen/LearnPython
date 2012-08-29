def Towers(size ,fromStack,toStack,spareStack):
    if size == 1:
        print( 'Move tower from ',fromStack,' to ' ,toStack)
    else:
        Towers(size - 1,fromStack,spareStack,toStack )
        Towers(1,fromStack,toStack,spareStack)
        Towers(size - 1,spareStack,toStack,fromStack)

Towers(5,'A','B','C')

