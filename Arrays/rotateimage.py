image=  [[1,  2,  3,  4]
         [5,  6,  7,  8],
         [9,  10, 11, 12],
         [13, 14, 15, 16]]
def rotate_image(image):
    left,right=0,len(image)-1
    while left<right:
        for i in range(right-left):
            top = left
            bottom = right
            image[top][left+i],image[top+i][right],image[bottom][right-i],image[bottom-i][left]=image[bottom-i][left],image[top][left+i],image[top+i][right],image[bottom][right-i]
        left+=1
        right-=1
    return image
print(rotate_image(image))


