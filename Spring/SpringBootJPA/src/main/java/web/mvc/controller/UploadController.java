package web.mvc.controller;

import java.io.File;

import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import web.mvc.dto.UploadDTO;


@Controller
public class UploadController {
	
	@RequestMapping("/upload")
	public String upload2(UploadDTO dto , HttpSession session) {
		
		//폴더에 저장
		String path = session.getServletContext().getRealPath("/images");
		File f = new File( path +"/" + dto.getFile().getOriginalFilename());
		try {
			
		  dto.getFile().transferTo(f);
		  
		}catch (Exception e) {
			e.printStackTrace();
		}
		
		dto.setFileName(dto.getFile().getOriginalFilename());
		dto.setFileSize(dto.getFile().getSize());
		
		return "uploadResult";
	}
	
	/**
	 * 다운로드 목록가져오기
	 * */
	@RequestMapping("/downList")
	public ModelAndView downList(HttpSession session) {
		String path = session.getServletContext().getRealPath("/images");
		File file = new File(path);
		String fileNames [] = file.list();
		
		return new ModelAndView("downList" , "fileNames", fileNames); //${fileNames}
	}
	
	/**
	 * 다운로드하기
	 * */
	@RequestMapping("/down.do")
	public ModelAndView down(String fileName , HttpSession session) {
		String path = session.getServletContext().getRealPath("/images");
		File file = new File(path+"/"+fileName);
		
		//다운로드를 담당하는 뷰클래스 실행하게한다!!
		return new ModelAndView("downLoadView", "fname" , file);//뷰의 이름이 id="downLoadView" 찾기!!!!
	}
	
	
}









