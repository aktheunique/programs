import java.util.Scanner;
public class Begin61
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
	    String str=sc.next();
	    char arr[]=str.toCharArray();
	    int number=sc.nextInt();
	    for(int i=0;i<number;i++){
	        System.out.print(arr[i]+"");
	    }
	}
}
