def add(x,y):
    return x + y
def sub(x,y):
    return x - y

x,y = map(int,input("Enter the values of x and y : ").split())
print("sum of x and y",add(x,y))
print("diff of x and y",sub(x,y))
