import javax.management.Notification;
import javax.management.NotificationBroadcaster;

public class Notification_14 {
    public static void main(String[] args) {
        NotificationBroadcaster broadcaster = new NotificationBroadcaster() {
            @Override
            public void sendNotification(Notification notification) {
                // Implementation not needed for this example
            }
        };

        Notification notification = new Notification("Test", broadcaster, 0);
        notification.setUserData("User data");

        System.out.println(notification.getUserData());
    }
}
