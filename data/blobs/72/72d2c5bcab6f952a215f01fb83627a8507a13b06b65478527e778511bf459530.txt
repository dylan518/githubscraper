package com.yimoo.smartcampussystemdemo.controller;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.api.R;
import com.yimoo.smartcampussystemdemo.pojo.Admin;
import com.yimoo.smartcampussystemdemo.pojo.LoginForm;
import com.yimoo.smartcampussystemdemo.pojo.Student;
import com.yimoo.smartcampussystemdemo.pojo.Teacher;
import com.yimoo.smartcampussystemdemo.service.AdminService;
import com.yimoo.smartcampussystemdemo.service.StudentService;
import com.yimoo.smartcampussystemdemo.service.TeacherService;
import com.yimoo.smartcampussystemdemo.util.*;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import io.swagger.models.auth.In;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import javax.imageio.ImageIO;
import javax.servlet.ServletContext;
import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.LinkedHashMap;
import java.util.Locale;
import java.util.Map;
import java.util.UUID;

/**
 * @ClassName: SystemController
 * @Author: yimoorua
 * @Date: 2022/10/8 17:27
 * @Description:
 * @Version: 1.0
 **/
@Api(tags = "系统控制器")
@RestController
@RequestMapping("/sms/system")
public class SystemController {

    @Autowired
    private AdminService adminService;
    @Autowired
    private StudentService studentService;
    @Autowired
    private TeacherService teacherService;

