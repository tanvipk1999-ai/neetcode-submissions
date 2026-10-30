class Solution {
    public int characterReplacement(String s, int k) {
        int l = 0;
        int maxf = 0;
        HashMap<Character,Integer> freq = new HashMap<>();
        int res = 0;
        for(int r=0;r<s.length();r++){
            freq.put(s.charAt(r), freq.getOrDefault(s.charAt(r),0)+1);
            maxf = Math.max(maxf, freq.get(s.charAt(r)));
            while((r-l+1)-maxf > k){
                freq.put(s.charAt(l), freq.get(s.charAt(l))-1);
                l+=1;
            }
            res = Math.max(res, r-l+1);
        }
        return res;
    }
}
