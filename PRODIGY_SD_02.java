import java.util.Scanner;
import java.util.Random;

public class GuessingGame {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in); // Replaced the Scanner object with 's'
        Random random = new Random();
        int secretNumber = random.nextInt(100) + 1; // Generates a random number between 1 and 100
        int attempts = 0;
        
        System.out.println("Welcome to the Guessing Game!");
        System.out.println("I've picked a number between 1 and 100. Can you guess what it is?");
        
        while (true) {
            System.out.print("Enter your guess (or 'exit' to quit): ");
            String input = s.nextLine(); // Using 's' instead of 'scanner'
            
            if (input.equalsIgnoreCase("exit")) {
                System.out.println("Thanks for playing. Goodbye!");
                break;
            }
            
            int guess;
            try {
                guess = Integer.parseInt(input);
            } catch (NumberFormatException e) {
                System.out.println("Please enter a valid number.");
                continue;
            }
            
            attempts++;
            
            if (guess < secretNumber) {
                System.out.println("Too low! Try again.");
            } else if (guess > secretNumber) {
                System.out.println("Too high! Try again.");
            } else {
                System.out.println("Congratulations! You guessed it right in " + attempts + " attempts.");
                break;
            }
        }
        
        s.close(); // Closing the 's' Scanner object
    }
}
