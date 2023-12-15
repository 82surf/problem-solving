// 의상

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class P42578 {
    public int solution(String[][] clothes) {
        // 옷 종류별 개수 세기
        HashMap<String, Integer> hashMap = new HashMap<>();
        for (String[] cloth : clothes) {
            String category = cloth[1];
            if (hashMap.containsKey(category)) {
                hashMap.put(category, hashMap.get(category) + 1);
            } else {
                hashMap.put(category, 1);
            }
        }

        // 경우의 수 계산
        int answer = 1;
        List<Integer> categoryCntArr = new ArrayList<>(hashMap.values());
        for (int cnt : categoryCntArr) {
            answer *= cnt + 1;
        }
        return answer - 1;
    }

    public static void main(String[] args) {
        P42578 p = new P42578();
        int result = p.solution(new String[][]{{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}});
        System.out.println(result);
    }
}
