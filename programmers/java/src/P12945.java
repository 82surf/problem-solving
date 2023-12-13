import java.util.Arrays;

public class P12945 {
    int[] memo = new int[100001];

    public int fibonacci(int n) {
        if (n < 2) {
            return n;
        } else if (memo[n] != 0) {
            return memo[n];
        } else {
            int val = fibonacci(n - 1) + fibonacci(n - 2);
            memo[n] = val % 1234567;
            return memo[n];
        }
    }

    public int solution(int n) {
        return fibonacci(n);
    }

    public static void main(String[] args) {
        P12945 p = new P12945();
        int answer = p.solution(5);
        System.out.println(answer);
    }
}
