class Solution {
    public String longestPalindrome(String s) {
        if (s.length() == 0) return "";
        if (s.length() == 2 && s.charAt(0) == s.charAt(1)) return s;
        String answer = Character.toString(s.charAt(0));
        for (int i=1; i < s.length(); i++) {
            System.out.println(i);
            if (i < s.length()-1 && s.charAt(i-1) == s.charAt(i+1)) {
                String result = longestAt(s, i, true);
                if (result.length() > answer.length()) answer = result;
            }
            if (s.charAt(i-1) == s.charAt(i)) {
                String result = longestAt(s, i, false);
                if (result.length() > answer.length()) answer = result;
            }
        }
        return answer;
    }
    
    private String longestAt(String s, int i, boolean odd) {
        int end = i;
        if (odd) {
            end++;
        }
        int start = i-1;
        while (start >= 0 && end < s.length() && s.charAt(start) == s.charAt(end)) {
            start--;
            end++;
        }
        return s.substring(start+1, end);
    }
}
