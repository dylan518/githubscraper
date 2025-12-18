package po.item;

import java.text.DecimalFormat;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.servlet.http.HttpServletRequest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import po.common.SearchVO;
import po.vendor.VendorService;
import po.vendor.VendorVO;

@Controller
public class ItemController {

	@Autowired
	private ItemService itemService;
	@Autowired
	private VendorService vendorService;

	// 리스트
	@RequestMapping(value = "/itemList")
	public String itemList(SearchVO searchVO, ModelMap modelMap) throws Exception {
		List<?> vendorList = itemService.selectVendorSelectList();
		
		if((searchVO.getSelectedVendor() == null || searchVO.getSelectedVendor().equals("")) 
				&& (searchVO.getHiddenKeyword() == null || searchVO.getHiddenKeyword().equals(""))) {
			searchVO.setHiddenKeyword(((VendorVO)vendorList.get(0)).getId());
		}else if(searchVO.getSelectedVendor() == null || searchVO.getSelectedVendor().equals("")){
			searchVO.setSelectedVendor(searchVO.getHiddenKeyword());
		}else if(searchVO.getHiddenKeyword() == null || searchVO.getHiddenKeyword().equals("")){
			searchVO.setHiddenKeyword(searchVO.getSelectedVendor());
		}else {
			
		}

		searchVO.pageCalculate( itemService.selectItemCount(searchVO) ); 
		List<?> listview   = itemService.selectItemList(searchVO);

		modelMap.addAttribute("vendor", searchVO.getHiddenKeyword());
		modelMap.addAttribute("vendorList", vendorList);
		modelMap.addAttribute("listview", listview);
		modelMap.addAttribute("searchVO", searchVO);
		return "item/itemList";
	}

	@RequestMapping(value = "/itemForm")
	public String itemForm(HttpServletRequest request, ModelMap modelMap) throws Exception {
		String id = request.getParameter("id");

		ItemVO itemInfo = new ItemVO();
		if (id!=null) {
			itemInfo = itemService.selectItemOne(id);
		}

		String vendor = request.getParameter("vendor");
		VendorVO vendorVO = vendorService.selectVendorOne(vendor);

		itemInfo.setVendor(vendorVO.getId());
		itemInfo.setVendorName(vendorVO.getName());

		modelMap.addAttribute("itemInfo", itemInfo);

		return "item/itemForm";
	}

	@RequestMapping(value = "/itemSave")
	public String itemSave(ItemVO itemInfo, ModelMap modelMap) throws Exception {
		List<?> vendorList = itemService.selectVendorSelectList();
	
		if(itemInfo.getVendor() == null || itemInfo.getVendor().equals("")) {
			itemInfo.setVendor(((VendorVO)vendorList.get(0)).getId());
		}
		itemService.insertItem(itemInfo);
		String selectedVendor = itemInfo.getVendor();
		modelMap.addAttribute("selectedVendor", selectedVendor);
		return "redirect:/itemList";
	}

	@RequestMapping(value = "/itemRead")
	public String itemSave(HttpServletRequest request, ModelMap modelMap) throws Exception {

		String id = request.getParameter("id");

		ItemVO itemInfo = itemService.selectItemOne(id);

		modelMap.addAttribute("itemInfo", itemInfo);

		return "item/itemRead";
	}

	@RequestMapping(value = "/itemDelete")
	public String itemDelete(HttpServletRequest request) throws Exception {

		String id = request.getParameter("id");

		itemService.deleteItemOne(id);

		return "redirect:/itemList";
	}

	@RequestMapping(value = "/deleteItems", method = RequestMethod.POST) 
	public String deleteItems(@RequestParam("delete_item_ids") String[] delete_item_ids, ModelMap modelMap) throws Exception { 
		for (String item_id : delete_item_ids) { 
			itemService.deleteItemOne(item_id); 
		}
		// 목록 페이지로 이동 
		return "redirect:/itemList"; 
	}

}

