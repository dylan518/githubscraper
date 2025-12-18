class StudentBuffer{
	Student s1;
	boolean status;
	synchronized void insert(Student s){
		if(status){
			try{
				wait();
			}catch(InterruptedException ie){
				System.out.println(ie);
			}
		}
		this.s1=s;
		status=true;
		notify();
	}
	synchronized Student pop(){
		if(!status){
			try{
				wait();
			}catch(InterruptedException ie){
				System.out.println(ie);
			}
		}
		status=false;
		notify();
		return s1;
	}
}
