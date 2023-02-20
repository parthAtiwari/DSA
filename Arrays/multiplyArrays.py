# Write a program that takes two arrays representing integers, and retums an integer representing their product. For example, since 193707721.x -761838257287 = -147573952589676412927
# if the inputs are [1,9,3,7,0,7,7,2, 1] and [-7,6,1,8,3,8,2,5,7,2,8,7] your function should return
# [-1, 4,7, 5,7,3, 9, 5, 2, 5,8,9, 6,7, 6, 4, 1., 2,9,2,7].
def multiply(arr1,arr2):
    sign=-1 if ((arr1[0]<0)^(arr2[0]<0)) else 1
    arr1[0],arr2[0]=abs(arr1[0]),abs(arr2[0])
    res=[0]*(len(arr1)+len(arr2))
    for i in reversed(range(len(arr1))):
        for j in reversed(range(len(arr2))):
            res[i+j+1]+=arr1[i]*arr2[j]
            res[i+j]+=res[i+j+1]//10
            res[i+j+1]%=10
    ix=0
    while res[ix]==0:
        ix+=1
    res[ix]*=sign
  
    return res[ix:]

#driver code
arr1=[1,2,3,4,5,6,8,7,9,9,3,9,9]
arr2=[2,3,3,4,9,9,9,9]
res=multiply(arr1,arr2)
print(res)






