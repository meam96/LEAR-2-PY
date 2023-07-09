l=[1, 2, 'b', 'v',"k"]
def filter_list(l):
    for i in l:
        print(i)
        c = type(i)
        if c==int:
            l.remove(i) 
    print(l)

filter_list(l)
        