package web.mvc.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class TestController {
	@RequestMapping("/a")
	public String aa() {
		System.out.println("TestController call");
		
		return "index.html";
	}
}
