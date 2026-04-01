class Solution {
    public void reverseString(char[] s) {
        int leftIdx = 0;
        int rightIdx = s.length - 1;

        while (leftIdx < rightIdx) {
            char temp = s[leftIdx];
            s[leftIdx] = s[rightIdx];
            s[rightIdx] = temp;
            leftIdx++;
            rightIdx--;
        }
    }
}