class Solution {
    public static boolean isNumber (String s) {
        if (s.contains("f")) {
            return false;
        }
        if (s.contains("D")) {
            return false;
        }
        try {
            Double.parseDouble(s);
        } catch (NumberFormatException e) {
            return false;
        }
        return true;
    }
}
