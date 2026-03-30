class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let numSet = new Set(nums)
        let longest = 0
        for(let n of numSet) {
            if(!numSet.has(n - 1)) {
                let length = 1
                while(numSet.has(n+length)) {
                    length += 1
                }
                longest = Math.max(longest, length)
            }
        }
        return longest
    }
}
