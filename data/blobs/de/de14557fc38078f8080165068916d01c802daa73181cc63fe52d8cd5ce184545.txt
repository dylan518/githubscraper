package org.example.game;

import org.example.config.Config;
import org.example.config.GetConfig;
import org.example.config.SetConfig;
import org.example.service.View;

import java.util.Scanner;

public class App {

    Scanner scan = new Scanner(System.in);
    Config config = new Config();
    View view = new View();
    String path = "/home/vildan/IdeaProjects/OOP_Java/Candy/src/main/resources/data.json";
    boolean flag = true;

    public void app(){
        System.out.println("/////////////////////////////////");
        System.out.println("1/New game\n2/Start game\n3/Configuration\n4/Load game\n5/Quit");
        System.out.println("Choose item: ");


        while(flag){
            String number = scan.nextLine();

            switch (number){
                case("1") -> {
                    Game newGame = new Game();
                    newGame.game(new Config(), new View());
                    app();
                }
                case("2") -> {
                    Game game = new Game();
                    game.game(config, view);
                    app();
                }
                case("3") -> {
                    GetConfig manualConfig = new GetConfig();
                    manualConfig.getConfig();
                    SetConfig newConfig = new SetConfig();
                    config = newConfig.setConfig(manualConfig.getHashMap());
                    app();

                }
                case("4") -> {
                    LoadGame load = new LoadGame();
                    load.readJson(path);
                    SetConfig newConfig = new SetConfig();
                    config = newConfig.setConfig(load.getMap());
                    app();

                }
                case("5") -> flag = false;
                default -> System.out.println(view.error());
            }
        }



    }
}
