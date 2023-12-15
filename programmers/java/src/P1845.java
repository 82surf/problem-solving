// 폰켓몬

import java.util.HashMap;

public class P1845 {
    public int solution(int[] nums) {
        int answer = 0;
        HashMap<Integer, Character> hashMap = new HashMap<>();
        for (int num : nums) {
            if (!hashMap.containsKey(num)) {
                hashMap.put(num, '1');
            }
        }

        answer = Math.min(nums.length / 2, hashMap.size());

        return answer;
    }

    public static void main(String[] args) {
        P1845 p = new P1845();
        int result = p.solution(new int[]{3, 3, 3, 2, 2, 4});
        System.out.println(result);
    }
}
