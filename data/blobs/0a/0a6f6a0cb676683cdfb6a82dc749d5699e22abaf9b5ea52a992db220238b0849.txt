package com.pks.test.ajax;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import com.pks.test.ajax.bo.BookingBO;
import com.pks.test.ajax.model.Booking;

@Controller
@RequestMapping("/ajax/booking")
public class BookingController {

	@Autowired
	private BookingBO bookingBO;
	
	@GetMapping("/home")
	public String booking() {
		return "/ajax/booking/booking";
	}
	
	@GetMapping("/list")
	public String bookingList(Model model) {
		
		List<Booking> bookinglist = bookingBO.getBooking();
		
		model.addAttribute("bookinglist", bookinglist);
		
		return "/ajax/booking/list";
	}
	
	@GetMapping("/input")
	public String bookingInput() {
		return "/ajax/booking/input";
	}
	
	
	// 데이터 전달받고 저장하는 api
	@GetMapping("/add")
	@ResponseBody
	public Map<String, String> addBooking(
			@RequestParam("name") String name
			, @RequestParam("date") String date
			, @RequestParam("day") int day
			, @RequestParam("headcount") int headcount
			, @RequestParam("phoneNumber") String phoneNumber
			) {
		
		int count = bookingBO.addBooking(name, date, day, headcount, phoneNumber);
	
		// {"result":"success"}
		// {"result":"fail"}
		
		Map<String, String> map = new HashMap<>();
		
		if(count == 1) { 
			map.put("result", "success");
		} else {
			map.put("result", "fail");
		}
		
		return map;
		
	}
	
	
	@GetMapping("/delete")
	@ResponseBody
	public Map<String, String> deleteBooking(@RequestParam("id") int id) {
		int count = bookingBO.deleteBooking(id);
		
		Map<String, String> map = new HashMap<>();
		
		if(count == 1) {
			map.put("result", "success");
		} else {
			map.put("result", "fail");
		}
		
		return map;
	}
	
	
	// 이름 전화번호 전달받고, 일치하는 결과 하나를 json 형태로 변화해서 리스펀스에 담는다.
	@GetMapping("/confirm")
	@ResponseBody
	public Map<String, Object> printBooking(
			@RequestParam("name") String name
			, @RequestParam("phoneNumber") String phoneNumber
			){

		// 이름 전화번호로 데이터 조회

		Booking booking = bookingBO.confirmBooking(name, phoneNumber);
		
		// 조회가 성공하면 "result" : "success" , "data":booking}
		// 조회가 실패하면 "result" : "fail"}
		
		Map<String, Object> result = new HashMap<>();
		
		if(booking != null) {
			result.put("result", "success");
			result.put("booking", booking);
		} else {
			result.put("result", "fail");
		}
		
		return result;
		 
			
	 }

}
	
	
	

