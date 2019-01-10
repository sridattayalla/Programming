package com.company;
import java.math.*;
import java.util.Scanner;

public class Main {
    static int exp_op;
    static int pow;

    public static void main(String[] args) {
	    Scanner scanner = new Scanner(System.in);
	    exp_op = scanner.nextInt();
	    pow = scanner.nextInt();

	    System.out.print(rec(exp_op, 1));
    }

    static int rec(int total, int i){
        if ( total == 0){
            return 1;
        }
        int sum = 0;
        int j = i;
        while ( Math.pow(j, pow) <= total ){
            sum = sum + rec(total - (int)Math.pow(j, pow), j + 1);
            j++;
        }
        return sum;
    }
}
