


def fascinating(n):
	    # code here
    n = str(n) + str(n*2) + str(n*3)
    k = []
    for j in n:
        k.append(int(j))
        k.sort()
    arr = [1,2,3,4,5,6,7,8,9]
    print(k)
    print(arr)
    if k == arr:
        return True
    return False

print(fascinating(853))