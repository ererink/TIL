package web.mvc.controller;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import web.mvc.dto.Member;



@RestController  // @Controller + @ResponseBody
public class AjaxController {

	 @RequestMapping(value = "/load" , produces = "text/html;charset=UTF-8")
	 public String load() {
		 return "Ajax와 Spring의 만남~~";
	 }
	 
	 
	 @RequestMapping(value = "/ajax" , produces = "text/html;charset=UTF-8")
	 public String ajax(String name) {
		 System.out.println("name : " + name);
		 return name+"님 반가워요^^";
	 }
	 
	 /**
	  * 자바의 객체를 응답해주기 위해서는 json으로 변환해주는 
	  * jackson LIB가 필요하다. 
	  * */
	 @RequestMapping(value = "/json")
	 public List<String> json() {
		 System.out.println("json요청됨.....");
		 return  Arrays.asList("짬뽕","탕수육","짬짜면","깐풍기","깐쇼새우","유산슬","양장피","팔보채");
	 }
	 
	 @RequestMapping("/memberDto")
	 public Member test() {
		 return new Member("jang", "장희정", 20, "경기도 성남시");
	 }
	 
	 @RequestMapping("/memberList")
	 public List<Member> test2(){
		 List<Member> list = new ArrayList<>();
		 
		 list.add(new Member("jang", "장희정", 20, "경기도 성남시"));
		 list.add(new Member("kim", "김희선", 25, "서울시 강남구"));
		 list.add(new Member("lee", "이효리", 22, "서울시 강북구"));
		 list.add(new Member("king", "이민희", 20, "경기도 성남시"));
		 list.add(new Member("queen", "정수미", 35, "경기도 성남시"));
		 list.add(new Member("jeff", "이미여", 18, "서울시 강남구"));
		 
		 return list;
	 }
	 
	 @RequestMapping("/map")
	 public Map<String, Object> test3(){
		 Map<String, Object> map = new HashMap<>();
		 map.put("message", "Spring 최고!!!");
		 map.put("pageNo", 10);
		 map.put("dto", new Member("jang", "장희정", 20, "경기도 성남시"));
		 
          List<Member> list = new ArrayList<>();
		 list.add(new Member("kim", "김희선", 25, "서울시 강남구"));
		 list.add(new Member("lee", "이효리", 22, "서울시 강북구"));
		 list.add(new Member("king", "이민희", 20, "경기도 성남시"));
		 list.add(new Member("queen", "정수미", 35, "경기도 성남시"));
		 list.add(new Member("jeff", "이미여", 18, "서울시 강남구"));
		 
		 map.put("memberList", list);
		 
		 
		 return map;
	 }
	 
	 
}





















