class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let n = s.length
        let l = 0
        let r = n - 1

        while(l < r) {
            while(l < r && !this.isAlphaNum(s[l])) {
                l++
            }

            while(l < r && !this.isAlphaNum(s[r])) {
                r--
            }

            if(s[l].toLowerCase() !== s[r].toLowerCase()) {
                return false
            }
            l++
            r--
        }
        return true
    }
    isAlphaNum(c) {
        return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')
    }
}
