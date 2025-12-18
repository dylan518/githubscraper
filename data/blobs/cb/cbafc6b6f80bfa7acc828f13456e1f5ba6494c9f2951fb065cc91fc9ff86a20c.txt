class Solution {
    public String removeDuplicates(String s) {
        //재귀를 사용해야 할 듯 싶다. ==> 안써도 되었다.
        //반복이 중단 되는 조건은 인접한 글자가 같지 않으면 반복을 중단하고 길이가 0이나 1이면 그냥 리턴한다.

        // 그냥 하나씩 넣으면서 저장하던 것의 마지막 것과 비교하고 같은면 지우는방식으로했으면 됨
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (sb.length() > 0 && sb.charAt(sb.length() - 1) == c) sb.deleteCharAt(sb.length() - 1);
            else sb.append(c);
        }
        return sb.toString();
    }
}