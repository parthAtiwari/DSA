# naive approach for m*n matrix
def spiralmatrix(mat):
    left,right=0,len(mat[0])
    top,bottom=0,len(mat)
    spiral=[]
    while top<bottom and left<right:
        for i in range(left,right):
            spiral.append((mat[top][i]))
        top+=1
        for i in range(top,bottom):
            spiral.append(mat[i][right-1])
        right-=1
        if not(left<right and top<bottom):
            break
        for i in range(right-1,left-1,-1):
            spiral.append(mat[bottom-1][i])
        bottom-=1
        for i in range(bottom-1,top-1,-1):
            spiral.append(mat[i][left])
        left+=1
    return spiral

# other pythonic approach for n*n matrix
def spiralmatrix(mat):
    def matrix_layer_clockwise(idx):
        if idx==len(mat)-idx-1:
            spiral.add(mat[idx][idx])
            return
        spiral.extend(mat[idx][idx:-1-idx])
        spiral.extend(list(zip(*mat))[-1-idx][idx:-1-idx])
        spiral.extend(mat[-1-idx][-1-idx:idx:-1])
        spiral.extend(list(zip(*mat))[idx][-1-idx:idx:-1])




    spiral=[]
    for i in range((len(mat)+1)//2):
        matrix_layer_clockwise(i)
    return spiral
