package com.newland.socket.controller;

import com.newland.socket.model.User;
import com.newland.socket.server.WebSocketServer;
import jakarta.websocket.Session;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;
import java.util.concurrent.ConcurrentHashMap;

@Controller
public class ChatController {
    @RequestMapping("/onlineusers")
    @ResponseBody
    public Set<String> onlineusers(@RequestParam("currentuser") String currentuser) {
        ConcurrentHashMap<String, Session> map = WebSocketServer.getSessionPools();
        Set<String> set = map.keySet();
        Iterator<String> it = set.iterator();
        Set<String> nameset = new HashSet<String>();
        while (it.hasNext()) {
            String entry = it.next();
            if (!entry.equals(currentuser)) {
                nameset.add(entry);
            }
        }
        return nameset;
    }


    @RequestMapping("getuid")
    @ResponseBody
    public User getuid(@RequestParam("username") String username) {
        User u = new User();
        u.setName(username);
        u.setUid(1L);
        return u;
    }
}
