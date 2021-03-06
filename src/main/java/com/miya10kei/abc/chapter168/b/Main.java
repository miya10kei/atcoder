package com.miya10kei.abc.chapter168.b;

import java.io.PrintWriter;
import java.util.Scanner;

import static java.lang.Integer.parseInt;

/**
 * ... (Triple Dots).
 */
public class Main {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var k = parseInt(sc.next());
        var s = sc.next();

        var writer = new PrintWriter(System.out);
        if (s.length() <= k) {
            writer.print(s);
        } else {
            writer.print(s.substring(0, k));
            writer.print("...");
        }
        writer.flush();
    }
}
