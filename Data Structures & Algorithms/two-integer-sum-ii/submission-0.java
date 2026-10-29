class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0;
        int r = numbers.length - 1;
        int[] res = new int[2];
        for(int i=0;i<numbers.length;i++){
            int csum = numbers[l] + numbers[r];
            if(csum < target){
                l+=1;
            }
            else if(csum > target){
                r-=1;
            }
            else{
                res[0] =l+1;
                res[1]=r+1;
            }
        }
        return res;
    }
}
