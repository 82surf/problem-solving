// 구명보트
// 시간초과

import java.util.*;
import java.util.stream.Collectors;

public class P42885 {
    public int solution(int[] people, int limit) {
        int answer = 0;
        List<Integer> peopleList = Arrays.stream(people).boxed().sorted(Comparator.naturalOrder()).collect(Collectors.toList());
        Deque<Integer> deque = new ArrayDeque<>(peopleList);

        while (!deque.isEmpty()) {
            if (deque.size() >= 2 && deque.getFirst() + deque.getLast() <= limit) {
                deque.removeFirst();
                deque.removeLast();
                answer += 1;
            } else {
                deque.removeLast();
                answer += 1;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        P42885 p = new P42885();
        int result = p.solution(new int[] {70, 80, 50}, 100);
        System.out.println(result);
    }
}
