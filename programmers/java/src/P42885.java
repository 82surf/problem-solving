// 구명보트

import java.util.*;
import java.util.stream.Collectors;

public class P42885 {
    public int solution(int[] people, int limit) {
        int answer = 0;

        Arrays.sort(people);
        int left = 0;
        int right = people.length - 1;

        while (left <= right) {
            int minVal = people[left];
            int maxVal = people[right];
            int diff = right - left;

            if (diff >= 1 && minVal + maxVal <= limit) {
                left += 1;
            }
            right -= 1;
            answer += 1;
        }

        return answer;
    }

    public static void main(String[] args) {
        P42885 p = new P42885();
        int result = p.solution(new int[] {70, 80, 50}, 100);
        System.out.println(result);
    }
}
