public class P12951 {
    public boolean isNumeric(String s) {
        try {
            Double.parseDouble(s);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    public String solution(String s) {
        String result = "";
        String[] strArr = s.split("");

        if (!isNumeric(strArr[0])) {
            result += strArr[0].toUpperCase();
        } else {
            result += strArr[0];
        }

        for (int i = 1; i < strArr.length; i++) {
            String before = strArr[i - 1];
            String curr = strArr[i];
            if (before.equals(" ")) {
                result += curr.toUpperCase();
            } else {
                result += curr.toLowerCase();
            }
        }

        return result;
    }

    public static void main(String[] args) {
        P12951 p = new P12951();
        String result = p.solution("for the last week");
        System.out.println(result);
    }
}
