public class BullsCows{
    public String getHint(String secret, String guess){
        if (secret == null || secret.length() == 0)
        {
            return "0A0B";
        }

        int bull = 0;
        int total = 0;
        char[] sChar = secret.toCharArray();
        char[] gChar = guess.toCharArray();
        int[] flags = new int[10];

        for (char c : sChar)
        {
            flags[c - '0']++;
        }

        for (int i = 0; i < sChar.length; i++)
        {
            if (gChar[i] == sChar[i])
            {
                bull++;
            }

            if (flags[gChar[i] - '0']-- > 0)
            {
                total++;
            }
        }

        return bull + "A" + (total - bull) + "B";
    }

    public static void main(String[] argv){
        BullsCows sol = new BullsCows();
        System.out.println(sol.getHint("1123", "0111"));
	}
}
