import org.eclipse.jetty.http3.api.Session;
import org.eclipse.jetty.http3.server.HTTP3ServerConnector;
import org.eclipse.jetty.http3.server.RawHTTP3ServerConnectionFactory;
import org.eclipse.jetty.util.ssl.SslContextFactory;

public class Server {
    public static void main(String[] args) {
        // Create a Server instance.
        org.eclipse.jetty.server.Server server = new org.eclipse.jetty.server.Server();

// HTTP/3 is always secure, so it always need a SslContextFactory.
        SslContextFactory.Server sslContextFactory = new SslContextFactory.Server();
        sslContextFactory.setKeyStorePath("c:/csStudy");
        sslContextFactory.setKeyStorePassword("secret");

// The listener for session events.
        Session.Server.Listener sessionListener = new Session.Server.Listener() {};

// Create and configure the RawHTTP3ServerConnectionFactory.
        RawHTTP3ServerConnectionFactory http3 = new RawHTTP3ServerConnectionFactory(sessionListener);
        http3.getHTTP3Configuration().setStreamIdleTimeout(15000);

// Create and configure the HTTP3ServerConnector.
        HTTP3ServerConnector connector = new HTTP3ServerConnector(server, sslContextFactory, http3);
// Configure the max number of requests per QUIC connection.
        connector.getQuicConfiguration().setMaxBidirectionalRemoteStreams(1024);

// Add the Connector to the Server.
        server.addConnector(connector);

// Start the Server so it starts accepting connections from clients.
        try {
            server.start();
        } catch (Exception e) {
            System.out.println("[에러] : " + e.getMessage());
        }
    }
}
