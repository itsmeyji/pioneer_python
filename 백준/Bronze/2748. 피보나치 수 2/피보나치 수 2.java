import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        long result = bottomUp(n);
        System.out.println(result);
    }

    public static long bottomUp(int n){
        if (n == 0) return 0;
        if (n == 1) return 1;

        long[] table = new long[n + 1];
        table[0] = 0;
        table[1] = 1;

        for (int i = 2; i <= n; i++) {
            table[i] = table[i - 2] + table[i - 1];
        }

        return table[n];
    }
}
