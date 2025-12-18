package org.javaacademy.homeworks.module1.homework2.office;

public class Office {

    private final Boss boss;
    private final Manager manager;
    private final Secretary secretary;
    private final Security security;

    public Office(Boss boss, Manager manager, Secretary secretary, Security security) {
        this.boss = boss;
        this.manager = manager;
        this.secretary = secretary;
        this.security = security;
    }

    public void workDay() {
        boss.customize(manager);
        manager.scream();
        security.ask();
        secretary.solveProblems(boss, manager, security);
    }
}
