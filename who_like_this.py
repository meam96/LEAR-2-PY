def likes(names):
    # your code here

    x = "no one likes this" 
    l = len(names)
    if l==0:
            return(x)
    elif l==1:
        for i in names:
            print(i,"likes this")
    elif l>1 and l<=2:
        print(names[0],"and",names[2],"like this")
    elif l>2:
        print(names[0],"and",names[2],"and",l-2,"others","like this")
            
        
        
likes(['peter','jhon','milad'])