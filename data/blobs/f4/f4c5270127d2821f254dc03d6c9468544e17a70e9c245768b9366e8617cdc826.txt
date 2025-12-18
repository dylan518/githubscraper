class CarNames
{
    public static void main(String []args)
	{
		System.out.println("start main in CarNames");
		
        String c1="BMW";
		String c2="Suzuki";
		String c3="Benz";
		String c4="Crete";
		String c5="Ertiga";
		String c6="Swift";
		String c7="Alto";
		String c8="Brezza";
		String c9="Sonet";
		String c10="Nexon";
		String c11="Tiago";
		String c12="Bolero";
		String c13="Ignis";
		String c14="Amaze";
		String c15="Triber";
		
		String[] Totalcarnames={c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15};
		
		for(int begin=0;begin<Totalcarnames.length;begin++)
		{
			System.out.println("Begin:"+Totalcarnames[begin]);
		}
		
		System.out.println(Totalcarnames.length);
		System.out.println("end main in carnames");

	}
}