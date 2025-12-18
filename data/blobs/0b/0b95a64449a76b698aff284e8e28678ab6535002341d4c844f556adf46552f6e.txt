import javax.swing.*;
import java.awt.*;
import java.util.Random;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import javax.sound.sampled.*;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class HangMan extends JFrame {
    private JTextField input;
    private JLabel wordLabel, hearts, usedLettersLabel;
    private JButton submitButton, restartButton;
    private String randomWord;
    private int heart;
    private char[] letters;
    private char[] usedLetters;
    private int countLetter;
    private HangmanPanel hangmanPanel;

    public HangMan() {
        super("Hangman Game");
        setBounds(650, 150, 350, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JPanel topPanel = new JPanel(new GridLayout(7, 1));
        
        initializeGame();
        
        JLabel welcomeText = new JLabel("Welcome to the Hangman Game!", SwingConstants.CENTER);
        welcomeText.setOpaque(true);
        welcomeText.setBackground(Color.YELLOW);

        wordLabel = new JLabel(getDisplayedWord(), SwingConstants.CENTER);
        wordLabel.setFont(new Font("Courier New", Font.BOLD, 15));
        
        hearts = new JLabel(getHeartsDisplay(), SwingConstants.CENTER);
        hearts.setForeground(Color.RED);

        usedLettersLabel = new JLabel("Used letters: ", SwingConstants.CENTER);
        
        input = new JTextField();
        input.addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                if (e.getKeyCode() == KeyEvent.VK_ENTER) {
                    processInput();
                }
            }
        });

        topPanel.add(welcomeText);
        topPanel.add(wordLabel);
        topPanel.add(usedLettersLabel);
        topPanel.add(input);

        hangmanPanel = new HangmanPanel();

        JPanel bottomPanel = new JPanel();
        
        submitButton = new JButton("Submit");
        submitButton.addActionListener(_ -> processInput());
        
        restartButton = new JButton("Restart Game");
        restartButton.addActionListener(_ -> restartGame());
        
        bottomPanel.add(submitButton);
        bottomPanel.add(restartButton);

        add(topPanel, BorderLayout.NORTH);
        add(hangmanPanel, BorderLayout.CENTER);
        add(bottomPanel, BorderLayout.SOUTH);
    }

    public class WordLoader {
        public static String[] loadWords(String filename) {
            try {
                List<String> wordList = Files.readAllLines(Paths.get(filename)); // Читаем строки в список
                return wordList.toArray(new String[0]); // Преобразуем список в массив
            } catch (IOException e) {
                e.printStackTrace();
                return new String[]{}; // Возвращаем пустой массив при ошибке
            }
        }

        public static void main(String[] args) {
            String[] words = loadWords("words.txt");
            for (String word : words) {
                System.out.println(word);
            }
        }
    }

    private void initializeGame() {
        playSound("sounds/background.wav");
        String[] words = WordLoader.loadWords("words.txt"); // Загружаем слова из файла
        if (words.length == 0) {
            words = new String[]{"default"}; // Запасной вариант, если файл пустой
        }
        randomWord = words[new Random().nextInt(words.length)];
        
        heart = 6;
        letters = new char[randomWord.length()];
        usedLetters = new char[6];
        countLetter = 0;
    
        for (int i = 0; i < letters.length; i++) {
            letters[i] = '_';
        }
    }    

    public void playSound(String soundFile) {
        try {
            File file = new File(soundFile);
            AudioInputStream audioStream = AudioSystem.getAudioInputStream(file);
            Clip clip = AudioSystem.getClip();
            clip.open(audioStream);
            clip.start();
        } catch (UnsupportedAudioFileException | IOException | LineUnavailableException e) {
            e.printStackTrace();
        }
    }

    private void processInput() {
        String let = input.getText().toLowerCase();
        input.setText("");

        if (let.length() >= 2) {
            if (let.equals(randomWord)) {
                letters = randomWord.toCharArray();
                submitButton.setEnabled(false);
                playSound("sounds/winner.wav"); // Если буква неверная
            } else {
                playSound("sounds/wrong.wav"); // Если буква неверная
                heart--;
            }
        } else {
            boolean found = false;
            char letter = let.charAt(0);
            for (int i = 0; i < randomWord.length(); i++) {
                if (letter == randomWord.charAt(i)) {
                    playSound("sounds/correct.wav"); // Если буква неверная
                    letters[i] = letter;
                    found = true;
                }
            }
            if (!found) {
                playSound("sounds/wrong.wav"); // Если буква неверная
                usedLetters[countLetter++] = letter;
                heart--;
            }
        }
        updateGUI();
    }

    private void updateGUI() {
        wordLabel.setText(getDisplayedWord());
        // hearts.setText(getHeartsDisplay());
        hangmanPanel.repaint();
        usedLettersLabel.setText("Used Letters: " + new String(usedLetters).trim());
        
        if (heart == 0) {
            wordLabel.setText("You lost! Word: " + randomWord);
            wordLabel.setBackground(Color.RED);
            submitButton.setEnabled(false);
            playSound("sounds/loser.wav");
        
            int result = JOptionPane.showConfirmDialog(
                this, 
                "You lost! The word was: " + randomWord + "\nDo you want to play again?", 
                "Game Over", 
                JOptionPane.YES_NO_OPTION,
                JOptionPane.WARNING_MESSAGE
            );
        
            if (result == JOptionPane.YES_OPTION) {
                restartGame();
            } else {
                System.exit(0); // Закрывает игру
            }
        }        
        if (randomWord.equals(new String(letters))) {
            wordLabel.setText("You win! Word: " + randomWord);
            wordLabel.setBackground(Color.GREEN);
            submitButton.setEnabled(false);
            playSound("sounds/winner.wav");
            int result = JOptionPane.showConfirmDialog(
                this, 
                "You WIN! The word was: " + randomWord + "\nDo you want to play again?", 
                "Game Over", 
                JOptionPane.YES_NO_OPTION,
                JOptionPane.WARNING_MESSAGE
            );
        
            if (result == JOptionPane.YES_OPTION) {
                restartGame();
            } else {
                System.exit(0); // Закрывает игру
            }
        }
    }

    private String getDisplayedWord() {
        return String.join(" ", new String(letters).split(""));
    }

    private String getHeartsDisplay() {
        return "Lives: " + "❤️ ".repeat(heart);
    }

    class HangmanPanel extends JPanel {
        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            
            Graphics2D g2 = (Graphics2D) g;
            g2.setStroke(new BasicStroke(5)); 
            g2.setColor(Color.BLACK);

            int panelWidth = getWidth();
            int panelHeight = getHeight();

            int baseX = panelWidth / 3 - 30; // Центрируем основание
            int baseY = panelHeight - 100;   // Поднимаем вверх на 100px

            // Основание
            g2.drawLine(baseX, baseY, baseX + 100, baseY);
            // Стойка
            g2.drawLine(baseX + 50, baseY, baseX + 50, baseY - 150);
            // Верхняя перекладина
            g2.drawLine(baseX + 50, baseY - 150, baseX + 130, baseY - 150);
            // Веревка
            g2.drawLine(baseX + 130, baseY - 150, baseX + 130, baseY - 130);

            // Рисуем части тела
            if (heart <= 5) g2.drawOval(baseX + 115, baseY - 130, 30, 30); // Голова
            if (heart <= 4) g2.drawLine(baseX + 130, baseY - 100, baseX + 130, baseY - 50); // Тело
            if (heart <= 3) g2.drawLine(baseX + 130, baseY - 90, baseX + 110, baseY - 70); // Левая рука
            if (heart <= 2) g2.drawLine(baseX + 130, baseY - 90, baseX + 150, baseY - 70); // Правая рука
            if (heart <= 1) g2.drawLine(baseX + 130, baseY - 50, baseX + 110, baseY - 20); // Левая нога
            if (heart == 0) g2.drawLine(baseX + 130, baseY - 50, baseX + 150, baseY - 20); // Правая нога
        }
    }

    private void restartGame() {
        initializeGame();
        submitButton.setEnabled(true);
        updateGUI();
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new HangMan().setVisible(true));
    }
}
