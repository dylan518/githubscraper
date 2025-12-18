package com.example.demo.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.example.demo.Util.AssertUtil;
import com.example.demo.Util.StringUtil;
import com.example.demo.pojo.User;
import com.example.demo.mapper.UserMapper;
import com.example.demo.service.IUserService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;

import java.beans.Transient;

/**
 * <p>
 *  服务实现类
 * </p>
 *
 * @author 老李
 * @since 2023-02-27
 */
@Service
public class UserServiceImpl extends ServiceImpl<UserMapper, User> implements IUserService {
    @Override
    public User login(String username,String password){
        AssertUtil.isTrue(StringUtil.isEmpty(username),"用户名不能为空");
        AssertUtil.isTrue(StringUtil.isEmpty(password),"密码不能为空");
        User user=this.findUserByUserName(username);
        AssertUtil.isTrue(null==user,"该用户记录不存在");
        AssertUtil.isTrue(!(user.getPassword().equals(password)),"密码错误");
        return null;
    }
    @Override
    public User findUserByUserName(String userName){

        return this.baseMapper.selectOne(new QueryWrapper<User>().eq("username",userName));
    }

    @Override
    //抛出异常就回转
    @Transactional(propagation = Propagation.REQUIRED,rollbackFor = Exception.class)
    public void updateUserInfo(User user) {
        AssertUtil.isTrue(StringUtil.isEmpty(user.getUsername()),"用户名不能为空！");
        User temp=this.findUserByUserName(user.getUsername());
        AssertUtil.isTrue(null !=temp&&!(temp.getId().equals(user.getId())),"用户名已存在！");
        AssertUtil.isTrue(!(this.updateById(user)),"用户更新失败！");
    }

    @Override
    @Transactional(propagation = Propagation.REQUIRED,rollbackFor = Exception.class)
    public void updatePassword(String username,String oldPassword,String newPassword,String confirmPassword) {
        User user=this.findUserByUserName(username);
        AssertUtil.isTrue(null==user,"用户名不存在或未登录！");
        AssertUtil.isTrue(StringUtil.isEmpty(oldPassword),"原始密码不能为空");
        AssertUtil.isTrue(StringUtil.isEmpty(newPassword),"新密码不能为空");
        AssertUtil.isTrue(StringUtil.isEmpty(confirmPassword),"确认密码不能为空");
        AssertUtil.isTrue(!(user.getPassword().equals(oldPassword)),"原始密码错误");
        AssertUtil.isTrue(!(newPassword.equals(confirmPassword)),"新密码和确认密码不一致");
        AssertUtil.isTrue(oldPassword.equals(newPassword),"新密码和原始密码一致");
        user.setPassword(newPassword);
        AssertUtil.isTrue(!updateById(user),"用户密码更新失败");
    }

}
