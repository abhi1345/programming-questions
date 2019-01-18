public class ZigzagIterator {
    private List<Integer> i, j;
   
    public ZigzagIterator(List<Integer> v1, List<Integer> v2) {
        if (v1.size() == 0) {
            i = v2; j = v1;
        } else {
            i = v1; 
            j = v2;
        }
    }

    public int next() {
        int output = i.get(0);
        i.remove(0);
        if (j.size() > 0) {
            List<Integer> tmp = i;
            i = j;
            j = tmp;
        }
        return output;
    }

    public boolean hasNext() {
        return (i.size() + j.size() > 0);
    }
}
 
