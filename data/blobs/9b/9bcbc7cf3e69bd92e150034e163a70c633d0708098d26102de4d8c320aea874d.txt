package inmobi.jobscheduling;  
  /*   
   Bluemoon
   11/04/22 2:27 PM  
   */

public abstract class AbstractJob implements Runnable {
    private String jobName;
    private JobPriority priority;
    private String ownerId;

    public AbstractJob(String jobName, JobPriority priority) {
        this.jobName = jobName;
        this.priority = priority;
    }

    public String getJobName() {
        return jobName;
    }

    public AbstractJob _setJobName(String jobName) {
        this.jobName = jobName;
        return this;
    }

    public JobPriority getPriority() {
        return priority;
    }

    public AbstractJob _setPriority(JobPriority priority) {
        this.priority = priority;
        return this;
    }

    public String getOwnerId() {
        return ownerId;
    }

    public AbstractJob _setOwnerId(String ownerId) {
        this.ownerId = ownerId;
        return this;
    }
}
