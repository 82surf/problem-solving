// 짝지어 제거하기

import java.util.ArrayDeque;
import java.util.Deque;

public class P12937 {
    public int solution(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (stack.isEmpty()) {
                stack.add(c);
            } else if (stack.getLast() == c) {
                stack.removeLast();
            } else {
                stack.add(c);
            }
        }
        return stack.isEmpty() ? 1 : 0;
    }

    public static void main(String[] args) {
        P12937 p = new P12937();
        int result = p.solution("baabaa");
        System.out.println(result);
    }
}
