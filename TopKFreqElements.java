class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        Map <Integer, Integer> hm = new HashMap<Integer, Integer>();
        
        int n = nums.length;
        
        for (int i = 0; i < n; i++) {
            if (hm.containsKey(nums[i])){
                hm.put(nums[i], hm.get(nums[i])+1);
            }
            
            else {
                hm.put(nums[i], 1);
            }
        }
        
        
        
        List answers = new ArrayList<Integer>();
        
        LinkedHashMap<Integer, Integer> reverseSortedMap = new LinkedHashMap<>();
 
        hm.entrySet()
            .stream()
            .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
            .forEachOrdered(x -> reverseSortedMap.put(x.getKey(), x.getValue()));

        List checker = new ArrayList(reverseSortedMap.keySet());
        
        for (int i = 0; i < k; i++) {
            answers.add(checker.get(i));
        
        }
        return answers;
        
        
    }
}
