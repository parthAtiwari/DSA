# Rotate array right by k steps (in place)
# Leetcode 189
arr=[1,2,3,4,5,6,7]
k=4
def rotate_array(arr,k):
    def helpme(i,j):
        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
    k=k%(n:=len(arr))
    helpme(0,n-1)
    helpme(0,k-1)
    helpme(k,n-1)
rotate_array(arr,k)
print(arr)
