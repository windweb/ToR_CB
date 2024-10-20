import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
public class GetTest {
@DisplayName("Тест get запроса в адрес yandex.ru")
@Test
void getUrl() throws Exception{
String url = "https://www.cbr.ru/";
String siteHeader = "Центральный банк Российской Федерации | Банк России";
URL obj = new URL(url);
HttpURLConnection connection;
connection = (HttpURLConnection) obj.openConnection();
connection.setRequestMethod("GET");
BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while((inputLine = in.readLine()) != null)
{ response.append(inputLine); }
in.close();
Assertions.assertNotNull(response.toString());
System.out.println(response.toString());
Assertions.assertTrue(response.toString().contains(siteHeader));
Assertions.assertTrue(response.toString().contains("https://www.cbr.ru/"));
}
}
