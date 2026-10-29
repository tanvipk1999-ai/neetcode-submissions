class Solution {
    public boolean isValidSudoku(char[][] board) {
        int n = board.length;
        int[] rows = new int[n];
        int[] cols = new int[n];
        int[] squares = new int[n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(board[i][j]!='.'){
                    int value = board[i][j] - '1';
                    int mask = 1<<value;
                    if((rows[i] & mask) > 0 || (cols[j] & mask)>0 || (squares[(i/3)*3 +(j/3)] & mask) >0){
                        return false;
                    }
                    rows[i] |= mask;
                    cols[j] |= mask;
                    squares[(i/3)*3 +(j/3)] |= mask;
                }
            }
        }
        return true;
    }
}
