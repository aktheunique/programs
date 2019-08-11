import java.util.Scanner;
public class Begin66
{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n1=sc.nextInt();
		int flag=0;
		for(int i=2;i<n1/2;i++){
		    if(n1%i==0){
		        flag=1;
		        break;
		    }
		}
		System.out.println(flag==0?"yes":"no");
	}
}
