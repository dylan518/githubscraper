package com.javarush.rogulenko.cryptoanalizer.util;
import com.javarush.rogulenko.cryptoanalizer.constants.Alphabet;
import com.javarush.rogulenko.cryptoanalizer.entity.Result;
import com.javarush.rogulenko.cryptoanalizer.entity.ResultCode;
import com.javarush.rogulenko.cryptoanalizer.exceptions.AppException;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class FileActionHandler {

    public Result processFileWithKey(String sourceFilePath, String targetFilePath, int key) {
        Path sourcePath = getPath(sourceFilePath);
        Path targetPath = getPath(targetFilePath);

        try (BufferedReader bufferedReader = Files.newBufferedReader(sourcePath);
             BufferedWriter bufferedWriter = Files.newBufferedWriter(targetPath)) {

            int charValue;
            int alphabetLength = Alphabet.CHARS.length;

            // Чтение и обработка каждого символа из исходного файла
            while ((charValue = bufferedReader.read()) != -1) {
                char character = Character.toLowerCase((char) charValue);

                if (Alphabet.index.containsKey(character)) {
                    int newIndex = (Alphabet.index.get(character) + key) % alphabetLength;
                    // Обеспечить положительный индекс
                    if (newIndex < 0) {
                        newIndex += alphabetLength;
                    }
                    bufferedWriter.write(Alphabet.CHARS[newIndex]);
                } else {
                    bufferedWriter.write(character);
                }
            }
        } catch (IOException e) {
            throw new AppException("Error processing file: " + e.getMessage(), e);
        }

        return new Result(targetFilePath, ResultCode.OK);
    }

    private Path getPath(String filename) {
        Path path = Path.of(filename);
        return path.isAbsolute() ? path : Path.of(System.getProperty("user.dir") + File.separator + "text" + File.separator + filename);
    }

}
