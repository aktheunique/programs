import java.util.Scanner;
public class Begin57
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
	    int n=sc.nextInt();
	    int k=sc.nextInt();
	    int count=0;
	    int arr[]=new int[n];
	    for(int i=0;i<n;i++){
	        arr[i]=sc.nextInt();
	    }
	    for(int j=0;j<n;j++){
	        if(k==arr[j]){
	            count+=1;
	        }
	        else{
	            continue;
	        }
	    }
	    System.out.println(count);
	}
}
