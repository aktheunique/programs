import java.util.Scanner;
public class Begin42
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
	    String s1=sc.nextLine();
	    String s2=sc.nextLine();
		if(s1.compareTo(s2)>0){
		    System.out.println(s1);
		}
		else if(s1.compareTo(s2)<0){
		    System.out.println(s2);
		}
		else{
		    System.out.println(s1);
		}
	}
}
