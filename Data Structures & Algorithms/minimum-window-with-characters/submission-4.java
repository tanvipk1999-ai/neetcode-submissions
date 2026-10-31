class Solution {
    public String minWindow(String s, String t) {
        if(t.isEmpty()) return "";
        String res = new String();
        int l = 0;
        Map<Character, Integer> need = new HashMap<>();
        Map<Character, Integer> window = new HashMap<>();

        for(char c:t.toCharArray()){
            need.put(c, need.getOrDefault(c,0)+1);
        }
        int have = 0;
        int required = need.size();
        int min_len = Integer.MAX_VALUE;

        for(int r=0;r<s.length();r++){
            char c = s.charAt(r);
            window.put(c, window.getOrDefault(c,0)+1);
            if(need.containsKey(c) && window.get(c).equals(need.get(c))){
                have += 1;
            }

            while(have == required){
                if(r-l+1 < min_len){
                    min_len = r-l+1;
                    res = s.substring(l, r+1);
                }
                window.put(s.charAt(l), window.get(s.charAt(l)) - 1);
                if(need.containsKey(s.charAt(l)) && window.get(s.charAt(l)) < need.get(s.charAt(l))){
                    have--;
                }
                l++;
            }
        }
        return res;
    }
}
