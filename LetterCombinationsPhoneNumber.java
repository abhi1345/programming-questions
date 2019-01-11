class Solution {
    public List<String> letterCombinations(String digits) {
        Map<Integer, String> trans = new HashMap<Integer, String>()
        {{
                put(2, "abc");
                put(3, "def");
                put(4, "ghi");
                put(5, "jkl");
                put(6, "mno");
                put(7, "pqrs");
                put(8, "tuv");
                put(9, "wxyz");
            }};
        String[] digitlist = digits.split("");
        List<String> answer = new LinkedList<String>();
        if (digits.length() == 0) return answer;
        answer.add("");
        for (int i=0; i<digits.length(); i++) {
            List<String> temp = new LinkedList<String>();
            String chars = trans.get(Character.getNumericValue(digits.charAt(i)));
            for (int c=0; c<chars.length(); c++) {
                for (int j=0; j<answer.size(); j++) {
                    temp.add(answer.get(j) + chars.substring(c, c+1));
                }
            }
            answer = temp;
        }        
        return answer;
    }
}
