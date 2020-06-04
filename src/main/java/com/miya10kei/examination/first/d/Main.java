package com.miya10kei.examination.first.d;

import java.io.PrintWriter;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());

        int[] array = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            int a = Integer.parseInt(sc.next());
            array[a]++;
        }

        int before = 0, after = 0;
        for (int i = 1; i <= n; i++) {
            int count = array[i];
            if (count == 0) {
                after = i;
            } else if (count == 2) {
                before = i;
            }
            if (before != 0 && after != 0) {
                break;
            }
        }

        PrintWriter writer = new PrintWriter(System.out);
        if (before == 0) {
            writer.print("Correct");
        } else {
            writer.print(before);
            writer.print(" ");
            writer.print(after);
        }
        writer.flush();
    }
}
