package com.example.dinozavr;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.res.Resources;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Rect;
import android.media.AudioAttributes;
import android.media.AudioManager;
import android.media.SoundPool;
import android.os.Build;
import android.os.CountDownTimer;
import android.view.MotionEvent;
import android.view.SurfaceView;
import android.view.View;
import android.view.Window;

import java.util.Timer;

public class GameView extends SurfaceView implements Runnable {
    private Thread thread;
    private boolean isPlaying;
    private int screenX, screenY; // поля размеров экрана по осям X и Y
    private Background background1, background2;
    private Paint paint; // поле стилей рисования
    private float screenRatioX, screenRatioY; // поля размеров экрана для совместимости разных размеров экрана
    private dino dino;
    private cactus cactus;
    private SharedPreferences preferences;
    private boolean CactisV = true;
    private boolean isGameOver = false;
    private boolean isGoingUp = false;
    private GameActivity activity;
    private int score = 0;
    private  int a = 0;
    private SoundPool soundPool; // поле для проигрывания маленьких аудиоклипов
    private int sound;







    public GameView(GameActivity activity, int screenX, int screenY) {
        super(activity);
        this.activity = activity;
        preferences = activity.getSharedPreferences("game", Context.MODE_PRIVATE);
        this.screenX = screenX;
        this.screenY = screenY;






        //настройка музыки
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            // 1 вариант настройки воспроизведения аудио
            AudioAttributes audioAttributes = new AudioAttributes.Builder()
                    .setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
                    .setUsage(AudioAttributes.USAGE_GAME)
                    .build();
            // загрузка настроек
            soundPool = new SoundPool.Builder()
                    .setAudioAttributes(audioAttributes)
                    .build();
        }  else { // иначе если старая сборка, то
            // 2 вариант настройки воспроизведения аудио
            soundPool = new SoundPool(1, AudioManager.STREAM_MUSIC, 0);
        }
        // загрузка нужного аудиофайла из папки res/raw
        sound = soundPool.load(activity, R.raw.musik, 1);




        screenRatioX = 1920f / screenX;
        screenRatioY = 1080f / screenY;
        background1 = new Background(screenX, screenY, getResources());
        background2 = new Background(screenX, screenY, getResources());



        // присваивание полю x класса Background переменной ширины screenX
        background2.setX(screenX); // второй фон мы сдвигаем по оси Х с нуля на размер ширины изображения


