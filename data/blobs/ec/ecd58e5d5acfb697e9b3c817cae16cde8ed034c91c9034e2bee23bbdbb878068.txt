public class _551_checkRecord {
    public boolean checkRecord(String s) {
        int late = 0;
        int absent = 0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='L'){
                late++;
                if(late>=3) return false;
            } else if (s.charAt(i)=='A') {
                absent++;
                if(absent>=2) return false;
                late=0;
            }else{
                late=0;
            }
        }
        return true;
    }
}
