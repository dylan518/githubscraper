class StaticModifierDemo
{
	int x = 10;
	static int y = 20;
	public static void main(String...args)
	{
		StaticModifierDemo sd = new StaticModifierDemo();
		sd.x=888;
		sd.y=999;
		StaticModifierDemo sd1 = new StaticModifierDemo();
		System.out.println(sd1.x +"  "+sd1.y);
	}
}

// In case of instance variable for every object a separate copy will be created.

/* In the case of static variable only one copy will be created at class level,
that copy for every object of the class. */