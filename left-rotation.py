def rotateLeft(a, d,n):
    
    length = len(a)     
    newArray = [0 for x in a] # Initialize 0 in an array of size 5.
    for i in range(n):
        newElement = i-d          
        newArray[newElement]=str(a[i]) 
    result = " ".join(newArray)
    return result


def main():
    
    arr = [1,2,3,4,5]
    d = 4
    n = 5
    result = rotateLeft(arr, d,n)
    print(result)


if __name__ == "__main__":
    main()