package org.example.백준.알고리즘중급_1.BFS_연습.탈출_3055;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int R;
    static int C;
    static char[][] map;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());


        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        Queue<Loc> loc = new LinkedList<>();
        Queue<Loc> water =new LinkedList<>();
        boolean[][] visit = new boolean[R][C];

        map = new char[R][C];

        for (int i = 0; i < R; i++) {
            String str = br.readLine();
            for (int j = 0; j < C; j++) {
                map[i][j] = str.charAt(j);
                if (map[i][j] == 'S') {
                    visit[i][j] = true;
                    loc.add(new Loc(i,j,0));
                }
                if (map[i][j] == '*') {
                    water.add(new Loc(i,j,0));
                }
            }
        }


        while (!loc.isEmpty()) {

            int size = loc.size();

            for (int i = 0; i < size; i++) {
                Loc temp = loc.poll();

                if(map[temp.x][temp.y] == 'D') {
                    System.out.println(temp.count);
                    return;
                }

                if(map[temp.x][temp.y] == '*') {
                    continue;
                }

                for (int j = 0; j < 4; j++) {

                    int x = temp.x + dx[j];
                    int y = temp.y + dy[j];

                    if(x < 0 || x >= R || y < 0 || y >= C) {
                        continue;
                    }

                    if(map[x][y] == '*' || map[x][y] == 'X' || visit[x][y]) {
                        continue;
                    }

                    visit[x][y] = true;
                    if(map[x][y] != 'D') {
                        map[x][y] = 'S';
                    }
                    loc.add(new Loc(x,y, temp.count+1));

                }
            }


            int size2 = water.size();

            for (int i = 0; i < size2; i++) {

                Loc temp = water.poll();

                for (int j = 0; j < 4; j++) {

                    int x = temp.x + dx[j];
                    int y = temp.y + dy[j];

                    if(x < 0 || x >= R || y < 0 || y >= C) {
                        continue;
                    }

                    if(map[x][y] == 'D' || map[x][y] == '*' || map[x][y] == 'X') {
                        continue;
                    }

                    map[x][y] = '*';
                    water.add(new Loc(x,y,0));
                }
            }

        }


        System.out.println("KAKTUS");

    }

    static class Loc {

        int x;
        int y;
        int count;

        public Loc(int x, int y , int count) {
            this.x = x;
            this.y = y;
            this.count = count;
        }
    }

}
