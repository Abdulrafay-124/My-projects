import java.util.Scanner;


public class A1Q2 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Input First Number : ");

        int num1 = scanner.nextInt();

        System.out.println("Input Second Number : ");

        int num2 = scanner.nextInt();

        int sum = num1 + num2;
        int difference = num1 - num2;
        int product = num1 * num2;
        int quotient = num1 / num2;
        int remainder = num1 % num2;

        System.out.println("Sum>  "+ num1 + " + " + num2 + " = " + sum);
        System.out.println("Difference> " + num1 + " - " + num2 + " = " + difference);
        System.out.println("Product> "+ num1 + " x " + num2 + " = " + product);
        System.out.println("Quotient> " + num1 + " / " + num2 + " = " + quotient);
        System.out.println("Remainder> "+ num1 + " % " + num2 + " = " + remainder);
       
        
    }


    
}
