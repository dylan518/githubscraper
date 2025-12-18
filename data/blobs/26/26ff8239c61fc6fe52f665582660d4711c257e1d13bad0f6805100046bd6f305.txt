package io.k8s.api.flowcontrol.v1;

import java.util.List;

/**
 * FlowSchemaStatus represents the current state of a FlowSchema.
 */
public class FlowSchemaStatus {
  public List<FlowSchemaCondition> conditions;

  /**
   * `conditions` is a list of the current states of FlowSchema.
   */
  public FlowSchemaStatus conditions(List<FlowSchemaCondition> conditions) {
    this.conditions = conditions;
    return this;
  }

  public static FlowSchemaStatus flowSchemaStatus() {
    return new FlowSchemaStatus();
  }
}
