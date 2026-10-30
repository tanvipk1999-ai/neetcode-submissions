class Solution {
    public int trap(int[] height) {
        int l = 0;
        int r = height.length - 1;
        int res = 0;
        int maxl = height[l];
        int maxr = height[r];
        while(l<r){
            if(maxl<maxr){
                l+=1;
                maxl = Math.max(maxl,height[l]);
                res += maxl-height[l];
            }
            else{
                r-=1;
                maxr = Math.max(maxr,height[r]);
                res += maxr-height[r];
            }
        }
        return res;
    }
}
