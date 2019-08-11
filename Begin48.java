import java.util.Scanner;
public class Begin48
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
	    int number=sc.nextInt();
	    int arr[]=new int[number];
	    int sum=0;
	    for(int i=0;i<number;i++){
	        arr[i]=sc.nextInt();
	    }
	    for(int j=0;j<number;j++){
	        sum=sum+arr[j];
	    }
	    System.out.print(sum/number);
	}
}
