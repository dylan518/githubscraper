package com.bannershallmark.controller;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.bannershallmark.entity.Accounts;
import com.bannershallmark.entity.PNL;
import com.bannershallmark.entity.PnlView;
import com.bannershallmark.entity.TradePairs;
import com.bannershallmark.entity.TradersAccounts;
import com.bannershallmark.entity.Users;
import com.bannershallmark.service.AccountsService;
import com.bannershallmark.service.MyUserDetails;
import com.bannershallmark.service.PNLService;
import com.bannershallmark.service.PnlViewService;
import com.bannershallmark.service.TradePairsService;

@Controller
@RequestMapping("/pnl")
public class PNLController {
	@Autowired
	private PNLService pnlService;
	@Autowired
	private PnlViewService pnlViewService;
	@Autowired
	private AccountsService accountsService;
	@Autowired
	private TradePairsService tradePairsService;

	@GetMapping("/allpnl")
	public String allpnl(Model model) {
		List<PNL> pnlList = pnlService.findAll();
		List<PnlView> pnlViews = pnlViewService.findAll();
		MyUserDetails user = (MyUserDetails) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
		Users users = user.getUser();
		int role = users.getRole().getId();
		model.addAttribute("role", role);
		if (role == 2) {
			pnlViews = pnlViewService.findByUserId(users.getId());
//			model.addAttribute("pnlList", pnlViews);
//			return "pnl/allpnl.html";
		}

		model.addAttribute("pnlList", pnlViews);
		return "pnl/allpnl.html";
	}

	@GetMapping("/addpnl")
	public String addpnl(Model model) {
		//// to Access user role////////////////
		MyUserDetails user = (MyUserDetails) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
		Users users = user.getUser();
		int role = users.getRole().getId();
		model.addAttribute("role", role);
		/////////////////////// end//////////
		List<TradersAccounts> accounts = accountsService.findTraderAccountsByTraderID(users.getId());
		List<TradePairs> tradePairsList = tradePairsService.findAll();

		model.addAttribute("tradePairsList", tradePairsList);
		model.addAttribute("accounts", accounts);
		return "pnl/addpnl.html";
	}

	@GetMapping("/editpnl")
	public String editpnl(@RequestParam("id") int id, Model model) {
		PNL pnl = pnlService.FindById(id);

		//// to Access user role////////////////
		MyUserDetails user = (MyUserDetails) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
		Users users = user.getUser();
		int role = users.getRole().getId();
		model.addAttribute("role", role);
		/////////////////////// end//////////
		List<TradersAccounts> accounts = accountsService.findTraderAccountsByTraderID(users.getId());
		List<TradePairs> tradePairsList = tradePairsService.findAll();
		model.addAttribute("tradePairsList", tradePairsList);
		model.addAttribute("accounts", accounts);
		model.addAttribute("pnl", pnl);
		return "pnl/addpnl.html";
	}

	@GetMapping("/deletepnl")
	public String deletepnl(@RequestParam("id") int id) {
		pnlService.DeleteById(id);
		return "redirect:/pnl/allpnl";
	}

	@PostMapping("/savePnl")
	public String savePnl(PNL pnl, @RequestParam("trDate") String trDate) {
		DateTimeFormatter formatter = DateTimeFormatter.ISO_LOCAL_DATE_TIME;
		LocalDateTime tradingDate = LocalDateTime.parse(trDate, formatter);
		Accounts accounts = accountsService.findAccountByAccountLogin(pnl.getAccountLogin()) ;
//		TradePairs tradePairs = tradePairsService.FindById(pair);
//		pnl.setAccounts(accounts);
//		pnl.setTradePair(tradePairs);
		System.out.println("accounts.getInitalSize() === "+accounts.getInitalSize());
		double pnlPercent = (pnl.getPnl()*100)/accounts.getInitalSize();
		pnl.setPnlPercent(pnlPercent);
		pnl.setTradingDate(tradingDate);
		pnlService.save(pnl);
		return "redirect:/pnl/allpnl";
	}
}
