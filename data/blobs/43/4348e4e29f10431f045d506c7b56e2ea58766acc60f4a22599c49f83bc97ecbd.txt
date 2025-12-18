package com.kfm.shop.system.controller;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.github.pagehelper.PageHelper;
import com.kfm.shop.common.util.Result;
import com.kfm.shop.system.domain.Role;
import com.kfm.shop.system.domain.dto.RoleGrantMenuDTO;
import com.kfm.shop.system.service.RoleService;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.util.ObjectUtils;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/role")
@Api(tags = "角色接口",value = "角色接口",description = "角色接口")
public class RoleController {
    @Autowired
    private RoleService roleService;

    @GetMapping
    @ApiOperation(value = "获取所有角色信息", notes = "获取所有角色信息")
    public Result getRole(@ApiParam(name = "menu", value = "角色信息") Role role) {
//        throw new RuntimeException("模拟异常");
        // 构建查询条件
        QueryWrapper<Role> queryWrapper = new QueryWrapper<>();
        if (!ObjectUtils.isEmpty(role.getName())) {
            queryWrapper.like("name", role.getName());
        }
        if (!ObjectUtils.isEmpty(role.getName())){
            queryWrapper.eq("status", role.getName());
        }
        // 分页
        PageHelper.startPage(role.getPage(), role.getSize());
        return Result.ok(roleService.list(queryWrapper));
    }

    @GetMapping("/{id}")
    @ApiOperation(value = "根据id获取角色信息", notes = "根据id获取角色信息")
    public Result getRoleById(@ApiParam(name = "id", value = "角色id", required = true) @PathVariable Integer id) {
        return Result.ok(roleService.getById(id));
    }


    @PostMapping("/edit")
    @ApiOperation(value = "根据id修改角色信息", notes = "根据id修改角色信息")
    public Result updateRoleById(@ApiParam(name = "menu", value = "角色信息", required = true) Role role) {
        return Result.ok(roleService.updateById(role));
    }



    @PutMapping("/add")
    @ApiOperation(value = "新增角色信息", notes = "新增角色信息")
    public Result addRole(@ApiParam(name = "menu", value = "角色信息", required = true) Role role) {
        return Result.ok(roleService.save(role));
    }

    @DeleteMapping("/{id}")
    @ApiOperation(value = "根据id删除角色信息", notes = "根据id删除角色信息")
    public Result deleteRoleById(@ApiParam(name = "id", value = "角色id", required = true) @PathVariable Integer id) {
        return Result.ok(roleService.removeById(id));
    }
    @PostMapping("/grant")
    @ApiOperation(value = "根据id修改角色信息", notes = "根据id修改角色信息")
    public Result grantMenu(@RequestBody RoleGrantMenuDTO roleGrantMenuDTO){
        return Result.ok(roleService.grant(roleGrantMenuDTO));
    }
}
