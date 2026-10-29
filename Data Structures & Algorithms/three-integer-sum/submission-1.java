class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums); // [-4,-1,-1,0,1,2]
        List<List<Integer>> res = new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            if(nums[i] > 0){
                break;
            }
            if(i>0 && nums[i]==nums[i-1]){
                continue;
            }
            int l = i+1;
            int r = nums.length - 1;
            while(l<r){
                int tSum = nums[i]+nums[l]+nums[r];
                if(tSum > 0){
                    r-=1;
                }
                else if(tSum < 0){
                    l+=1;
                }
                else{
                    res.add(Arrays.asList(nums[i],nums[l],nums[r]));
                    r-=1;
                    l+=1;
                    while(l<r && nums[l]==nums[l-1]){
                        l+=1;
                    }
                }
            }
        }
        return res;
    }
}
