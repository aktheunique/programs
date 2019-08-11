import java.util.Scanner;
public class Begin58
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
	    int n=sc.nextInt();
	    int k=sc.nextInt();
	    int flag=0;
	    int arr[]=new int[n];
	    for(int i=0;i<n;i++){
	        arr[i]=sc.nextInt();
	    }
	    for(int j=0;j<n;j++){
	        if(k==arr[j]){
	            flag=1;
	        }
	        else{
	            continue;
	        }
	    }
	    System.out.println(flag==1?"yes":"no");
	}
}
