class Solution {
    public int secondHighest(String s) {
        int largest = -1;
        int secondLargest = -1;
        
        for (char ch : s.toCharArray()) {
            if (Character.isDigit(ch)) {
                int c = Character.getNumericValue(ch);
                
                // 1. If the digit is greater than the largest found so far
                if (c > largest) {
                    secondLargest = largest; // Old largest drops to second
                    largest = c;             // Update largest
                } 
                // 2. If it's between largest and secondLargest (ignores duplicates)
                else if (c < largest && c > secondLargest) {
                    secondLargest = c;
                }
            }
        }
        
        return secondLargest;
    }
}
