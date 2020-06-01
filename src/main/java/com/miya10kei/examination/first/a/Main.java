package com.miya10kei.examination.first.a;

import java.io.PrintWriter;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();

        PrintWriter writer = new PrintWriter(System.out);
        try {
            writer.print(Integer.parseInt(s) * 2);
        } catch (NumberFormatException e) {
            writer.print("error");
        }
        writer.flush();
    }
}
