import java.util.Arrays;
import java.util.Collections;

public class P12941 {
    public int solution(int[] A, int[] B) {
        Arrays.sort(A);
        Arrays.sort(B);

        int answer = 0;
        for (int i = 0; i < A.length; i++) {
            answer += A[i] * B[B.length - i - 1];
        }
        return answer;
    }

    public static void main(String[] args) {
        P12941 p = new P12941();
        int answer = p.solution(new int[]{1, 4, 2}, new int[]{5, 4, 4});
        System.out.println(answer);
    }
}
