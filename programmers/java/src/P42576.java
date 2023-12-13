// 완주하지 못한 선수

import java.util.Collection;
import java.util.HashMap;

public class P42576 {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Number> count = new HashMap<>();
        for (String name : participant) {
            if (count.containsKey(name)) {
                count.put(name, (int) count.get(name) + 1);
            } else {
                count.put(name, 1);
            }
        }

        for (String name : completion) {
            count.put(name, (int) count.get(name) - 1);
            if ((int) count.get(name) == 0) {
                count.remove(name);
            }
        }

        Collection<String> keys = count.keySet();
        String[] result = keys.toArray(new String[0]);

        return result[0];
    }

    public static void main(String[] args) {
        P42576 p = new P42576();
        String result = p.solution(new String[]{"mislav", "stanko", "mislav", "ana"}, new String[] {"stanko", "ana", "mislav"});
        System.out.println(result);
    }
}
