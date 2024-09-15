import java.util.Scanner;

public class BrickWallCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the width of the brick in inches: ");
        double brickWidth = scanner.nextDouble();
        System.out.print("Enter the length of the brick in inches: ");
        double brickLength = scanner.nextDouble();
        System.out.print("Enter the height of the brick in inches: ");
        double brickHeight = scanner.nextDouble();
        double brickVolume = brickWidth * brickLength * brickHeight;
        System.out.println("The volume of the brick is: " + brickVolume + " cubic inches");
        double wallWidthInches = 25 * 12;  
        double wallHeightInches = 10 * 12; 
        double brickWidthWithCement = brickWidth + 1;    
        double brickHeightWithCement = brickHeight + 1;  
        double wallArea = wallWidthInches * wallHeightInches;  
        double brickFaceArea = brickWidthWithCement * brickHeightWithCement; 
        int numberOfBricks = (int) Math.ceil(wallArea / brickFaceArea);
        System.out.println("The number of bricks needed to build the wall is: " + numberOfBricks + " bricks");
    }
}
