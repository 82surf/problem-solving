import java.util.Arrays;

public class P70129 {
    public int[] solution(String s) {
        String tmp = s;
        int iterateCnt = 0;
        int total0 = 0;
        while (!tmp.equals("1")) {
            int cnt1 = 0;
            for (int i = 0; i < tmp.length(); i++) {
                if (tmp.charAt(i) == '1') {
                    cnt1 += 1;
                }
            }

            total0 += tmp.length() - cnt1;
            iterateCnt++;
            tmp = Integer.toBinaryString(cnt1);
        }
        return new int[]{ iterateCnt, total0 };
    }

    public static void main(String[] args) {
        P70129 p = new P70129();
        int[] answer = p.solution("110010101001"	);
        System.out.println(Arrays.toString(answer));
    }
}
