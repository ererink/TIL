class Solution {
    public int solution(int n) {
        int answer = 0;
        int x = 1;
        for(int i=1; i<=x; i++){
            if ((n % i) == 1){
                answer = i;
            } else{
                x ++;
            }
        }
        return answer;
    }
}