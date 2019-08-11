import java.util.Scanner;
public class Begin44
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
	    int arr[]={1,2,3,4,5,6,7,8,9,10};
	    int number=sc.nextInt();
	    int flag=0;
	    for(int i=0;i<arr.length;i++){
	        if(number==arr[i]){
	            flag=1;
	            break;
	        }
	    }
	    if(flag==1){
	        System.out.println("yes");
	    }
	    else{
	        System.out.println("no");
	    }
	}
}
