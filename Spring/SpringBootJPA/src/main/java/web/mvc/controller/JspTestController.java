package web.mvc.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class JspTestController {
	@RequestMapping("/b")
	public String bb() {
		System.out.println("JspTestController call");
		
		return "index";
	}
	
	@RequestMapping("/{url}")
	public void url() {
		
	}
}
