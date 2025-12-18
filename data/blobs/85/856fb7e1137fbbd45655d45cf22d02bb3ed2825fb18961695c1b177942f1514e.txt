package com.example.tfg_adrian;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Rect;
import android.util.Log;
import android.view.MotionEvent;
import android.view.SurfaceHolder;
import android.view.SurfaceView;

import androidx.annotation.NonNull;

public class GameView extends SurfaceView implements SurfaceHolder.Callback {
    GameThread gameThread;
    Rect retryBtn;

    public GameView(Context context) {
        super(context);
        InitView();
    }

    @Override
    public void surfaceCreated(@NonNull SurfaceHolder surfaceHolder) {
        startGameThread(surfaceHolder);
    }

    @Override
    public void surfaceChanged(@NonNull SurfaceHolder surfaceHolder, int i, int i1, int i2) {
    }

    @Override
    public void surfaceDestroyed(@NonNull SurfaceHolder surfaceHolder) {
        stopGameThread();
    }

    void InitView() {
        SurfaceHolder holder = getHolder();
        holder.addCallback(this);
        setFocusable(true);

        int left = AppConstants.SCREEN_WIDTH / 2 - 190;
        int top = 400;
        int right = left + AppConstants.getBitmapBank().retryBtn.getWidth();
        int bottom = top + AppConstants.getBitmapBank().retryBtn.getHeight();
        retryBtn = new Rect(left, top, right, bottom);
    }

    @Override
    public boolean onTouchEvent(MotionEvent event) {
        int action = event.getAction();

        if (retryBtn.contains((int) event.getX(), (int) event.getY())) {
            onRetryButtonClick();
        } else {
            // Se ha detectado un toque en la pantalla
            if (action == MotionEvent.ACTION_DOWN) {
                if (AppConstants.getGameEngine().gameState != 2) {
                    AppConstants.getGameEngine().gameState = 1;
                    AppConstants.getGameEngine().monkey.setVelocity(AppConstants.VELOCITY_WHEN_JUMP);
                }
            }
        }
        return true;
    }

    private void onRetryButtonClick() {
        stopGameThread();

        // Reiniciar el estado del juego
        AppConstants.gameEngine = new GameEngine();

        // Reiniciar la vista y el hilo del juego
        InitView();
        startGameThread(getHolder());
    }
    private void startGameThread(SurfaceHolder surfaceHolder) {
        if (gameThread == null || !gameThread.isRunning()) {
            gameThread = new GameThread(surfaceHolder);
            gameThread.setIsRunning(true);
            gameThread.start();
        }
    }

    private void stopGameThread() {
        if (gameThread != null && gameThread.isRunning()) {
            gameThread.setIsRunning(false);
            boolean retry = true;
            while (retry) {
                try {
                    gameThread.join();
                    retry = false;
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            gameThread = null;
        }
    }
}
