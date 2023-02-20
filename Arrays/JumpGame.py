def canJump(arr):
    maxreach=0
    lastidx=len(arr)-1
    current=0
    while current<=maxreach and maxreach<lastidx:
        maxreach=max(maxreach,current+arr[current])
        current+=1
    return maxreach>=lastidx