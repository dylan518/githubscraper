package com.example.collegeschedule.service.impl;

import com.example.collegeschedule.service.EmailService;
import jakarta.mail.internet.MimeMessage;
import lombok.RequiredArgsConstructor;
import lombok.SneakyThrows;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.mail.javamail.MimeMessageHelper;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class EmailServiceImpl implements EmailService {
    private final JavaMailSender mailSender;

    @Value("${spring.mail.username}")
    private String EMAIL_FROM;

    @SneakyThrows
    @Override
    public void sendMessage(String toEmail, String token) {
        MimeMessage message = mailSender.createMimeMessage();
        MimeMessageHelper helper = new MimeMessageHelper(message);

        helper.setFrom(EMAIL_FROM, "Поддержка от разработчика Арген");
        helper.setTo(toEmail);

        String subject = "Код для сброса пароля";
        String content = "<html>" +
                "<body style='font-family: Arial, sans-serif;'>" +
                "<h2 style='color: #333;'>Здравствуйте,</h2>" +
                "<p>Вы запросили сброс пароля.</p>" +
                "<p>Скопируйте код и вставьте, чтобы изменить пароль:</p>" +
                "<div style='font-size: 24px; font-weight: bold; color: #333; margin: 20px 0;'>" +
                token+
                "</div>" +
                "<p>Игнорируйте это письмо, если вы помните свой пароль " +
                "или если вы не запрашивали сброс пароля.</p>" +
                "<br>" +
                "<p>С уважением,<br>Поддержка от разработчика Арген</p>" +
                "</body>" +
                "</html>";

        helper.setSubject(subject);
        helper.setText(content, true);
        mailSender.send(message);
    }
}