package web.mvc.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import web.mvc.domain.Board;

public interface BoardRepository extends JpaRepository<Board, Long>{
	
	/**
	 * JPQL 문법 적용 
	 * 인수로 전달된 글번호보다 큰 레코드 삭제 
	 * 	: JPQL 에서 DML 문장인 경우는 @Modifying 선언 필수 
	 */
	@Query("delete from Board b where b.bno > ?1")
	@Modifying
	 void deleteGrateThan(Long bno);
	
	/**
	 * 글번호 또는 제목에 해당하는 레코드 검색 
	 */
	//@Query("select b from Board b where b.bno > ?1 or b.title = ?2")
	@Query(value = "select * from Board b where bno > ?1 or title = ?2", nativeQuery=true)
	List<Board> selectByBnoTitle(Long bno, String title);
	
	/**
	 * 글번호, 제목, 작성자에 해당하는 레코드 검색 
	 */
	@Query("select b from Board b where b.bno=:#{#bo.bno} or > b.title=:#{#bo.title} or b.writer=:#{#bo.writer}")
	List<Board> selectByPramsBoard(@Param("bo") Board board);
}
