package Day6.P_크레인인형뽑기게임;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class P_크레인인형뽑기게임_김예린 {
    public static void main(String[] args) throws IOException {
        int [][] board = {{0,0,0,0,0}, {0,0,1,0,3}, {0,2,5,0,1}, {4,2,4,4,2}, {3,5,1,3,1}};
        int [] moves = {1,5,3,5,1,2,1,4};
        int N = board.length;
        List<List<Integer>> col_b = new ArrayList<>();

        for (int i=0; i<N; i++){
            List<Integer> line = new ArrayList<>();
            for (int j=N-1; j>=0; j--){
                if (board[j][i] != 0){
                    line.add(board[j][i]);
                }
            }
            col_b.add(line);
        }

        List<Integer> picked = new ArrayList<>();
        int check = 0;
        int cnt = 0;
        for (int i = 0; i < moves.length; i++) {
            if (col_b.isEmpty() || col_b.get(moves[i] - 1).isEmpty()) {
                continue;
            }
            check = col_b.get(moves[i] - 1).remove(col_b.get(moves[i] - 1).size()-1);
            if (picked.isEmpty()) {
                picked.add(check);
            } else if (check == picked.get(picked.size()-1)) {
                picked.remove(picked.size()-1);
                cnt += 2;
            } else {
                picked.add(check);
            }
        }

        System.out.println(cnt);
    }
}
