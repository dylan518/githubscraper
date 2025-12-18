/**
 *
 *  Esta clase construye un frame a partir de una pregunta
 *  extrayendo sus respuestas e instanciandolas, así como la lógica
 *  del voto entre los participantes
 *
 *  @author CodeBros
 */

package com.codebros.grafico;

import com.codebros.jugadores.Ficha;
import com.codebros.jugadores.Jugador;
import com.codebros.modelo.Pregunta;
import com.codebros.modelo.Respuesta;
import com.codebros.utilidades.Fondo;
import com.codebros.utilidades.JFramePersonalizado;
import com.codebros.utilidades.Sonido;
import com.codebros.utilidades.TipoSonido;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.TimeUnit;

public class FramePregunta extends JFramePersonalizado implements ActionListener {

    //elementos de la clase
    private final Pregunta pregunta;
    private final JLabel turnoActualLabel;
    private final Juego juego;
    private final List<Ficha> jugadoresContestando;
    private Ficha fichaTurnoActual;
    private int idTurnoActual = 0;

    //constructor de la clase
    public FramePregunta(Juego juego, Pregunta pregunta) {

        super(new Fondo("resources\\img\\fondos\\FondoPreguntas.png"));
        setSize(610, 410);
        setLocationRelativeTo(juego);
        setDefaultCloseOperation(DO_NOTHING_ON_CLOSE);

        this.juego = juego;
        this.pregunta = pregunta;
        this.jugadoresContestando = new ArrayList<>(juego.getJugadores());
        Collections.shuffle(this.jugadoresContestando);
        fichaTurnoActual = jugadoresContestando.get(idTurnoActual);

        JLabel preguntaLabel = new JLabel("<html><center>" + pregunta.getPregunta() + "</center></html>", SwingConstants.CENTER);
        preguntaLabel.setFont(new Font("Arial", Font.BOLD, 15));
        preguntaLabel.setForeground(Color.WHITE);
        preguntaLabel.setBounds(0, 30, getWidth()-5, 60);
        add(preguntaLabel);
        repaint();

        //se crea Jlabel que mostrara el turho
        turnoActualLabel = new JLabel("Turno de "
                + fichaTurnoActual.getNombre(), SwingConstants.RIGHT);
        turnoActualLabel.setFont(new Font("Arial", Font.ITALIC, 15));
        turnoActualLabel.setBounds(-10, 0, getWidth(), 37);
        add(turnoActualLabel);

        //agrega todas las respuestas al Frame
        int auxY = 85;
        for (Respuesta respuesta : pregunta.getRespuestas()) {
            add(respuesta);
            respuesta.addActionListener(this);
            respuesta.mover(50, auxY, 5);
            auxY += 75;
        }
    }

    // Evento de respuesta presionada
    @Override
    public void actionPerformed(ActionEvent e) {

        new Sonido(TipoSonido.CLICK).play(0); // sonido de voto
        Respuesta presionada = (Respuesta) e.getSource();

        if (presionada.esCorrecta()) {
            ((Jugador) fichaTurnoActual).avanzaSiguienteRonda(true);
        }

        if (idTurnoActual != juego.getJugadores().size() - 1) {
            new Thread(() -> {

                pregunta.getRespuestas().forEach(respuesta -> respuesta.setEnabled(false));

                try {
                    TimeUnit.SECONDS.sleep(1);
                } catch (InterruptedException ex) {
                    ex.printStackTrace();
                }

                pregunta.getRespuestas().forEach(respuesta -> respuesta.setEnabled(true));
                fichaTurnoActual = jugadoresContestando.get(++idTurnoActual);
                turnoActualLabel.setText("Turno de " + fichaTurnoActual.getNombre());
            }).start();

        } else {
            new Thread(() -> {
                try {
                    // Quita label de turno y desactiva las respuestas
                    remove(turnoActualLabel);
                    pregunta.getRespuestas().forEach(res -> res.setEnabled(false));
                    repaint();

                    // Sleep thread 2
                    TimeUnit.SECONDS.sleep(2);

                    // Tambores de suspenso...
                    new Sonido(TipoSonido.TAMBORES).play(0);

                    // Esperamos 4 segundos
                    TimeUnit.SECONDS.sleep(4);

                    // Hace un sonido y pinta de verde la respuesta correcta
                    new Sonido(TipoSonido.POP).play(0);
                    for (Respuesta respuesta : pregunta.getRespuestas()) {
                        if (respuesta.esCorrecta()) {
                            respuesta.setEnabled(true);
                            respuesta.setForeground(Color.GREEN);
                            respuesta.removeActionListener(this);
                        }
                    }

                    juego.getTarjetas().forEach(tarjeta -> tarjeta.setVisible(false));
                    // Espera de 2 seg
                    TimeUnit.SECONDS.sleep(2);
                    juego.aplicarMovimientosPendientes();
                    dispose();
                } catch (InterruptedException exception) {
                    exception.printStackTrace();
                }
            }).start();
        }

    }
}
