package dev.profitsoft.intern.controller;

import dev.profitsoft.intern.model.User;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.model;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.view;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@AutoConfigureMockMvc
public class HelloControllerTest {

    private final MockMvc mockMvc;

    @Autowired
    public HelloControllerTest(MockMvc mockMvc) {
        this.mockMvc = mockMvc;
    }

    @Test
    public void showHelloPage() throws Exception {
        User authUser = new User("roma", "123", "Roma");

        this.mockMvc.perform(get("/hello").sessionAttr("authUser", authUser))
                .andExpect(status().isOk())
                .andExpect(model().attribute("authUser", authUser))
                .andExpect(view().name("hello"));
    }

}