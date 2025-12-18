package ru.otus.service;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import ru.otus.service.interfaces.IOService;

import java.io.InputStream;
import java.io.PrintStream;
import java.util.Scanner;

@Service
public class IOServiceStreams implements IOService {
    private final Scanner input;
    private final PrintStream output;

    public IOServiceStreams(@Value("${io.in}") InputStream input,
                            @Value("${io.out}") PrintStream output) {
        this.input = new Scanner(input);
        this.output = output;
    }

    @Override
    public void println(String text) {
        output.println(text);
    }

    @Override
    public String readLine() {
        return input.nextLine();
    }

}
