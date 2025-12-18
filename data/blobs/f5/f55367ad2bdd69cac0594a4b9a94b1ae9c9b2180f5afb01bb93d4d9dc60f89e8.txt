package sukkiri.object_oriented.abstract_class.sample01;
//抽象メソッドとは、処理内容を記述しないメソッドです。
//抽象クラスとは、抽象メソッドを持つクラスを指します。
//抽象クラスはインスタンス化することができません。

abstract class Animal { //①抽象クラス
	//フィールド
	String name;
	//コンストラクタ
	public Animal(String name) { 
		this.name = name; 
		}
	//抽象メソッド
	abstract void run(); //②抽象メソッド
	//getter, setter
	public String getName() {
		return name;
		}
	public void setName(String name) {
		this.name = name;
		}
	}