    @ApiOperation("获取验证码（图片和代码）")
    @RequestMapping(value = "/getVerifiCodeImage", method = RequestMethod.GET)
    public void getverifiCodeImage(HttpServletRequest request, HttpServletResponse response) {
        //获取图片
        BufferedImage verifiCodeImage = CreateVerifiCodeImage.getVerifiCodeImage();
        //获取图片上的验证码
        String verifiCode = new String(CreateVerifiCodeImage.getVerifiCode());
        //将验证码文本放入session域，为下一次验证做准备
        HttpSession session = request.getSession();
        session.setAttribute("verifiCode", verifiCode);
        //将验证图片响应给浏览器
        try {
            ServletOutputStream outputStream = response.getOutputStream();
            ImageIO.write(verifiCodeImage, "JPEG", response.getOutputStream());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @ApiOperation("登录验证，根据不同的userType传回不同的token")
    @RequestMapping(value = "/login", method = RequestMethod.POST)
    public Result login(
            @ApiParam("登录的账号信息")
            @RequestBody LoginForm loginForm, HttpServletRequest request) {
        //验证码校验
        HttpSession session = request.getSession();
        String sessionverifiCode = (String) session.getAttribute("verifiCode");
        System.out.println(sessionverifiCode);//Nfob
        String loginFormverifiCode = loginForm.getVerifiCode();
        System.out.println(loginFormverifiCode);//
        if ("".equals(sessionverifiCode) || null == sessionverifiCode) {
            return Result.fail().message("验证码失效，请刷新后重试");
        }
        if (!sessionverifiCode.equalsIgnoreCase(loginFormverifiCode)) {
            return Result.fail().message("验证码错误，请重新输入！");
        }
        //从session中移除现有验证码
        session.removeAttribute("verifiCode");
        //分用户类型进行校验
        //准备一个map用户存放响应的数据
        Map<String, Object> map = new LinkedHashMap<>();
        switch (loginForm.getUserType()) {
            case 1:
                try {
                    Admin admin = adminService.login(loginForm);
                    if (admin != null) {
                        //用户的类型和用户的id转换成一个密文，以token的名称向客户端反馈
                        String token = JwtHelper.createToken(admin.getId().longValue(), 1);
                        map.put("token", token);
                    } else {
                        throw new RuntimeException("账号信息有误！");
                    }
                    return Result.ok(map);
                } catch (RuntimeException e) {
                    e.printStackTrace();
                    return Result.fail().message(e.getMessage());
                }
            case 2:
                try {
                    Student student = studentService.login(loginForm);
                    if (student != null) {
                        //用户的类型和用户的id转换成一个密文，以token的名称向客户端反馈
                        String token = JwtHelper.createToken(student.getId().longValue(), 2);
                        map.put("token", token);
                    } else {
                        throw new RuntimeException("账号信息有误！");
                    }
                    return Result.ok(map);
                } catch (RuntimeException e) {
                    e.printStackTrace();
                    return Result.fail().message(e.getMessage());
                }
            case 3:
                try {
                    Teacher teacher = teacherService.login(loginForm);
                    if (teacher != null) {
                        //用户的类型和用户的id转换成一个密文，以token的名称向客户端反馈
                        String token = JwtHelper.createToken(teacher.getId().longValue(), 3);
                        map.put("token", token);
                    } else {
                        throw new RuntimeException("账号信息有误！");
                    }
                    return Result.ok(map);
                } catch (RuntimeException e) {
                    e.printStackTrace();
                    return Result.fail().message(e.getMessage());
                }
        }
        return Result.fail().message("查无此用户");
    }

    @ApiOperation("从响应头中的token获取信息")
    @RequestMapping(value = "/getInfo", method = RequestMethod.GET)
    public Result getInfoByToken(
            @ApiParam("json格式的token信息")
            @RequestHeader("token") String token) {
        //检查token是否过期
        boolean expiration = JwtHelper.isExpiration(token);
        if (expiration) {
            return Result.build(null, ResultCodeEnum.TOKEN_ERROR);
        }
        //从token中解析出用户id和用户类型
        Long userId = JwtHelper.getUserId(token);
        Integer userType = JwtHelper.getUserType(token);
        Map<String, Object> map = new LinkedHashMap<>();
        switch (userType) {
            case 1:
                Admin admin = adminService.getById(userId);
                map.put("userType", 1);
                map.put("user", admin);
                break;
            case 2:
                Student student = studentService.getById(userId);
                map.put("userType", 2);
                map.put("user", student);
                break;
            case 3:
                Teacher teacher = teacherService.getById(userId);
                map.put("userType", 3);
                map.put("user", teacher);
                break;
        }
        return Result.ok(map);
    }


    // /sms/system/headerImgUpload
    @ApiOperation("图片上传")
    @RequestMapping(value = "/headerImgUpload", method = RequestMethod.POST)
    public Result headerImgUpload(
            @ApiParam("头像文件")
            @RequestPart("multipartFile") MultipartFile multipartFile
    ) throws IOException {
        String uuid = UUID.randomUUID().toString().replace("-", "").toLowerCase();
        String originalFilename = multipartFile.getOriginalFilename();
        int index = originalFilename.lastIndexOf(".");
        String filename = uuid.concat(originalFilename.substring(index));
        //保存文件
        String portraitPath=
                "/Users/yimoorua/IdeaProjects/SmartCampusSystemDemo/target/classes/public/upload/"
                        .concat(filename);
        multipartFile.transferTo(new File(portraitPath));
        //响应图片的路径
        String path="upload/".concat(filename);
        return Result.ok(path);
    }


    // /sms/system/updatePwd/admin/123456
    @ApiOperation("修改密码的方法")
    @RequestMapping(value = "/updatePwd/{oldPwd}/{newPwd}",method = RequestMethod.POST)
    public Result updatePwd(
            @RequestHeader("token") String token,
            @PathVariable("oldPwd")String oldPwd,
            @PathVariable("newPwd")String newPwd
    ){
       boolean expiration=JwtHelper.isExpiration(token);
        if (expiration) {
            //token过期
            return Result.fail().message("token失效,请重新登录后修改密码");
        }
        //获取用户iD和类型
        Long userId =JwtHelper.getUserId(token);
        Integer userType =JwtHelper.getUserType(token);
        oldPwd=MD5.encrypt(oldPwd);
        newPwd=MD5.encrypt(newPwd);
        switch (userType){
            case 1:
                QueryWrapper<Admin> queryWrapper1=new QueryWrapper<>();
                queryWrapper1.eq("id",userId.intValue());
                queryWrapper1.eq("password",oldPwd);
                Admin admin=adminService.getOne(queryWrapper1);
                if(admin!=null){
                    //修改密码
                    admin.setPassword(newPwd);
                    adminService.saveOrUpdate(admin);
                }else {
                    return Result.fail().message("原密码有误，请重新修改");
                }
               break;
            case 2:
                QueryWrapper<Student> queryWrapper2=new QueryWrapper<>();
                queryWrapper2.eq("id",userId.intValue());
                queryWrapper2.eq("password",oldPwd);
                Student student=studentService.getOne(queryWrapper2);
                if(student!=null){
                    //修改密码
                    student.setPassword(newPwd);
                    studentService.saveOrUpdate(student);
                }else {
                    return Result.fail().message("原密码有误，请重新修改");
                }
                break;
            case 3:
                QueryWrapper<Teacher> queryWrapper3=new QueryWrapper<>();
                queryWrapper3.eq("id",userId.intValue());
                queryWrapper3.eq("password",oldPwd);
                Teacher teacher=teacherService.getOne(queryWrapper3);
                if(teacher!=null){
                    //修改密码
                    teacher.setPassword(newPwd);
                    teacherService.saveOrUpdate(teacher);
                }else {
                    return Result.fail().message("原密码有误，请重新修改");
                }
                break;
        }
        return Result.ok();
    }
}
