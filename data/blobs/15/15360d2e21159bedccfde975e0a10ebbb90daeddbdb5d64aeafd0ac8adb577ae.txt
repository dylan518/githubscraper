/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejercicio1;

/**
 * Ejercicio1-Desenvolupa un programa que demani un número i digui si és major
 * que 100.
 *
 *
 * @author Aaron Monterroso Segura
 */

import java.util.Scanner;

public class BankATM {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String cardNum = "6228123123"; // número de tarjeta
        int pwd = 888888; // contraseña
        boolean flag = true; // declara una variable booleana
        double surplus = 1000;// balance

        // interfaz
        System.out.println("--------- Bienvenido al cajero automático de ICBC ---------");

//        / ** Limita el número de inicios de sesión ** /
        for (int i = 1; i <= 3; i++) {
            System.out.println("Por favor inserte su tarjeta bancaria:");
            String inputCard = input.next();
            System.out.println("Por favor ingrese su contraseña:");
            int inputPwd = input.nextInt();

            // verificar cuenta y contraseña
            if (inputCard.equals(cardNum) && inputPwd == pwd) {
                flag = true;
                break;
            } else {
                if (i <= 2) {
                    System.out.println("Lo siento, la contraseña es incorrecta, aún tienes" + (3 - i) + "¡Segunda oportunidad!");
                } else {
                    System.out.println("Lo siento, tu tarjeta está bloqueada!");
                    break;
                }
                flag = false;
            }
        }

//        / ** Seleccione la función después de un inicio de sesión exitoso * /
        if (flag) {
            char answer = 's';
            while (answer == 's' || answer== 'S') {
                System.out.println("Seleccione una función: 1. Retirada 2. Depósito 3. Verificar saldo 4. Transferencia 5. Salir");
                int choice = input.nextInt();
                switch (choice) {
                    case 1:
                        // Realizar una operación de retirada
                        System.out.println("---> Retirada");
                        System.out.println("Ingrese el monto del retiro:");
                        double getMoney = input.nextDouble();
                        if (getMoney > 0) {
                            if (getMoney <= surplus) {
                                if (getMoney % 100 == 0) {
                                    System.out.println("¡Toma tu billete! El saldo es ￥" + (surplus - getMoney));
                                } else {
                                    System.out.println("Lo siento, ¡no puedo aceptar el cambio!");
                                }
                            } else {
                                System.out.println("Lo siento, el balance es insuficiente!");
                            }
                        } else {
                            System.out.println("Ingrese la cantidad correcta:");
                        }

                        break;
                    case 2:
                        // realiza la operación de depósito
                        System.out.println("---> Depósito");
                        System.out.println("Organice los billetes y póngalos en el puerto de depósito:");
                        double saveMoney = input.nextDouble();
                        if (saveMoney > 0 && saveMoney <= 10000) {
                            if (saveMoney % 100 == 0) {
                                surplus += saveMoney;
                                System.out.println("¡Depósito exitoso! El saldo es ￥" + surplus);
                            } else {

                                double backMoney = saveMoney % 100;
                                surplus = saveMoney + surplus - backMoney;
                                System.out.println("¡Depósito exitoso! El saldo es ￥" + surplus);
                                System.out.println("Por favor, quita el cambio ￥" + backMoney);
                            }
                        } else if (saveMoney > 10000) {
                            System.out.println("Deposite hasta 10,000 yuanes a la vez, ¡deposite en lotes!");
                        } else {
                            System.out.println("¡El billete depositado es un billete falsificado y no es válido y es confiscado!");
                        }
                        break;
                    case 3:
                        // ejecutar saldo de consulta
                        System.out.println("---> Consultar saldo");
                        System.out.println("El saldo de su tarjeta es:" + surplus);
                        break;
                    case 4:
                        // realiza la operación de transferencia
                        System.out.println("---> Transferencia");
                        System.out.println("Ingrese el monto de la transferencia:");
                        double goMoney = input.nextDouble(); // cantidad de transferencia
                        if (goMoney > 0) {
                            if (goMoney <= surplus) {
                                System.out.println("¡Transferencia exitosa! El balance es ￥" + (surplus - goMoney));
                            } else {
                                System.out.println("Lo siento, ¡asegúrate de tener suficiente saldo en la tarjeta!");
                            }

                        } else {
                            System.out.println("¡Transferencia fallida! Ingrese la cantidad correcta:");
                        }
                        break;
                    case 5:
                        // ejecuta la operación de salida
                        // System.out.println ("---> Salir");
                        System.out.println("¡Gracias por tu uso!");
                        return;
                    default:
                        System.out.println("Lo siento, ¡la función que seleccionó es incorrecta!");
                        break;
                }// switch end
                System.out.println("¿Continuar? S / n");
                answer = input.next().charAt(0);

            } // while end
            System.out.println("¡Gracias por tu uso!");

        }

    }
}
