package com.miya10kei.examination.first.b;

import java.io.PrintWriter;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        PrintWriter writer = new PrintWriter(System.out);
        int prev = sc.nextInt();
        for (int i = 0; i < n - 1; i++) {
            int next = sc.nextInt();
            if (prev < next) {
                writer.print("up ");
                writer.println(next - prev);
            } else if (prev > next) {
                writer.print("down ");
                writer.println(prev - next);
            } else {
                writer.println("stay");
            }
            prev = next;
        }
        writer.flush();
    }
}
