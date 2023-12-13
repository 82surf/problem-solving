// 다음 큰 숫자
public class P12911 {
    public int countBinary1(int n) {
        String binaryN = Integer.toBinaryString(n);
        int cnt = 0;
        for (int i = 0; i < binaryN.length(); i++) {
            char c = binaryN.charAt(i);
            if (c == '1') {
                cnt += 1;
            }
        }
        return cnt;
    }

    public int solution(int n) {
        int cntN = countBinary1(n);

        int answer = n;
        while (true) {
            answer += 1;
            int cntAnswer = countBinary1(answer);
            if (cntAnswer == cntN) {
                return answer;
            }
        }
    }

    public static void main(String[] args) {
        P12911 p = new P12911();
        int answer = p.solution(15);
        System.out.println(answer);
    }
}
