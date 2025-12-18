package com.alihmzyv.logservice.mapper.impl;

import com.alihmzyv.logservice.mapper.LogMapper;
import com.alihmzyv.logservice.proto.CreateLogRequest;
import com.alihmzyv.logservice.tables.records.LogRecord;
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import org.jooq.DSLContext;
import org.jooq.JSONB;
import org.springframework.stereotype.Component;

import java.time.LocalDateTime;
import java.time.ZoneId;

import static com.alihmzyv.logservice.Tables.LOG;

@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
@RequiredArgsConstructor
@Component
public class LogMapperImpl implements LogMapper {
    DSLContext dslContext;

    @Override
    public LogRecord toRecord(CreateLogRequest createLogRequest) {
        if (createLogRequest == null) {
            return null;
        }

        LogRecord logRecord = dslContext.newRecord(LOG)
                .setCreatedAt(LocalDateTime.now().atZone(ZoneId.systemDefault()).toLocalDateTime())
                .setOperationService((short) createLogRequest.getOperationService())
                .setOperationType((short) createLogRequest.getOperationType())
                .setUsername(createLogRequest.getUsername())
                .setJsonData(JSONB.jsonbOrNull(createLogRequest.getJson()));

        if (createLogRequest.hasCashierCode()) { //cashier code is optional
            logRecord.setCashierCode(createLogRequest.getCashierCode());
        }

        return logRecord;
    }
}
