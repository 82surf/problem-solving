// 전화번호 목록

import java.util.Arrays;
import java.util.HashMap;

public class P42577 {
    private HashMap<String, Character> hashMap = new HashMap<>();

    public boolean hasPrefix(String phoneNumber) {
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < phoneNumber.length(); i++) {
            char c = phoneNumber.charAt(i);
            stringBuilder.append(c);
            if (hashMap.containsKey(stringBuilder.toString())) {
                return true;
            }
        }
        return false;
    }

    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);
        for (String phoneNumber : phone_book) {
            if (hasPrefix(phoneNumber)) {
                return false;
            }
            hashMap.put(phoneNumber, '1');
        }
        return true;
    }

    public static void main(String[] args) {
        P42577 p = new P42577();
        boolean result = p.solution(new String[]{"119", "97674223", "1195524421"});
        System.out.println(result);
    }
}
