package com.leo.fly.db.system.setting.controller;

import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.leo.fly.common.entity.vo.JsonResult;
import com.leo.fly.db.system.setting.entity.SystemSetting;
import com.leo.fly.db.system.setting.params.SystemSettingAddForm;
import com.leo.fly.db.system.setting.params.SystemSettingQueryForm;
import com.leo.fly.db.system.setting.params.SystemSettingQueryParam;
import com.leo.fly.db.system.setting.params.SystemSettingUpdateForm;
import com.leo.fly.db.system.setting.service.SystemSettingService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;

@RestController
@RequestMapping("/system/setting")
public class SystemSettingController {
	@Autowired
	SystemSettingService systemSettingService;
	@PostMapping
	public JsonResult add(@RequestBody SystemSettingAddForm addForm) {
		//log.debug("name:{}", addForm);
		SystemSetting systemSetting = addForm.toPo(SystemSetting.class);
		return JsonResult.success(systemSettingService.save(systemSetting));
	}
	@PutMapping()
	public JsonResult update( @Valid @RequestBody SystemSettingUpdateForm updateForm) {
		SystemSetting systemSetting = updateForm.toPo(SystemSetting.class);
		return JsonResult.success(systemSettingService.updateById(systemSetting));
	}
	@GetMapping(value = "/{id}")
	public JsonResult get(@PathVariable String id) {
		//log.debug("get with id:{}", id);
		return JsonResult.success(systemSettingService.getById(id));
	}
	@PostMapping(value = "/page")
	public JsonResult page(@Valid @RequestBody SystemSettingQueryForm systemSettingQueryForm) {
		//log.debug("search with systemSettingQueryForm:{}", systemSettingQueryForm);
		Page<SystemSetting> page = systemSettingService.page(systemSettingQueryForm.getPage(), systemSettingQueryForm.toParam(SystemSettingQueryParam.class));
		return JsonResult.success(page);
	}
	@DeleteMapping(value = "/{id}")
	public JsonResult delete(@PathVariable String id) {
		return JsonResult.success(systemSettingService.removeById(id));
	}
}
