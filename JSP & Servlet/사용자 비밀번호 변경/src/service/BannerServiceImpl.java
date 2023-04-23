package service;

import java.util.List;

import dao.BannerDao;
import dao.BannerDaoImpl;

public class BannerServiceImpl implements BannerService{

	@Override
	public List<String> listBanner() {
		BannerDao bannerDao = new BannerDaoImpl();
		return bannerDao.listBanner();
	}

}
