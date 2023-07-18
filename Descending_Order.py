#Your task is to make a function that can 
#take any non-negative integer as an argument 
#and return it with its digits in descending order.
# Essentially, rearrange the digits to 
#create the highest possible number.

num = 42145
ls = []
def descending_order(num):
    ou = 0
    while num>0:
        lft = num % 10
        num = num//10
        ls.append(lft)
    ls.sort(reverse=True)
    for i in ls:
        ou = (ou + i) *10
    return(ou//10)

descending_order(42145)
    