package Revise;

import java.util.Scanner;

public class numpali
{

	public static void main(String[] args) {
   System.out.println("enter num");
Scanner in=new Scanner (System.in);
int num=in.nextInt();
int n=num;
 System.out.println(5%10);
int rev=0,rmd;
//while(num>0) {
	rmd=num%10;
	rev=rev*10+rmd;
	num=num/10;
//}
if(rev==n)
	System.out.println("is pali");
else
	System.out.println("no pali");
}
	}
//

