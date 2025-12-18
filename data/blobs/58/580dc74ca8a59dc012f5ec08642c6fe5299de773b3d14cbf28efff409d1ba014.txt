package com.ams.api.util;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.PropertySource;
import org.springframework.stereotype.Component;

import lombok.Data;

@Component(value = "GlobalProperties")
@PropertySource(value = "classpath:global.properties")
@PropertySource(value = "file:/deployments/global/global.properties", ignoreResourceNotFound = true, name = "remoteConfigProps")
@Data
public class GlobalProperties {

	@Value("${global.logging}")
	private boolean globalLog;

	@Value("${global.audit}")
	private boolean globalAudit;

	@Value("${allowed.domains}")
	private String allowedDomains;

	@Value("${global.auditLog}")
	private boolean globalAuditLog;

	@Value("${global.header}")
	private boolean globalHeader;

	@Value("${global.authorization}")
	private boolean isAuthorizationNeeded;

	@Value("${global.txnKeyValidation}")
	private boolean txnKeyValidation;
}
