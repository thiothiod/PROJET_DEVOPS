package com.example;

public class Main {
    public static void main(String[] args) {
        if (args.length != 3) {
            System.out.println("Utilisation : java -jar calculator.jar 10 + 5");
            return;
        }

        double a = Double.parseDouble(args[0]);
        String op = args[1];
        double b = Double.parseDouble(args[2]);

        Calculator calc = new Calculator();
        double result = 0;

        try {
            switch (op) {
                case "+": result = calc.add(a, b); break;
                case "-": result = calc.subtract(a, b); break;
                case "*": result = calc.multiply(a, b); break;
                case "/": result = calc.divide(a, b); break;
                default:
                    System.out.println("Opérateur invalide");
                    return;
            }
            System.out.println("Résultat : " + result);
        } catch (Exception e) {
            System.out.println("Erreur : " + e.getMessage());
        }
    }
}