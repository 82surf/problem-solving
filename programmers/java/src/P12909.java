import java.util.Stack;

public class P12909 {
    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack.push(c);
            } else {
                if (stack.empty()) {
                    return false;
                }
                stack.pop();
            }
        }
        return stack.empty();
    }

    public static void main(String[] args) {
        P12909 p = new P12909();
        boolean answer = p.solution("(())()");
        System.out.println(answer);
    }
}
