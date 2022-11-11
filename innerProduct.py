def innerProd(a, b):
    innerProductSum = 0
    if (len(a) == len(b)):
        for i in range(len(a)):
            innerProductSum += a[i] * b[i]
        return innerProductSum
    return -1
list_a = [1,2,3]
list_b = [2.1,3.4,5]
print (innerProd(list_a,list_b))