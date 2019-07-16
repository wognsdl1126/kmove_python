for i in range(2,10):    
    for j in range(1,10):
        print("%d * %d = %2d"%(i,j,i*j), end ="\t")
    print('')
print("\n")
for i in range(1,10):    
    for j in range(2,10):
        print("%d * %d = %2d"%(j,i,i*j), end ="\t")
    print('')