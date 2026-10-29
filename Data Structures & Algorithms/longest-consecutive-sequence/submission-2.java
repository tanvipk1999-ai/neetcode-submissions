class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<> ();
        for(int n: nums){
            numSet.add(n);
        }
        int maxLen = 0;
        for(int n: numSet){
            if(!numSet.contains(n-1)){
                int len = 1;
                while(numSet.contains(n+len)){
                    len+=1;
                }
                if(len > maxLen){
                    maxLen = len;
                }
            }
        }
        return maxLen;
    }
}
