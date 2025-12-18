package Me23_List_Generic;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class C06_Map {

	// 저장멤버 MAP
	private static Map<String,Integer> map = new HashMap();
	
	public static void Insert(String k, Integer v) {
		if(!map.containsKey(k) && !map.containsValue(v)) {
			map.put(k, v); // key, value저장
		}else {
			System.out.println("동일한 key가 존재합니다");
		}
	}
	
	public static void ShowInfo() {
		//	조회
		Set<String> set=map.keySet(); // MAP안의 모든 key를 set형으로 
		for(String key : set) {
			int value = map.get(key);
			System.out.println("KEY : "+key+"\n"+"Value : "+value);
		}
	}
	
	public static void Remove(String key) {
		Integer result = map.remove(key);
		if(result == null) {
			System.out.println("삭제실패..");
		}else {
			System.out.println("삭제성공");
		}
		
	}
	public static void Remove(Integer value) {
		// 동일한 Value을 가지는 모든 요소를 삭제
		
		// map의 키정보를 Set을 String변환대서 넘긴다
		Set<String> set = map.keySet();
		for(String key : set) {
			// Integer형 매개변수 value와 map에 가져온 키에있는 value를 대조하라
			if(value.equals(map.get(key))) {
				
			}
			
		}
	}
	
	public static void main(String[] args) throws Exception{
		
		map.put("aaa",1111);
		map.put("bbb",2222);
		map.put("ccc",3333);
		map.put("ddd",4444);
		map.put("ddd",1234); // id 중복인 경우(나중 요청된 K:V 저장)
		map.put("fff",1234); // pw 중복인 경우(문제없이 저장)
		
		// 개수
		System.out.println("저장 수 : "+map.size());
		
		// 조회
		ShowInfo();
		
		// 삭제
		Remove("aaa"); Remove("bbb");
		
		//	개수	
		System.out.println("저장 수 : " + map.size());
		Remove(3333); //Value전달 삭제
		System.out.println("저장 수 : " + map.size());
		ShowInfo();
	}

}
