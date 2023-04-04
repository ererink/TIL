package kb.mvc.view;

import java.util.Scanner;

import kb.mvc.controller.BoardController;
import kb.mvc.dto.BoardDTO;
import kb.mvc.dto.ReplyDTO;

public class MenuView {
   static Scanner sc =new Scanner(System.in);
 
   /**
    * 메뉴
    * */
    public static void menuChoice() {
         while(true) {
        	 System.out.println("\n----------------------------------------");
        	 System.out.print("[ 1. 전체검색   ");
        	 System.out.print("2. 글번호에 해당하는 검색   ");
          	System.out.print("3. 제목에 포함된 검색   ");
         	System.out.print("4. 등록   ");
         	System.out.print("5. 수정   ");
         	System.out.print("6. 삭제   ");
         	
         	System.out.print("7. 댓글등록   ");
         	System.out.print("8. 부모글의 댓글정보검색  ");
         	
         	System.out.print("9. 종료 ]");

              System.out.println("\n--------------------------------------------");
              System.out.println("선택메뉴는?");
              try {
	              int menu = Integer.parseInt(sc.nextLine());//
	              switch (menu) {
				  case 1:
					  BoardController.boardSelectByAll();	
					break;
	               case 2:
	            	   inputBoardByno(); //존재하는 게시물
					break;
	               case 3:
	            	   inputBoardBySubject();
	 				break;
	               case 4:
	            	   inputInsertBoard();
	 				break;
	               case 5:
	    				inputUpdateBoard();
	    				break;
	               case 6:
	            	   inputDeleteBoard();
	    				break;
	               case 7: //댓글등록
	            	   inputInsertReply();
	    				break;
	               case 8: //부모글의 댓글정보 검색
	            	   inputSelectReplyByParentNo();
	    				break;		
	    		
	               case 9:
	            	  System.out.println("다음에 다시 만나요~~^^ 로그아웃됩니다...");
	    			 System.exit(0);	
	    			break;
				default:
					System.out.println("잘못되었습니다..다시 입력해주세요.");
				}
	        	 
              }catch (NumberFormatException e) {
				System.out.println("메뉴는 숫자만 가능합니다.");
			}
         }//while문
    	
    }
   
	/**
     * 2. 글번호 검색...
     * */
     public static void inputBoardByno() {
    	 try {
	    	 System.out.println("글번호는 ???");
	    	 String no = sc.nextLine();
	    	 
	    	 BoardController.boardSelectByNo(Integer.parseInt(no));
    	  }catch (NumberFormatException e) {
			System.out.println("글번호는 숫자만 입력해주세요.");
			System.out.println("다시 할래요?  yes or no");
			String choice = sc.nextLine();
			if(choice.equals("yes")) {
				inputBoardByno();
			}
		 }//catch블럭End
     }//메소드 end
     
     /**
      *  검색필드..검색
      * */
     public static void inputBoardBySubject() {
    	 System.out.println("찾을 문자열은 ???");
    	 String word = sc.nextLine();
    	 BoardController.boardSelectBySubject(word);
     }
    
    
    /**
     *  등록
     * */
     public static void inputInsertBoard() {
    	 System.out.println("제목은?");
    	 String subject = sc.nextLine();
    	 
    	 System.out.println("작성자?");
    	 String writer = sc.nextLine();
    	 
    	 System.out.println("내용은?");
    	 String content = sc.nextLine();
    	 
    	 BoardDTO board =  new BoardDTO(0, subject, writer, content, null);
    	 BoardController.boardInsert(board);
     }
     
    /**
     * 수정
     * */
     public static void inputUpdateBoard() {
    	 System.out.println("수정 할 게시물 번호는?");
    	 int no = Integer.parseInt(sc.nextLine());
    	 
    	 System.out.println("수정 내용은?");
    	 String content = sc.nextLine();
    	
    	 BoardDTO board =  new BoardDTO(no, null, null, content, null);
    	 
    	 BoardController.boardUpdate(board);
     }
    
    /**
     * 삭제
     * */
     public static void inputDeleteBoard() {
    	 System.out.println("삭제 게시물 번호는?");
    	 int no = Integer.parseInt(sc.nextLine());
    	 BoardController.boardDelete(no);
     }
     
     /**
      *  부모글에 해당하는 댓글정보 검색하기 
      * */
     public static void inputSelectReplyByParentNo() {
    		//부모글의 글번호를 키보드로 입력받는다.
    	  System.out.println("검색하려는 댓글의 부모 글번호 ?");
    	  int boardNo = Integer.parseInt(sc.nextLine());
    	  BoardController.replySelectByParentNo(boardNo);
    	  
    	}
     
     
     /**
      * 댓글등록
      * */
     public static void inputInsertReply() {
    	//키보드 입력으로 댓글내용 , 등록하려는 부모글번호 입력받는다.
    	 System.out.println("댓글을 등록하려는 부모글 번호 ?");
    	 int boardNo = Integer.parseInt(sc.nextLine());
    	 
    	 System.out.println("댓글 내용은 ?");
    	 String replyContent = sc.nextLine();
    	 
    	 BoardController.replyInsert(new ReplyDTO(replyContent, boardNo));
    	 
    		
    }
}//클래스끝

















