class Solution {
    public int[] productExceptSelf(int[] arr) {
        int i, temp = 1;
        int n = arr.length;
         
        int prod[] = new int[n];
 
        for(int j=0;j<n;j++)
            prod[j]=1;
 
        for (i = 0; i < n; i++) 
        {
            prod[i] = temp;
            temp *= arr[i];
        }
 
        temp = 1;
 
        for (i = n - 1; i >= 0; i--) 
        {
            prod[i] *= temp;
            temp *= arr[i];
        }
        
        return prod;

    }
}
