package kb.mvc.exception;

public class SearchWrongException extends RuntimeException {
	/**
	 * 검색에 관련된 오류가 있을 때 발생시킬 예외
	 */
	private static final long serialVersionUID = 1L;
	public SearchWrongException() {}
	public SearchWrongException(String message) {
		super(message);
	}

}
