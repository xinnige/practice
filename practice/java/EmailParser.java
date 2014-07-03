public class EmailParser{
	private String firstName;
	private String lastName;
	private String company;
	private String emailAddress;

	public EmailParser(String address)
	{
		if(!address.matches("[a-zA-Z]+\\.[a-zA-Z]+@[a-zA-Z]+\\.org")){
			System.out.println("Address is not valid!");
			System.exit(0);
		}
		emailAddress = address;
		firstName = "";
		lastName = "";
        company = "";
		parse();
		format();
	}

	public void parse(){
		if (emailAddress.length() == 0){
			System.out.println("Email Address is empty!");
			return;
		}
		String[] strarr = emailAddress.split("@");
        String[] names = strarr[0].split("\\.");
		firstName = names[0].toLowerCase();
		lastName = names[1].toLowerCase();
		company = strarr[1].split("\\.")[0];
	}

    public void format(){
		StringBuilder capLastName = new StringBuilder();
		capLastName.append(lastName.substring(0,1).toUpperCase());
		capLastName.append(lastName.substring(1));
		lastName = capLastName.toString();
	}

	public String getLastName(){
		return lastName;
	}
	public String getFirstName(){
		return firstName;
	}
	public String getCompany(){
		return company;
	}
	public String getEmailAddress(){
		return emailAddress;

	}

	public static void main(String[] args){
		if (args.length == 0){
			System.out.println("Need an email address!");
		}
		String input = args[0];
        EmailParser ep = new EmailParser(input);
        System.out.println("Valid Email Address :"+ep.getEmailAddress());
		    
		System.out.println("The Name is "+ep.getLastName()+" "+ep.getFirstName());
        System.out.println("The company is "+ep.getCompany());


	}
}
