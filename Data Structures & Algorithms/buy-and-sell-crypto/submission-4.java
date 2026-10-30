class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int minBuy = prices[0];
        for(int p:prices){
            profit = Math.max(profit,p-minBuy);
            minBuy = Math.min(minBuy,p);
        }
        return profit;
    }
}
