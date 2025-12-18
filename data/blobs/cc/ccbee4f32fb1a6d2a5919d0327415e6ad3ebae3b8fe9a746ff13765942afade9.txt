package com.daniel.ms_messaging.domain.usecase;

import com.daniel.ms_messaging.domain.api.ISendSmsServicePort;
import com.daniel.ms_messaging.domain.model.OrderMessage;
import com.daniel.ms_messaging.domain.spi.ISendSmsPersistencePort;

public class SendSmsUseCase implements ISendSmsServicePort {
    private final ISendSmsPersistencePort sendSmsPersistencePort;

    public SendSmsUseCase(ISendSmsPersistencePort sendSmsPersistencePort) {
        this.sendSmsPersistencePort = sendSmsPersistencePort;
    }

    @Override
    public boolean sendSms(OrderMessage orderMessage) {
        return sendSmsPersistencePort.sendSms(orderMessage);
    }
}
