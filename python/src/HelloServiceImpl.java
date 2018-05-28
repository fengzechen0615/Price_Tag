import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class HelloServiceImpl implements HelloService {
    public static void main (String[] args)  {
        String[] args1 = new String[]{
                "python", "/Users/kumbaya/IdeaProjects/python/src/Price.py", "水都物语"
        };

        try {
            Process pr = Runtime.getRuntime().exec(args1);
            pr.waitFor();
            BufferedReader in = new BufferedReader(new InputStreamReader(
                    pr.getInputStream()));
            String line;
            while ((line = in.readLine()) != null) {
                System.out.println(line);
            }
            in.close();
            pr.waitFor();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    public String getinfo(String name){
        return null;
    }
}
