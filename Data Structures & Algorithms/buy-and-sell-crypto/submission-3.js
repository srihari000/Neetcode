class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let maxP = 0
        let minB = prices[0]
        for(let sell of prices) {
            maxP = Math.max(maxP, sell - minB)
            minB = Math.min(minB, sell)
        }
        return maxP
    }
}
