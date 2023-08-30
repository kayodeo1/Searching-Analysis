import time
import random
import matplotlib.pyplot as plt
#implementing linear search
def linearSearch(arr,key):
    for i in range (0,len(arr),1):
        if arr[i]==key:
            return(i+1)
    return(0)
#implementing binary search recursively
def binaryRecursive(arr,start,finish,key):
    while start<finish:
        mid=int((start+finish)/2)
        if key==arr[mid]:
            return(mid+1)
        elif key<arr[mid]:
            return(binaryRecursive(arr,0,mid-1,key))
        else:
            return(binaryRecursive(arr,mid+1,finish,key))

#implementing bunary search non recursively        
def binaryNonRecursive(arr,key):
    lower=0
    upper=len(arr)-1
    while lower<upper:
        mid=int((upper+lower)/2)
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            upper=mid-1
        elif arr[mid]<key:
            lower=mid+1
    if upper==lower and arr[upper]==key:
        return(upper)
    else:
        return -1

'''
initialising the array size
a list for the sizes of data to be manipulated
and lists to accumulate the time taken for finding 70 in the sorted and unsorted array

'''
array=[]
arrSizes=[50000,100000,250000,500000,750000]
linearTime=[]
binaryRecursiveTime=[]
binaryNonRecursiveTime=[]
for i in range (5):
    for j in range(arrSizes[i]):
        array.append(random.randint(1,100))
    for k in range (2):
        before=time.time()
        index=linearSearch(array,70)
        after=time.time()
        timeTaken=after-before
        linearTime.append(timeTaken)
        print(70,"was found at position",index,"in",timeTaken,"seconds")
        
        before=time.time()
        index=binaryRecursive(array,0,(len(array)-1),70)
        after=time.time()
        timeTaken=after-before
        binaryRecursiveTime.append(timeTaken)
        print(70,"was found at position",index,"in",timeTaken,"seconds")
        
        before=time.time()
        array.sort()
        index=binaryNonRecursive(array,70)
        after=time.time()
        timeTaken=after-before
        binaryNonRecursiveTime.append(timeTaken)
        print(70,"was found at position",index,"in",timeTaken,"seconds")
        array.sort()
    array=[]
     
linearUnsortedTime=[]
binaryRecursiveUnsortedTime=[]
binaryNonRecursiveUnsortedTime=[]
linearSortedTime=[]
binaryRecursiveSortedTime=[]
binaryNonRecursiveSortedTime=[]

for i in range (0,10,2):
    linearUnsortedTime.append(linearTime[i])
print(linearUnsortedTime)

for i in range (1,10,2):
    linearSortedTime.append(linearTime[i])
print(linearSortedTime)

for i in range (0,10,2):
    binaryRecursiveUnsortedTime.append(binaryRecursiveTime[i])
print(binaryRecursiveUnsortedTime)

for i in range (1,10,2):
    binaryRecursiveSortedTime.append(binaryRecursiveTime[i])
print(binaryRecursiveSortedTime)
    
for i in range (0,10,2):
    binaryNonRecursiveUnsortedTime.append(binaryNonRecursiveTime[i])
print(binaryNonRecursiveUnsortedTime)

for i in range (1,10,2):
    binaryNonRecursiveSortedTime.append(binaryNonRecursiveTime[i])
print(binaryNonRecursiveSortedTime)
    
plt.plot(arrSizes,linearUnsortedTime,label="Linear search Unsorted List",color="blue")
plt.plot(arrSizes,binaryRecursiveUnsortedTime,label="Binary Recursive Seacrh Unsorted list",color="yellow")
plt.plot(arrSizes,binaryNonRecursiveUnsortedTime,label="Binary Non Recursive Seacrh Unsorted list",color="red")
plt.show()
plt.plot(arrSizes,linearSortedTime,label="Linear search Sorted List",color="blue")
plt.plot(arrSizes,binaryRecursiveSortedTime,label="Binary Recursive Seacrh Sorted List",color="yellow")
plt.plot(arrSizes,binaryNonRecursiveSortedTime,label="Binary Non Recursive Seacrh Sorted List",color="red")
plt.show()
