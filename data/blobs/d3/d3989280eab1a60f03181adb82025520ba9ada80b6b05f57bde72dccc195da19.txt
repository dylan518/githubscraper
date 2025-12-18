package AtivEmpresa;

public class PrincipalEmpresa {

	public static void main(String[] args) {
		Departamento setor = new Departamento ("USP");
		Empresa JGT = new Empresa ("fellipe",setor);
		
		System.out.println("empresa "+JGT.getNome()+"/departmento "+setor.getdep());
		
	}

}
