public class Forloop{
    public static void main(String[] argv)
	{
       String s = "A test String for the switch!\n The second line of the test String."; 
       outer:for (int i = 0; i < s.length();i++){
            switch(s.charAt(i)){
                case '\n': break outer;
                case ' ': break;
                default: System.out.print(s.charAt(i));
            }
       }
	}
}
