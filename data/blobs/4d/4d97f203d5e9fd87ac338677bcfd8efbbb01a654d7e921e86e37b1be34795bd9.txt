package org.example.app.controllers;

import org.example.app.service.UsersUpdateService;
import org.example.app.utils.AppStarter;
import org.example.app.views.UsersUpdateView;

public class UsersUpdateController {

    UsersUpdateService service;
    UsersUpdateView view;

    public UsersUpdateController(UsersUpdateService service, UsersUpdateView view) {
        this.service = service;
        this.view = view;
    }
    public void updateContact() {
        view.getOutput(service.updateUser(view.getData()));
        AppStarter.startApp();
    }
}
