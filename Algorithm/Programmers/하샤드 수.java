class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        String s = Integer.toString(x);
        int chk = 0;
        
        for(int i=0; i<s.length(); i++){
            int a = Character.getNumericValue(s.charAt(i));
            chk += a;
        }

        if(x % chk == 0){
            answer = true;
        } else{
            answer = false;
        }
        return answer;
    }
}