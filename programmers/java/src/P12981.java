// 영어 끝말잇기

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class P12981 {
    public Map<String, Character> memo = new HashMap<>();

    public boolean isValid(String before, String curr) {
        return before.charAt(before.length() - 1) == curr.charAt(0);
    }

    public int[] solution(int n, String[] words) {
        int[] answer = {0, 0};
        memo.put(words[0], '1');

        for (int i = 1; i < words.length; i++) {
            String curr = words[i];
            if (!memo.containsKey(curr) && isValid(words[i - 1], curr)) {
                memo.put(curr, '1');
            } else {
                answer[0] = i % n + 1;
                answer[1] = i / n + 1;
                break;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        P12981 p = new P12981();
        int[] result = p.solution(3, new String[]{"tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"});
        System.out.println(Arrays.toString(result));
    }
}
