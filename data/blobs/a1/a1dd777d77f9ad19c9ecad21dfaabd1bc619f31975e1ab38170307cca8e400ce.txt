package com.tutorialspoint.util;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import java.lang.reflect.*;
import com.tutorialspoint.Args;
import com.tutorialspoint.MethodTest;
import java.util.*;
import java.util.stream.*;
import com.alibaba.fastjson.JSON;
import com.tutorialspoint.HelloWorld;

public class Utils{

   public final static Map<String,String> TYPE_MAP = new HashMap<String, String>();

   public final static MavenProjectClassLoader MAVEN_PROJECT_CLASS_LOADER = new MavenProjectClassLoader();

   static{
	TYPE_MAP.put("byte","java.lang.Byte");
	TYPE_MAP.put("short","java.lang.Short");
	TYPE_MAP.put("int","java.lang.Integer");
	TYPE_MAP.put("long","java.lang.Long");
	TYPE_MAP.put("float", "java.lang.Float");
	TYPE_MAP.put("double","java.lang.Double");
	TYPE_MAP.put("char","java.lang.Character");
	TYPE_MAP.put("boolean","java.lang.Boolean");
	TYPE_MAP.put("byte[]","java.lang.Byte[]");
	TYPE_MAP.put("short[]","java.lang.Short[]");
	TYPE_MAP.put("int[]","java.lang.Integer[]");
	TYPE_MAP.put("long[]","java.lang.Long[]");
	TYPE_MAP.put("float[]", "java.lang.Float[]");
	TYPE_MAP.put("double[]","java.lang.Double[]");
	TYPE_MAP.put("char[]","java.lang.Character[]");
	TYPE_MAP.put("boolean[]","java.lang.Boolean[]");
   }
   
    public static Class forName(String className) throws ClassNotFoundException{
        if(className.indexOf('.') <0){
	    className = className.toLowerCase();
	}
	switch(className){
	    case "byte":
		return byte.class;
	    case "short":
		return short.class;
	    case "int":
		return int.class;
	    case "long":
		return long.class;
	    case "float":
		return float.class;
	    case "double":
		return double.class;
	    case "char":
		return char.class;
	    case "string":
		return String.class;
	    case "byte[]":
		return byte[].class;
	    case "short[]":
		return short[].class;
	    case "int[]":
		return int[].class;
	    case "long[]":
		return long[].class;
	    case "float[]":
		return float[].class;
	    case "double[]":
		return double[].class;
	    case "char[]":
		return char[].class;
	    case "string[]":
		return String[].class;

	    default:
		return Class.forName(className);
	}
    }


    public static Object exec(String objectName, String methodName) throws Exception{
	System.out.println(String.format("===================objectName:%s\tmethodName:%s",objectName, methodName));
	ApplicationContext context = new ClassPathXmlApplicationContext("Beans.xml");

        Object objectBean = null;
	try{ objectBean = context.getBean(objectName);}
	catch(Exception e){
	    throw new Exception(String.format("================"+objectName+"引用未在配置文件中定义"));
	}

	try{ context.getBean(methodName);}
	catch(Exception e){
	    System.out.println("================="+methodName+"引用未在配置文件中定义,调用默认类方法"+methodName);
	    return objectBean.getClass().getMethod(methodName).invoke(objectBean);
	}
	
	Args methodBean = (Args) context.getBean(methodName);
	Class[] methodType = new Class[methodBean.values==null?0:methodBean.values.length];
	if(methodBean.values != null){
	    for(int i=0;i<methodBean.values.length;i++){
		methodType[i] = methodBean.values[i].getClass();
	    }
	}
	for(Method method: objectBean.getClass().getDeclaredMethods()){
	   if(method.getName().equals(methodBean.methodName)){
		if(classArrayEquals(methodType, method.getParameterTypes())){
		    System.out.println("=============执行程序:"+
			String.format("类名:%s\t方法名:%s\t方法参数:%s", 
			    objectBean.getClass().getName(),
			    methodBean.getMethodName(), 
			    Arrays.toString(method.getParameterTypes())));
		    return method.invoke(objectBean, methodBean.values);
	        } 
	    }
	}
	throw new Exception(
	   String.format("==========找不到方法,类名:%s\t方法名:%s\t方法参数:%s", 
	       objectBean.getClass().getName(),
	       methodBean.getMethodName(), 
	       Arrays.toString(methodType)));
    }

    public static boolean classArrayEquals(Class[] a1, Class[] a2){
	if(null == a1 && null == a2){return true;}
	if(null == a1 || null == a2){return false;}
	if(a1.length != a2.length){return false;}

	for(int i=0;i<a1.length;i++){
	    String name1 = a1[i].getCanonicalName();
	    String name2 = a2[i].getCanonicalName();	
	    System.out.println(String.format("name1:%s,name2:%s",name1,name2));
	    if(name1.equals(name2)){ continue;}else{
		name1 = Optional.ofNullable(TYPE_MAP.get(name1)).orElse(name1);
		name2 = Optional.ofNullable(TYPE_MAP.get(name2)).orElse(name2);
		if(!name1.equals(name2)){ return false;}
	    }
	}
	return true;
   }

