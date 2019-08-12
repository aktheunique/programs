mport java.util.Scanner;
public class Begin71
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
	    String str=sc.next();
        StringBuilder sb=new StringBuilder();
        sb.append(str);
        sb=sb.reverse();
		System.out.println(sb.toString().equals(str)?"yes":"no");
	}
}
