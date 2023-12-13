// 카펫

import java.util.Arrays;

public class P42842 {
    public boolean isValid(int a, int b, int brown, int yellow) {
        return (a + 2) * (b + 2) == brown + yellow;
    }

    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int a = 1;
        while (a <= yellow) {
            if (yellow % a == 0) {
                int b = yellow / a;
                if (isValid(a, b, brown, yellow)) {
                    answer[0] = Math.max(a, b) + 2;
                    answer[1] = Math.min(a, b) + 2;
                    break;
                }
            }
            a += 1;
        }
        return answer;
    }

    public static void main(String[] args) {
        P42842 p = new P42842();
        int[] result = p.solution(24, 24);
        System.out.println(Arrays.toString(result));
    }
}
