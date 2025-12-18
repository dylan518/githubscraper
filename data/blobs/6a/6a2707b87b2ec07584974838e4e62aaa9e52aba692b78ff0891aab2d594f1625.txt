package com.example.reactProject.controller;

import com.example.reactProject.entity.User;
import com.example.reactProject.service.UserService;
import lombok.RequiredArgsConstructor;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.util.List;
import java.util.Objects;


@RestController			// rendering 하지 않고, 데이터를 보내는 컨트롤러 (@ResponseBody 느낌)
@RequestMapping("/react")
@RequiredArgsConstructor
public class ReactController {
    private final UserService uSvc;

    @GetMapping("/data")
    public String data() {
        return "스프링부트에서 보낸 데이터";
    }

//    @GetMapping("/json")       //@GetMapping("/json")
//   public String json() {
//        List<User> userList = uSvc.userList();
//        JSONArray jArr = new JSONArray(); // 자동차 싣는 트럭
//
////        for(int i = 0; i < userList.size(); i++){
////            System.out.println(userList.get(i).getUid());
////        }
////          for(Object obj : userList){
////              System.out.println(obj).getUid());
////          }
//
//        for (User i : userList){
//            JSONObject Obj = new JSONObject();// 자동차 프레임
//            Obj.put("uid", i.getUid());
//            Obj.put("uname", i.getUname());
//            Obj.put("email", i.getEmail());
//            Obj.put("github", i.getGithub());
//            Obj.put("insta", i.getInsta());
//
//            jArr.add(Obj);
//        }
//       return jArr.toJSONString();
//
//    }

    @GetMapping("/users")       //@GetMapping("/json")
    public String user() {
        List<User> userList = uSvc.userList();
        JSONArray jArr = new JSONArray(); // 자동차 싣는 트럭

//        for(int i = 0; i < userList.size(); i++){
//            System.out.println(userList.get(i).getUid());
//        }
//          for(Object obj : userList){
//              System.out.println(obj).getUid());
//          }

        for (User i : userList){
            JSONObject Obj = new JSONObject();// 자동차 프레임
            Obj.put("uid", i.getUid());
            Obj.put("uname", i.getUname());
            Obj.put("email", i.getEmail());
            Obj.put("github", i.getGithub());
            Obj.put("insta", i.getInsta());

            jArr.add(Obj);
        }
        return jArr.toJSONString();

    }
    @PostMapping("/form")
    public String form(String uid, String uname) {
        System.out.println("uid=" + uid + ", uname=" + uname);
        return "uid=" + uid + ", uname=" + uname;
    }

    @PostMapping("/multi")
    public String form(String uid, String uname, MultipartFile file) {
        String msg = "uid=" + uid + ", uname=" + uname + ", fname=" + file.getOriginalFilename();
        System.out.println(msg);
        return msg;
    }

}




















