   public static Object exec(String beanId) throws Exception{
	System.out.println("========================================beanId:"+beanId);
	ApplicationContext context = new ClassPathXmlApplicationContext("Beans.xml");

	System.out.println("========================================context:"+(context==null));
	Args args = null; 
	try{ args = (Args)context.getBean(beanId);}
	catch(Exception e){
	    throw new Exception(beanId+"引用在配置文件中未定义或定义出错\n"+e.getMessage());
	}
       
	if(args.className == null){ throw new Exception("执行类className为空");}
	if(args.methodName == null){ throw new Exception("执行方法methodName为空");}

	String stackMsg = String.format("类名:%s\t构造参数类型:%s\t构造参数:%s\t方法名:%s\t方法参数类型%s\t方法参数:%s", 
	                         args.className,
			         JSON.toJSONString(Arrays.stream(Optional.ofNullable(args.constructorArgs).orElse(new Object[0])).map(a -> a.getClass().getCanonicalName()).toArray(String[]::new)),
				 JSON.toJSONString(Optional.ofNullable(args.constructorArgs).orElse(new Object[0])),
			         args.methodName,
			         JSON.toJSONString(Arrays.stream(Optional.ofNullable(args.values).orElse(new Object[0])).map(a->a.getClass().getCanonicalName()).toArray(String[]::new)),
				 JSON.toJSONString(Optional.ofNullable(args.values).orElse(new Object[0]))
			        ); 


	//初始化测试对象并执行方法
	try{ 
	    //因为同一个类只能被同一个加载器加载一次，否则报LinkageError,所以这里每次都创建一个新的加载器进行加载
	    Class clazz = new MavenProjectClassLoader().findClass(args.className);
            Class[] constructorArgsTypes = Arrays.stream(Optional.ofNullable(args.constructorArgs).orElse(new Constructor[0]))
					       .map(arg -> arg.getClass())
					       .toArray(Class[]::new);
            Class[] valuesTypes = Arrays.stream(Optional.ofNullable(args.values).orElse(new Object[0]))
					       .map(arg -> arg.getClass())
					       .toArray(Class[]::new);

	    for(Constructor c: clazz.getConstructors()){
		if(classArrayEquals(constructorArgsTypes, c.getParameterTypes())){
		    Object execObject = c.newInstance(args.constructorArgs);
		    for(Method m : clazz.getDeclaredMethods()){
			if(args.methodName.equals(m.getName()) && classArrayEquals(valuesTypes, m.getParameterTypes())){
			    System.out.println("==========执行方法,"+stackMsg);
			    m.setAccessible(true);
			    System.out.println("++---args value instance of HelloWorld"+(args.values[0] instanceof HelloWorld));
			    //return m.invoke(execObject, args.values[0]);
			    return m.invoke(new MethodTest(), new HelloWorld());
			    //System.out.println(String.format("args_value_length:%d,args_value:%s",args.values.length,
			    //    JSON.toJSONString(args.values)));
			    //Object exearg = args.values.length==1?(Object)args.values[0]:(Object)args.values;
			    //System.out.println("==========exearg,"+JSON.toJSONString(exearg));
			    //System.out.println("==========exearg class:,"+exearg.getClass().getCanonicalName());
			    //return m.invoke(execObject, exearg);
//
//			    System.out.println(String.format("method name:%s, method types:%s", m.getName(),
//				JSON.toJSONString(Arrays.stream(m.getParameterTypes()).map(t -> t.getCanonicalName()).
//				toArray(String[]::new))));
//			    System.out.println("args values type:"+args.values.getClass().getCanonicalName());
//			    System.out.println("args values[0] type:"+args.values[0].getClass().getCanonicalName());
//			    //return m.invoke(execObject, (Object)args.values[0]);
//			    HelloWorld[] hw = new HelloWorld[1];
//			    hw[0] = new HelloWorld();
//			    System.out.println("execObject class name:"+execObject.getClass().getName());
//			    //return m.invoke(execObject, hw); 
//	                    Method method =  MethodTest.class.getMethod("printO", HelloWorld[].class);
//			    System.out.println("execObject instanceof of MethodTest:"+(execObject instanceof MethodTest));
//			    System.out.println("execObject class name:"+execObject.getClass().getName());
//			//    return method.invoke(execObject,hw);
////			    return method.invoke((MethodTest)execObject,hw);
//
//ApplicationContext context1 = new ClassPathXmlApplicationContext("Beans.xml");
//
//	Args _args = null; 
//	try{ _args = (Args)context1.getBean("test41");}
//	catch(Exception e){
//	    throw new Exception("引用在配置文件中未定义或定义出错\n"+e.getMessage());
//	}
//	MethodTest m1 = new MethodTest();
//
//	//Object[] aa = new HelloWorld[2];
//	//HelloWorld a1 = new HelloWorld();
//	//a1.message = "ajflaj";
//	//aa[0] = a1;
//	//HelloWorld a2 = new HelloWorld();
//	//a2.message = "ajflaj";
//	//aa[1] = a2;
//	//System.out.println("jkldsjfalj=============9999988888888889");
//
//	//Method method1 =  MethodTest.class.getMethod("printO", HelloWorld[].class);
//	Arrays.stream(execObject.getClass().getMethods()).forEach(mm -> System.out.println(mm.getName() +"--"+ Arrays.toString(mm.getParameterTypes())));
//	Method method1 =  execObject.getClass().getMethod("printO", HelloWorld[].class);
//
//	Arrays.stream(_args.values).forEach(e-> System.out.println(e.getClass().getCanonicalName()));
//	Arrays.stream(method1.getParameterTypes()).forEach(e -> System.out.println(e.getCanonicalName()));
//	System.out.println("args values class"+_args.values.getClass().getCanonicalName());
//
//	method1.setAccessible(true);
//	Object invokearg = _args.values.length==1?_args.values[0]:_args.values;
//	//System.out.println("invoke args"+JSON.toJSONString(invokearg));
//	System.out.println("-----------------------args values "+JSON.toJSONString(_args.values));
//
////	method1.invoke(execObject, args.values);
//	method1.invoke(execObject, args.values);


			}
		    }
		}
	    }
	} catch(Exception e){
	    e.printStackTrace();
	    throw e;
	}
	
    	throw new Exception("==========找不到类和方法,"+stackMsg);
    }
}
