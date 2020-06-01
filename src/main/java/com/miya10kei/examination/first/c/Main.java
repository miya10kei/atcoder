package com.miya10kei.examination.first.c;

import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] values = new int[6];
        for (int i = 0; i < 6; i++) {
            values[i] = Integer.parseInt(sc.next());
        }
        Arrays.sort(values);
        PrintWriter writer = new PrintWriter(System.out);
        writer.println(values[3]);
        writer.flush();
    }
}
