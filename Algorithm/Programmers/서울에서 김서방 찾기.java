class Solution {
    public String solution(String[] seoul) {
        String answer = "";
        int i = 0;
        for(String n : seoul){
            System.out.println(i + " " + n);
            if(n.equals("Kim")){
                answer = "김서방은 " + i + "에 있다";
                // System.out.println("김서방은 " + i + "에 있다");
            } else{
                i++;
                continue;
            }
        }
        return answer;
    }
}