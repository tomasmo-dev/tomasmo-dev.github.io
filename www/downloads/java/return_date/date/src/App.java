import java.sql.Date;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
class getTime{
    public static String getNformatTime(){
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-dd-MM");

        LocalDateTime time = LocalDateTime.now();

        return time.format(formatter);
    }
}

public class App {
    public static void main(String[] args){
        
        System.out.println(getTime.getNformatTime());

    }
}
