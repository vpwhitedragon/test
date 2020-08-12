
def josephus(ls,skip):
    skip -= 1
    dx=skip
    while(len(ls) > 1):
        ls.pop(dx)
        #print(dx)
        dx=(dx+skip)%len(ls)
    print('Last one',ls)

a=list(range(1,10))

josephus(list(range(1,101)),2)

