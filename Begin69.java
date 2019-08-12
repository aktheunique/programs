import java.util.Scanner;
public class Begin69
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
	    int n1=sc.nextInt();
	    int n2=sc.nextInt();
		System.out.println(Math.abs(n1+n2)%2==0?"even":"odd");
	}
}
