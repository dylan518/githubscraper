package com.xworkz.springcm.temple.controller;

import java.util.List;

import javax.annotation.PostConstruct;

import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import com.xworkz.springcm.temple.dto.AppPropertyDTO;
import com.xworkz.springcm.temple.service.AppPropertySERVICE;

@Controller
@RequestMapping("/")
public class RefInitLandingController {
	
	private static final Logger logger=Logger.getLogger(RefInitLandingController.class);
	
	private List<AppPropertyDTO> entryList;
	private List<AppPropertyDTO> prasadaList;
	private List<AppPropertyDTO> idList;
	private List<AppPropertyDTO> poojaTypeList;
	
	@Autowired
	public AppPropertySERVICE appPropertyService;

	public RefInitLandingController() {
		logger.info("Created \t" + this.getClass().getSimpleName());
	}

	@PostConstruct
	public void init() {
		logger.info("Invoked init method by post construct");
		logger.debug(appPropertyService);
		entryList=appPropertyService.validateAndFetchAllByType("se");
		logger.info("Special entry List: "+entryList);
		prasadaList=appPropertyService.validateAndFetchAllByType("prasada");
		logger.info("prasada List: "+prasadaList);
		idList=appPropertyService.validateAndFetchAllByType("id");	
		logger.info("id List: "+idList);
		poojaTypeList=appPropertyService.validateAndFetchAllByType("pt");
		logger.info("pooja Type List: "+poojaTypeList);
	}
	
	@RequestMapping(value = "/booking.cm")
	public String doNavigateForBookingPage(Model model) {
		logger.info("Invoked landing page with list values, register.jsp");
		logger.debug(model);
		model.addAttribute("specialEntryList", entryList);
		model.addAttribute("prasadaList", prasadaList);
		model.addAttribute("idList", idList);
		model.addAttribute("poojaTypeList", poojaTypeList);
		logger.info("Invoking list has completed try registering");
		return "BookVisit";
	}
	
}
