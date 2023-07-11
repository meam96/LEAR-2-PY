l=[1, 2, 'b', 'v',"k","j"]
def filter_list(l):
    new_list=[]
    for i in l:
        c = type(i)
        if c==int:
            new_list.append(i)
        else:
            continue 
    print(new_list)

filter_list(l)
        