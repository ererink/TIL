package common;
/**
 * DB의 설정 정보들 상수로 관리
 * */
public interface DBProperties {
  public static final String DRVIER_NAME="oracle.jdbc.driver.OracleDriver";
   String URL="jdbc:oracle:thin:@localhost:1521:XE";
   String USER_ID="c##scott";
   String USER_PASS="tiger";
   
}
