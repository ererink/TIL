package kb.mvc.service;

import java.sql.SQLException;
import java.util.List;

import kb.mvc.dto.BoardDTO;
import kb.mvc.dto.ReplyDTO;
import kb.mvc.exception.DMLException;
import kb.mvc.exception.SearchWrongException;

public interface BoardService {
	/**
	 * 모든 레코드 검색
	 */
	List<BoardDTO> boardSelectAll() throws SearchWrongException;

	/**
	 * 제목에 특정문자열 포함한 레코드 검색
	 */
	List<BoardDTO> boardSelectBySubject(String keyWord) throws SearchWrongException;

	/**
	 * 글번호에 해당하는 레코드 검색
	 */
	BoardDTO boardSelectByNo(int boardNo) throws SearchWrongException;

	/**
	 * 게시물 등록 
	 */
	void boardInsert(BoardDTO boardDTO) throws DMLException;

	/**
	 * 게시물 수정
	 */
	void boardUpdate(BoardDTO boardDTO) throws DMLException;

	/**
	 * 게시물 삭제
	 */
	void boardDelete(int boardNo) throws DMLException;
	
	
	/**
	 * 댓글등록하기
	 * */
	void replyInsert(ReplyDTO replyDTO)throws DMLException;

	/**
	 * 부모글에 해당하는 댓글 정보 가져오기 
	 * */
     BoardDTO replySelectByParentNo(int boardNo) throws SearchWrongException;
}
















