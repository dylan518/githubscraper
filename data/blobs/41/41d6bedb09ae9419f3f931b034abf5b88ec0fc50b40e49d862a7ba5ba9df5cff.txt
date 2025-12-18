import java.util.*;

public class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {

        Map<String, List<Set<String>>> map = new HashMap<>();
        for (List<String> account : accounts) {
            String nameOfNewAccount = account.get(0);
            Set<String> newAccount = new HashSet<>(account);
            newAccount.remove(nameOfNewAccount);
            Set<String> finalAcc = new HashSet<>(newAccount);
            List<Set<String>> list = new LinkedList<>();
            if (map.containsKey(nameOfNewAccount)) {
                list = map.get(nameOfNewAccount);
                Iterator<Set<String>> iterator = list.iterator();
                while (iterator.hasNext()) {
                    Set<String> strings = iterator.next();
                    for (String s : newAccount) {
                        if (strings.contains(s)) {
                            finalAcc.addAll(strings);
                            iterator.remove();
                            break;
                        }
                    }
                }
                if (finalAcc.equals(newAccount)) {
                    map.get(nameOfNewAccount).add(finalAcc);
                } else {
                    list.add(finalAcc);
                    map.put(nameOfNewAccount, list);
                }
            } else {
                list.add(newAccount);
                map.put(nameOfNewAccount, list);
            }
        }
        Set<Map.Entry<String, List<Set<String>>>> entries = map.entrySet();
        accounts = new ArrayList<>();
        List<String> acc = new ArrayList<>();
        for (Map.Entry<String, List<Set<String>>> entry : entries) {
            for (int i = 0; i < entry.getValue().size(); i++) {
                acc.add(entry.getKey());
                List<String> w = new ArrayList<>(entry.getValue().get(i));
                Collections.sort(w);
                acc.addAll(w);
                accounts.add(acc);
                acc = new ArrayList<>();
            }
        }
        return accounts;
    }
}
