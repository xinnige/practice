import java.util.Scanner;
import java.util.Random;
//import java.util.;


public class guessNumber{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		String input;
        Random random = new Random();
        int answer = random.nextInt(100);
        int counter = 0;
        int guess;
        while (true){
			System.out.print("Please enter the number you guess (\"quit\" to quit):");
			input = in.nextLine();
            if (input.toLowerCase().equals("quit")){
				System.out.println("\tGoodbye~");
				break;
			}
			
			try{
				guess = Integer.parseInt(input);
				counter++;
			} catch (NumberFormatException ex){
				System.out.println("\tPlease enter a positive integer!");
				continue;
			}
	
			if(guess == answer){
				System.out.println("Bingo! Guessed in "+counter+" times!");
				break;
			}else if(guess < answer){
				System.out.println("Guess a larger number!");
			}else{
				System.out.println("Guess a smaller number!");
			}
		}
	}
}
