import java.util.Scanner;
public class Begin62
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
	    String str=sc.next();
	    int flag=0;
	    char arr[]=str.toCharArray();
	    for(int i=0;i<arr.length;i++){
	        if(arr[i]=='0'|| arr[i]=='1'){
	            flag=1;
	        }
	        else{
	            flag=0;
	        }
	    }
	    System.out.println(flag==1?"yes":"no");
	}
}
