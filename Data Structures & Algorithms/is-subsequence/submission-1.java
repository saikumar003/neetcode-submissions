public class Solution {
    public boolean isSubsequence(String s, String t) {
        if (s.isEmpty()) return true;
        
        int s1 = 0;
        int t1 = 0;
        
        while (t1 < t.length()) {
            if (s.charAt(s1) == t.charAt(t1)) {
                s1++;
            }
            t1++;

        if(s1 == s.length()){
            return true;
        }

        
        }
        
        return s1 == s.length();
    }
}