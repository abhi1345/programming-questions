class Solution {
    public List<String> fizzBuzz(int n) {
        
        List<String> answer = new ArrayList<String>();
        
        for (int i = 0; i < n; i++) {
            int num = i + 1;
            if (num % 15 == 0) {
                answer.add("FizzBuzz");
            } else if (num % 5 == 0) {
                answer.add("Buzz");
            } else if (num % 3 == 0) {
                answer.add("Fizz");
            } else {
                answer.add(Integer.toString(num));
            }
        }
        
        return answer;
    }
    
}
