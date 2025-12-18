package ru.job4j.oop;

public class Error {
    private boolean active;
    private int status;
    private String message;

    public Error() {
    }

    public Error(boolean active, int status, String message) {
        this.active = active;
        this.status = status;
        this.message = message;
    }

    public void printError() {
        System.out.println("Активность: " + active);
        System.out.println("Статус ошибки: " + status);
        System.out.println("Сообщение об ошибке: " + message);
    }

    public static void main(String[] args) {
        Error errorDefault = new Error();
        errorDefault.printError();
        System.out.println("---------------------------------------");
        Error errorParametr = new Error(true, 1, "Программа прервана.");
        errorParametr.printError();
    }
}
