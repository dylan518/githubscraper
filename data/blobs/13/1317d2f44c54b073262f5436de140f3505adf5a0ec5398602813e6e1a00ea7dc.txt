package com.privasia.poller.routes;

import com.privasia.poller.core.utils.Constants;
import com.privasia.poller.processors.MessagePersistProcessor;
import org.apache.camel.builder.RouteBuilder;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class SFTPPollerRoute extends RouteBuilder{

    @Autowired
    private MessagePersistProcessor messagePersistProcessor;

    @Override
    public void configure() throws Exception {

        log.info("SFTP Poller Route Starting ......................");

        from("sftp://mmswUser@192.168.1.232:22/OUT?password=mmsw" +
                "&delete=true" +
                "&initialDelay=5000" +
                "&delay=10000" +
                "&readLock=changed" +
                "&readLockTimeout=10000" +
                "&sortBy=file:modified" +
                "&filter=#fileReadyFilter" +
                "&runLoggingLevel=INFO" +
                "&disconnect=true" +
                "&passiveMode=true")
                .id("sftp-poller-route")

                .log("Connected to the SFTP server as mmswUser")
                .setHeader("sourceId", simple("SFTP"))
                .bean(messagePersistProcessor, "saveMessageTransaction")
                .log("MessageTransaction saved with ID: ${header." + Constants.MESSAGE_TX_ID + "}")
                .id("persisSFTPPollerMessage");


        log.info("SFTP Poller Route Ending ......................");
    }
}