        paint = new Paint();
        paint.setTextSize(64);
        paint.setColor(Color.BLACK);
        dino = new dino(screenX, screenY, getResources());
        cactus = new cactus(screenX, screenY, getResources());

    }


    public GameView(Context context) {
        super(context);
    }
    @Override
    public void run() {
        while (isPlaying) {
            draw();
            sleep();
            update();

        }
    }


    public void update() {

        //фон

        if (a == 0) {
            background1.setX(background1.getX() - (int) (10 * screenRatioX));
            background2.setX(background2.getX() - (int) (10 * screenRatioX));
        }
        if (a == 1) {
            background1.setX(background1.getX() - (int) (12 * screenRatioX));
            background2.setX(background2.getX() - (int) (12 * screenRatioX));
        }
        if (a == 2) {
            background1.setX(background1.getX() - (int) (15 * screenRatioX));
            background2.setX(background2.getX() - (int) (15 * screenRatioX));
        }
        if (a == 3) {
            background1.setX(background1.getX() - (int) (18 * screenRatioX));
            background2.setX(background2.getX() - (int) (18 * screenRatioX));
        }
        if (a == 4) {
            background1.setX(background1.getX() - (int) (20 * screenRatioX));
            background2.setX(background2.getX() - (int) (20 * screenRatioX));
        }
        if (a == 5) {
            background1.setX(background1.getX() - (int) (22 * screenRatioX));
            background2.setX(background2.getX() - (int) (22 * screenRatioX));
        }
        if (a == 6) {
            background1.setX(background1.getX() - (int) (25 * screenRatioX));
            background2.setX(background2.getX() - (int) (25 * screenRatioX));
        }

        if ((background1.getX() + background1.getBackground().getWidth()) <= 0) { // если фон 1 полностью исчез с экрана
            background1.setX(screenX); // то обновление x до размера ширины фона
        }
        if ((background2.getX() + background2.getBackground().getWidth()) <= 0) { // если фон 2 полностью исчез с экрана
            background2.setX(screenX); // то обновление x до размера ширины фона
        }


        //дино
        if (dino.isGoingUp()) {
            if (!preferences.getBoolean("isMute", false)) {
                // при выпуске снаряда воспроизводится звук (индекс, стерео, приоритет, повтор - нет, порядок)
                soundPool.play(sound, 1,1, 0, 0, 1);
            }
            // условие подъём
            dino.setY(screenY / 1 / 2);
            dino.setGoingUp(false);
        } else { // условие снижения
            dino.setY(dino.getY() + (int) (18 * screenRatioY));
        }

        if (dino.getX() < 0) {
            dino.setX(0);
        } else if (dino.getY() >= screenY - dino.getHeight()) {
            dino.setY(screenY - dino.getHeight());
        }



        //кактус
        if (cactus.getY() < 0) {
            cactus.setY(0);
        } else if (cactus.getY() >= screenY - cactus.getHeight()) {
            cactus.setY(screenY - cactus.getHeight());
        }

        if (CactisV){
            cactus.setY(cactus.getY() + (int) (18 * screenRatioY));
        }

        if (CactisV) {
            if (a == 0) {
                cactus.setX(cactus.getX() - (int) (20 * screenRatioY));
            }
            if (a == 1) {
                cactus.setX(cactus.getX() - (int) (25 * screenRatioY));
            }
            if (a == 2) {
                cactus.setX(cactus.getX() - (int) (28 * screenRatioY));
            }
            if (a == 3) {
                cactus.setX(cactus.getX() - (int) (30 * screenRatioY));
            }
            if (a == 4) {
                cactus.setX(cactus.getX() - (int) (33 * screenRatioY));
            }
            if (a == 5) {
                cactus.setX(cactus.getX() - (int) (36 * screenRatioY));
            }
            if (a == 6) {
                cactus.setX(cactus.getX() - (int) (40 * screenRatioY));
            }
        }
        if (cactus.getX() < -100) {
            cactus.setX(3000);
        }
        //столкновение
        if (Rect.intersects(dino.getCollisionShape(), cactus.getCollisionShape())) {
            isGameOver = true; // установление флага окончания игры
            return;
        }

        //очки
        if (score == 200) {
            a = 1;
        }
        if (score == 500) {
            a = 2;
        }
        if (score == 700) {
            a = 3;
        }
        if (score == 1000) {
            a = 4;
        }
        if (score == 1200) {
            a = 5;
        }
        if (score == 1500) {
            a = 6;
        }
        score++;





    }

    public void draw() {
        if (getHolder().getSurface().isValid()) { // проверка валидности объекта surface

            Canvas canvas = getHolder().lockCanvas(); // метод lockCanvas() возвращает объект Canvas (холст для рисования)
            // метод drawBitmap() рисует растровое изображение фона на холсте (изображение, координаты X и Y, стиль для рисования)
            canvas.drawBitmap(background1.getBackground(), background1.getX(), background1.getY(), paint);
            canvas.drawBitmap(background2.getBackground(), background2.getX(), background2.getY(), paint);

            // отрисовка растрового изображения самолёта
            canvas.drawBitmap(dino.getDino(), dino.getX(), dino.getY(), paint);
            canvas.drawBitmap(cactus.getCactus(), cactus.getX(), cactus.getY(), paint);

            canvas.drawText("Рекорд: " + score, screenX / 2f, screenY / 8f, paint);



            if (isGameOver) {
                isPlaying = false; // установление флага приостановления дополнительного потока
                // отрисовка растрового изображения подбитого самолёта
                canvas.drawBitmap(dino.getPlaneShotDown(), dino.getX(), dino.getY(), paint);
                // вывод нарисованных изображений на экран
                getHolder().unlockCanvasAndPost(canvas);
                // сохранение рекордного результата
                saveIfHighScore();
                danna();
                // считывание рекордного результата при загрузке приложения
                waitBeforeExiting();
                return;
            }


            // вывод нарисованных изображений на экран
            getHolder().unlockCanvasAndPost(canvas);
        }
    }

    public void sleep() {
        try {
            // засыпание потока на 16 милисекунд
            Thread.sleep(16);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }


    public void resumeThread() {
        thread = new Thread(this);
        thread.start();
        isPlaying = true;

    }

    @Override
    public boolean onTouchEvent(MotionEvent event) {

        // обработка событий касания экрана
        switch (event.getAction()) {
            case MotionEvent.ACTION_DOWN: // нажатие
                // если пользователь нажал на левую сторону экрана
                if (event.getX() < (screenX)) {
                    // то движение самолёта вверх
                    dino.setGoingUp(true);
                } else if (event.getX() >= (screenX)) {

                }
                break;
            case MotionEvent.ACTION_MOVE: // движение по экрану

                break;
            case MotionEvent.ACTION_UP: // отпускание
                // при отпускании экрана самолёт начнёт снижаться
                dino.setGoingUp(false);
                break;
        }

        return true; // активация обработки касания экрана
    }


    public void pauseThread() {
        try {
            // установление флага приостановления игры
            isPlaying = false;
            // приостановление потока
            thread.join();
            /**
             * метод join() — используется для того,
             * чтобы приостановить выполнение текущего потока до тех пор,
             * пока другой поток не закончит свое выполнение
             */
        } catch (InterruptedException e) { // исключение на случай зависания потока
            e.printStackTrace();
        }
    }
    private void saveIfHighScore() {

        if (preferences.getInt("gamer", 0) < score) {
            // сохраним рекордное значение
            SharedPreferences.Editor editor = preferences.edit();
            editor.putInt("gamer", score);
            editor.apply();
        }
    }
    private void danna() {
         preferences.getInt("qwe" , 0);

            SharedPreferences.Editor editor = preferences.edit();
            editor.putInt("qwe", score); // внесение нового рекордного значения
            editor.apply(); // сохранение результатов

    }
    // метод считывания рекордного результата при загрузке приложения
    private void waitBeforeExiting() {
        // ввод вспомогательного потока в сон на 3 секунды
        try {
            Thread.sleep(3000);
            // переход к основной активити
            activity.startActivity(new Intent(activity, MainActivity.class));
            activity.finish(); // закрытие данной активити
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

}
