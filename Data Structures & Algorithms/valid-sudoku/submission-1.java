class Solution {
    public boolean isValidSudoku(char[][] board) {
        int[] rows = new int[9];
        int[] cols = new int[9];
        int[] squares = new int[9];
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                if(board[i][j]!='.'){
                    int value = board[i][j] - '1';
                    int mask = 1<<value;
                    if((rows[i] & mask) > 0 || (cols[j] & mask) >0 || (squares[(i/3)*3+(j/3)] & mask) >0){
                        return false;
                    }
                    rows[i] |= mask;
                    cols[j] |= mask;
                    squares[(i/3)*3+(j/3)] |= mask;
                }
            }
        }
        return true;
    }
}
