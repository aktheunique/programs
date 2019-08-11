import java.util.Scanner;
public class Begin53
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
	    int number=sc.nextInt();
	    int sum=0;
	    while(number>0){
	        sum=sum+(number%10);
	        number=number/10;
	    }
	    System.out.println(sum);
	}
}
