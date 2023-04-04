package kb.mvc.controller;

import kb.mvc.dto.BoardDTO;
import kb.mvc.dto.ReplyDTO;
import kb.mvc.exception.DMLException;
import kb.mvc.exception.SearchWrongException;
import kb.mvc.service.BoardService;
import kb.mvc.service.BoardServiveImpl;
import kb.mvc.view.FailView;
import kb.mvc.view.SuccessView;

import java.util.List;


public class BoardController {
   private static BoardService boardService = BoardServiveImpl.getInstance();
   
   /**
    * 전체검색
    * */
   public static void boardSelectByAll() {
	  try {
		  List<BoardDTO> boardList = boardService.boardSelectAll();
		  SuccessView.selectPrint(boardList);

	  }catch (SearchWrongException e){
		  FailView.errorMessage(e.getMessage());
	  }
   }
    /**
     * 글번호에 해당하는 게시물 검색
     * */
	public static void boardSelectByNo(int boardNo) {
		try {
			BoardDTO dto = boardService.boardSelectByNo(boardNo);
			SuccessView.selectByNoPrint(dto);

		}catch (SearchWrongException e){
			FailView.errorMessage(e.getMessage());
		}
	}
	
	/**
	 * subject에 인수로 전달된 word를 포함한 게시물 검색
	 * */
	public static void boardSelectBySubject(String word) {
		try {
			List<BoardDTO> boardList = boardService.boardSelectBySubject(word);
			SuccessView.selectPrint(boardList);
		}catch (SearchWrongException e){
			FailView.errorMessage(e.getMessage());
		}
	}
	
	/**
	 * 게시물 등록하기 
	 * */
	public static void boardInsert(BoardDTO board) {
		try {
			boardService.boardInsert(board);
			SuccessView.messagePrint("게시물이 등록되었습니다.");

		}catch (DMLException e){
			FailView.errorMessage(e.getMessage());
		}
	}
	
	/**
	 * 게시물 수정하기
	 * */
	public static void boardUpdate(BoardDTO board) {
		try {
			boardService.boardUpdate(board);
			SuccessView.messagePrint("게시물이 수정되었습니다.");
		}catch (DMLException e){
			FailView.errorMessage(e.getMessage());
		}

	}
	
	/**
	 * 게시물 삭제하기 
	 * */
	public static void boardDelete(int no) {
		try {
			boardService.boardDelete(no);
			SuccessView.messagePrint("게시물이 삭제되었습니다.");
		}catch (DMLException e){
			FailView.errorMessage(e.getMessage());
		}
		
	}
	
	/**
	 * 댓글등록하기
	 * */
	public static void replyInsert(ReplyDTO replyDTO) {
		try {
			boardService.replyInsert(replyDTO);
			SuccessView.messagePrint("댓글이 게시되었습니다.");
		}catch (DMLException e){
			FailView.errorMessage(e.getMessage());
		}
	}

	/**
	 * 부모글에 해당하는 댓글정보 가져오기
	 * */
	public static void replySelectByParentNo(int boardNo) {
		try {
			BoardDTO boardDTO = boardService.replySelectByParentNo(boardNo);
			SuccessView.selectReplyPrint(boardDTO);
		}catch (SearchWrongException e){
			FailView.errorMessage(e.getMessage());
		}
		
	}
	
}//클래스끝



















