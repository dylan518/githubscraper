import org.apache.http.HttpEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.conn.ssl.NoopHostnameVerifier;
import org.apache.http.conn.ssl.SSLConnectionSocketFactory;
import org.apache.http.conn.ssl.TrustStrategy;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.ssl.SSLContextBuilder;
import org.apache.http.util.EntityUtils;
import org.junit.Test;

import javax.net.ssl.SSLContext;
import javax.net.ssl.TrustManager;
import javax.net.ssl.X509TrustManager;
import java.security.cert.CertificateException;
import java.security.cert.X509Certificate;

public class HttpsDemo {

    @Test
    public void httpsTrustAll() throws Exception {
        String url = "https://localhost:8443/";
        // https单向连接，信任服务端
        HttpClientBuilder b = HttpClientBuilder.create();
        SSLContext sslContext = new SSLContextBuilder().loadTrustMaterial(null, new TrustStrategy() {
            public boolean isTrusted(X509Certificate[] arg0, String arg1) throws CertificateException {
                return true;
            }
        }).build();
        SSLConnectionSocketFactory sslSocketFactory = new SSLConnectionSocketFactory(sslContext,
                NoopHostnameVerifier.INSTANCE);
        CloseableHttpClient httpclient = HttpClients.custom().setSSLSocketFactory(sslSocketFactory).build();
        HttpGet httpGet = new HttpGet(url);
        try (CloseableHttpResponse response = httpclient.execute(httpGet)) {
            System.out.println(response.getStatusLine()); // 获取响应状态,比如 HTTP/1.1 200 OK
            HttpEntity entity = response.getEntity(); // 获取响应结果
            String rtn = EntityUtils.toString(entity); // 将结果转换为字符串
            System.out.println(rtn);
            EntityUtils.consume(entity); // 如果返回内容是输入流类型， 关闭输入流
        }
    }
    @Test
    public void httpsNoCheck() throws Exception {
        String url = "https://localhost:8443/";
        X509TrustManager trustManager = new X509TrustManager() {
            @Override
            public X509Certificate[] getAcceptedIssuers() {
                return null;
            }

            @Override
            public void checkClientTrusted(X509Certificate[] xcs, String str) {
            }

            @Override
            public void checkServerTrusted(X509Certificate[] xcs, String str) {
            }
        };
        SSLContext ctx = SSLContext.getInstance(SSLConnectionSocketFactory.TLS);
        ctx.init(null, new TrustManager[] { trustManager }, null);
        SSLConnectionSocketFactory sslSocketFactory = new SSLConnectionSocketFactory(ctx,
                NoopHostnameVerifier.INSTANCE);
        CloseableHttpClient httpclient = HttpClients.custom().setSSLSocketFactory(sslSocketFactory).build();
        HttpGet httpGet = new HttpGet(url);
        try (CloseableHttpResponse response = httpclient.execute(httpGet)) {
            System.out.println(response.getStatusLine()); // 获取响应状态,比如 HTTP/1.1 200 OK
            HttpEntity entity = response.getEntity(); // 获取响应结果
            String rtn = EntityUtils.toString(entity); // 将结果转换为字符串
            System.out.println(rtn);
            EntityUtils.consume(entity); // 如果返回内容是输入流类型， 关闭输入流
        }
    }

}
