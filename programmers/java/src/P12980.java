// 점프와 순간 이동

public class P12980 {
    public int solution(int n) {
        int answer = 0;
        while (n > 0) {
            if (n % 2 == 0) {
                n /= 2;
            } else {
                n -= 1;
                answer += 1;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        P12980 p = new P12980();
        int result = p.solution(5000);
        System.out.println(result);
    }
}
