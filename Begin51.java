import java.util.Scanner;
import java.util.Stack;
public class Begin51
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
	    int number=sc.nextInt();
	    Stack<Integer> list=new Stack<Integer>();
	    while(number>0){
	        list.push(number%10);
	        number=number/10;
	    }
	    while(!list.isEmpty()){
	        System.out.print(list.pop()+" ");
	    }
	}
}
