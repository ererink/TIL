package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

import common.DBManager;

public class BannerDaoImpl implements BannerDao{

	@Override
	public List<String> listBanner() {
		List<String> bannerList = new ArrayList<>();
		Connection con = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		
		try {
			con = DBManager.getConnection();
			String sql = "select banner_text from banner ";
			pstmt = con.prepareStatement(sql);
			
			System.out.println(pstmt.toString());
			rs = pstmt.executeQuery();

			while(rs.next()) {
				bannerList.add(rs.getString("banner_text"));
			}
			
		}catch(Exception e) {
			e.printStackTrace();
		}finally {
			DBManager.releaseConnection(con, pstmt, rs);
		}
		
		return bannerList;
	}

}
