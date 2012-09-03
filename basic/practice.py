import sys

def intersect(*args):
    res = []
    for x in args[0]:
        for other in args[1:]:
            if x not in other: break
            else:
                res.append(x)
    return res

def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res

def print30(*args,**kargs):
    sep = kargs.get('sep',' ')
    end = kargs.get('end','\n')
    file = kargs.get('file',sys.stdout)
    output = ''
    first = True
    for arg in args:
        output += (''if first else sep) + str(arg)
        first = False
    file.write(output + end)

def print31(*args,sep=' ',end='\n',file=sys.stdout):
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)

def print32(*args,**kargs):
    sep = kargs.pop('sep',' ')
    end = kargs.pop('end','\n')
    file = kargs.pop('file',sys.stdout)
    if kargs:raise TypeError('extra keywords: %s' % kargs)
    output =  ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)

