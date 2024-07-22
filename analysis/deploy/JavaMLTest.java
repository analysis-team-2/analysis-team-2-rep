import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

public class JavaMLTest {

    public static void main(String[] args) {
        try {
            // 파이썬 스크립트 실행
            ProcessBuilder processBuilder = new ProcessBuilder("python3", "deploy.py");
            processBuilder.redirectErrorStream(true);
            Process process = processBuilder.start();

            // JSON 입력 데이터 생성
            String jsonInputString = "{"
                    + "\"admi_cty_no\": [41210510],"
                    + "\"card_tpbuz_cd\": [\"D05\"],"
                    + "\"cnt\": [28],"
                    + "\"TOTAL_POPULATION\": [13850.98],"
                    + "\"운영점포평균영업기간\": [188.5],"
                    + "\"폐업점포평균영업기간\": [358.0],"
                    + "\"상권변동지표구분\": [\"HH\"]"
                    + "}";

            // 파이썬 프로세스의 입력 스트림에 데이터 쓰기
            try (OutputStream os = process.getOutputStream()) {
                os.write(jsonInputString.getBytes(StandardCharsets.UTF_8));
                os.flush();
            }

            // 파이썬 프로세스의 출력 스트림에서 결과 읽기
            StringBuilder output = new StringBuilder();
            try (Scanner scanner = new Scanner(process.getInputStream(), StandardCharsets.UTF_8.name())) {
                while (scanner.hasNextLine()) {
                    output.append(scanner.nextLine());
                }
            }

            // 결과 출력
            System.out.println("Response: " + output.toString());

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
