import java.util.Arrays;

/**
 * Date: 2023.11.14
 * Title: 최댓값과 최솟값
 * Level: 2
 * Link: https://school.programmers.co.kr/learn/courses/30/lessons/12939?language=java
 */

public class P12939 {
    public String solution(String s) {
        String[] strNumArr = s.split(" ");
        int[] nums = Arrays.stream(strNumArr).mapToInt(Integer::parseInt).toArray();
        int min = Arrays.stream(nums).min().getAsInt();
        int max = Arrays.stream(nums).max().getAsInt();
        return String.format("%d %d", min, max);
    }
}
