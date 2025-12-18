
package projeto.models;

public class Sessao {

    String data, hora;
    private Filme filme;
    private Sala sala;

    public Sessao(String data, String hora, Filme filme) {
        this.data = data;
        this.hora = hora;
        this.filme = filme;
    }

    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }

    public String getHora() {
        return hora;
    }

    public void setHora(String hora) {
        this.hora = hora;
    }

    public Filme getFilme() {
        return filme;
    }

    public void setFilme(Filme filme) {
        this.filme = filme;
    }

    public Sala getSala() {
        return sala;
    }

    public void setSala(Sala sala) {
        this.sala = sala;
    }

    public Sessao(String data, String hora, Filme filme, Sala sala) {
        this.data = data;
        this.hora = hora;
        this.filme = filme;
        this.sala = sala;
    }
}
