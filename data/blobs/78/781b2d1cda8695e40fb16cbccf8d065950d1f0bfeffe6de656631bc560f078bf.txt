public class TADVetor implements ITADVetor{
    private ListaEncadeada Lista;
    private No primeiro;
    private No head;
    private No tail;
    private No ultimo;
    private No atual;
    private No anterior;
    private int tamanho;

    public TADVetor() {
        //dando erro de "Lista is null" sem isso
        this.Lista = new ListaEncadeada();
        //nós sentinelas
        this.head = new No(null);
        this.tail = new No(null);
        head.setNext(tail);
        tail.setPrev(head);
        this.tamanho = 0;
    }

    public Object elemAtRank(No posicao) {
        return posicao.getElement();
    }

    public Object replaceAtRank(No posicao, Object novoElemento) {
        No novoNo = new No(novoElemento);
        this.atual =posicao;
        posicao.setElement(novoNo);
        return atual;
    }

    public void insertAtRank(No posicao, Object novoElemento) {
        No novoNo = new No(novoElemento);
        //novoNo => posição
        novoNo.setNext(posicao);
        //anterior (do posição) <= novoNo
        novoNo.setPrev(posicao.getPrev());
        //posição => próximo
        posicao.setNext(posicao.getNext());
        //novoNo <= posição
        posicao.setPrev(novoNo);
        tamanho++;

    }

    public Object removeAtRank(No posicao) {
        //anterior => atual => próximo / anterior => próximo
        (posicao.getPrev()).setNext(posicao.getNext());
        //anterior <= próximo
        (posicao.getNext()).setPrev(posicao.getPrev());
        tamanho--;
        return posicao;
    }

    public void size() {
        System.out.println("Tamanho da lista: "+Lista.getTamanho());

    }

    public boolean isEmpty() {
        //se o próximo do head for o tail, significa que a lista está vazia
        return head.getNext()==tail;
    }
}
