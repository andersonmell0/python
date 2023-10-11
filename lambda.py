# Expressões Lambda

f = lambda x,y:x*y
print(f(2,3))

g = lambda x,y=3: x*y
print(g(4))

h = lambda x,y,w: x*y*w
print(h(w=3,y=3,x=3))