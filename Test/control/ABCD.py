el = 'AB-CD=EF EF+GH=PPP'
ns = '123456789'

el = el.replace('=','==').replace(' ', ' and ')
vs = list(set([s for s in el if s>='A' and s<='Z']))

ns = [s for s in ns]

def fs(el, vs, ns):
    if not vs:
        if eval(el):
            print el.replace('and ', '').replace('==', '=')
    else:
        v = vs[0]
        ix = len(ns)
        while ix:
            ix -= 1
            nel = el.replace(v, ns[ix])
            print ns[ix+1:]
            fs(nel, vs[1:], ns[0:ix]+ns[ix+1:])

import time
st = time.time()
fs(el,vs,ns)
print 'time:%dms'%((time.time()-st)*1000)
