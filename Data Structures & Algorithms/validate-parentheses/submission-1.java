class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character,Character> co = new HashMap<>();
        co.put(')','(');
        co.put('}','{');
        co.put(']','[');

        for(char c: s.toCharArray()){
            if(!co.containsKey(c)){
                stack.push(c);
            }
            else{
                if(!stack.isEmpty() && stack.peek() == co.get(c)){
                    stack.pop();
                }
                else{
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
