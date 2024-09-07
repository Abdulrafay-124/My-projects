import java.util.Scanner;

public class A1Q4 {
    
    public static void main(String[] args){
    Scanner scanner = new Scanner(System.in);
    
    int num1;
    int num2;
    int num3;
    System.out.println("Input the first number: ");
    num1 = scanner.nextInt();
    System.out.println("Input the second number: ");
    num2 = scanner.nextInt();
    
    System.out.println("Input the third number: ");
    num3 = scanner.nextInt();
    if (num1 < num2 && num2 < num3){
        System.out.println("True");
    }
    else{
        System.out.println("False");
    }
    }
}
 
