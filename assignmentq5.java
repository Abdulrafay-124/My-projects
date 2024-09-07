import java.util.Scanner;

public class A1Q5 {
    
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Input the first number: ");
        int num1 = scanner.nextInt();
        System.out.println("Input the first number: ");
        int num2 = scanner.nextInt();
        int bigger = Math.max(num1,num2);
        int smaller = Math.min(num1,num2);
        int remainder1 = num1 % 6; 
        int remainder2 = num2 % 6; 
        if (num1 == num2){
            System.out.println("result = " + 0);
        }
        else if (remainder1 == remainder2){
            
            System.out.println("result = " + smaller);
        }
        else if (num1 == bigger){
            
            System.out.println("1st number is bigger = "+ num1);
        }
        else if (num2 == bigger){
            
            System.out.println("2nd number is bigger = "+ num2);
        }
        
