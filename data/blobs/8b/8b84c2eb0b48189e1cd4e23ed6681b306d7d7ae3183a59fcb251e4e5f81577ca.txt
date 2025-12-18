package com.airbyte.api.models.shared;

import com.fasterxml.jackson.annotation.JsonInclude.Include;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;

/**
 * DestinationAmazonSqs
 * The values required to configure the destination.
**/
public class DestinationAmazonSqs {
    @JsonInclude(Include.NON_ABSENT)
    @JsonProperty("access_key")
    public String accessKey;
    public DestinationAmazonSqs withAccessKey(String accessKey) {
        this.accessKey = accessKey;
        return this;
    }
    
    @JsonProperty("airbyte-destination-name")
    public DestinationAmazonSqsAmazonSqsEnum airbyteDestinationName;
    public DestinationAmazonSqs withAirbyteDestinationName(DestinationAmazonSqsAmazonSqsEnum airbyteDestinationName) {
        this.airbyteDestinationName = airbyteDestinationName;
        return this;
    }
    
    @JsonInclude(Include.NON_ABSENT)
    @JsonProperty("message_body_key")
    public String messageBodyKey;
    public DestinationAmazonSqs withMessageBodyKey(String messageBodyKey) {
        this.messageBodyKey = messageBodyKey;
        return this;
    }
    
    @JsonInclude(Include.NON_ABSENT)
    @JsonProperty("message_delay")
    public Long messageDelay;
    public DestinationAmazonSqs withMessageDelay(Long messageDelay) {
        this.messageDelay = messageDelay;
        return this;
    }
    
    @JsonInclude(Include.NON_ABSENT)
    @JsonProperty("message_group_id")
    public String messageGroupId;
    public DestinationAmazonSqs withMessageGroupId(String messageGroupId) {
        this.messageGroupId = messageGroupId;
        return this;
    }
    
    @JsonProperty("queue_url")
    public String queueUrl;
    public DestinationAmazonSqs withQueueUrl(String queueUrl) {
        this.queueUrl = queueUrl;
        return this;
    }
    
    @JsonProperty("region")
    public DestinationAmazonSqsAWSRegionEnum region;
    public DestinationAmazonSqs withRegion(DestinationAmazonSqsAWSRegionEnum region) {
        this.region = region;
        return this;
    }
    
    @JsonInclude(Include.NON_ABSENT)
    @JsonProperty("secret_key")
    public String secretKey;
    public DestinationAmazonSqs withSecretKey(String secretKey) {
        this.secretKey = secretKey;
        return this;
    }
    
}
