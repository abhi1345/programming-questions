# Complete the hourglassSum function below.
def hourglassSum(arr):
    sums = []
    
    i = 0
    
    while i < len(arr)-2:
        
        j = 0
        
        while j < len(arr[0])-2:
            
            temp = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            
            sums.append(temp)
            
            j += 1
            
            
            
        i += 1
            
    return max(sums)
