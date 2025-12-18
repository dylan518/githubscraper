import java.util.*;

class Solution {
    public int[] solution(String[] ids, String[] reports, int k) {
        Map<String, Set<String>> map = new HashMap<>();
        Map<String, Integer> counts = new HashMap<>();
        Map<String, Integer> answer = new HashMap<>();
        
        for (String id : ids) {
            map.put(id, new HashSet<>());
            answer.put(id, 0);
        }
        
        for (String report : reports) {
            String splits[] = report.split("\\s");
            if (map.get(splits[0]).add(splits[1])) {
                counts.put(splits[1], counts.getOrDefault(splits[1], 0) + 1);
            }
        }
        
        for (Map.Entry<String, Set<String>> entry : map.entrySet()) {
            Set<String> set = entry.getValue();
            set.stream().forEach(s -> {
                if (counts.get(s) >= k) {
                    answer.put(entry.getKey(), answer.getOrDefault(entry.getKey(), 0) + 1);
                }
            });
        }
        
        List<Integer> numbers = new ArrayList<>();
        for (String id : ids) {
            numbers.add(answer.get(id));
        }
        
        return numbers.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}