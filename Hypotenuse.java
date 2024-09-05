import java.util.Scanner;

public class Hypotenuse {

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter side x value: ");

        double x = scanner.nextDouble();

        System.out.println("Enter side y value: ");

        double y = scanner.nextDouble();

        double z = Math.sqrt((x*x)+(y*y));

        System.out.println("Hypotenuse of the Triangle is "+ z);

        scanner.close();

    }
    
}
