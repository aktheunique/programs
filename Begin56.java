import java.util.Scanner;
public class Begin56
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
	    String str=sc.next();
	    int flag=0;
	    for(int i=0;i<str.length();i++){
	        while(Character.isDigit(str.charAt(i))){
	            flag=1;
	            break;
	        }
	    }
	    System.out.println(flag==1?"Yes":"No");
	}
}
