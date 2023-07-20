#write a nested for to show a multiplication table
#1 2 3
#2 4 6
#3 6 9

def multiplication_table(start,stop):
    for x in range(1,4):
        for y in range(1,4):
            print(str(x*y), end=" ")
    
        print()
multiplication_table(1,3)