def product( x , y ): 
    if x < y: 
        return product(y, x) 
    elif y != 0: 
        return (x + product(x, y - 1)) 
    else: 
        return 0

x = 51
y = 20
print(product(x, y)) 