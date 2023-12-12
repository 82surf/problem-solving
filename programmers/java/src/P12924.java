// Lv2 숫자의 표현
public class P12924 {
    public int solution(int n) {
        int answer = 0;
        float c = 1;
        while (true) {
            float a = ((n * 2 / c) - (c - 1)) / 2;
            if (a <= 0) {
                break;
            } else if (a - (int) a == 0) {
                answer += 1;
            }
            c += 1;
        }
        return answer;
    }

    public static void main(String[] args) {
        P12924 p = new P12924();
        int answer = p.solution(15);
        System.out.println(answer);
    }
}
