public class Codec {
    // Encodes a list of strings to a single string.
    public static String encode(List<String> strs) {
        String answer = "";
        for (String s : strs) {
            answer += Integer.toString(s.length()) + "/" + s;
        }
        return answer;
    }

    // Decodes a single string to a list of strings.
    public static List<String> decode(String s) {
        int i=0;
        List<String> answer = new LinkedList<String>();
        while (i < s.length()) {
            String numcharsstr = "";
            while (s.charAt(i) != '/') {
                numcharsstr += s.charAt(i);
                i++;
            }
            System.out.println(numcharsstr);
            int numchars = Integer.valueOf(numcharsstr);
            i++;
            String curr = s.substring(i, i+numchars);
            i += numchars;
            answer.add(curr);
        }
        return answer;
    }
}
