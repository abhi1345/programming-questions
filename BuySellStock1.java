class Solution {
    public int maxProfit(int[] prices) {
        int l = prices.length;
        int buy = 1341241;
        int sell = 0;
        int profit = 0;
        
        for (int i=0; i < l; i++) {
            buy = prices[i];
            for (int j = i; j < l; j++) {
                if (prices[j] - buy > profit) {
                    profit = prices[j] - buy;
                }
            }
        }
        
        
        return profit;
        
    }
}
