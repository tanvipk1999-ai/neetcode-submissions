class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        Stack<Integer> stack = new Stack<>();
        int[] res = new int[n];
        for(int i=0;i<n;i++){
            int temp = temperatures[i];
            while(!stack.isEmpty() && temp > temperatures[stack.getLast()]){
                int t = stack.removeLast();
                res[t] = i-t;
            }
            stack.push(i);
        }
        return res;
    }
}
