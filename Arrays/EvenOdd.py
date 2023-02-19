#Your input is an array of integers, and you have to reorder its entries so that the even entries appear first. This is easy if you use O(n) space, where n is the length of the array.Howevever, you are required to solve it without allocating additional storage.

def even_odd(arr):
    ev_idx,odd_idx=0,len(arr)-1
    while ev_idx<odd_idx:
        if arr[ev_idx]%2==0:
            ev_idx+=1
        else:
            arr[ev_idx],arr[odd_idx]=arr[odd_idx],arr[ev_idx]
            odd_idx-=1
    return arr

