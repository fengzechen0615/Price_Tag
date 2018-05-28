import java.io.IOException;
import java.net.InetSocketAddress;

public class test {

    public static void main(String[] args) throws IOException {


        HelloService service = RPCClient.getRemoteProxyObj(HelloService.class, new InetSocketAddress("172.20.10.9", 8089));
        System.out.println(service.sayHi("test"));
    }
}
