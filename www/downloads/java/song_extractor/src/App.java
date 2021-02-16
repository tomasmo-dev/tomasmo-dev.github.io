import java.io.File;
import java.io.IOException;
import java.lang.reflect.Array;
import java.nio.file.Files;
import java.util.Arrays;
import java.util.Random;

public class App {

    public static void main(String[] args) {

        final String OsuPath = "YOUR OSU SONG PATH HERE";
        final String ExtractToPath = "WHERE YOU WANT TO COPY YOUR SONGS TO";
	
        final String ExtensionSplit = "mp3";

        File[] f = new File(OsuPath).listFiles();
        String[] songDirs = new File(OsuPath).list();

        // for (File fileInFiles : f) {
        // System.out.println(fileInFiles.getAbsolutePath());
        // }
            
        // for (int x=0; x < songDirs.length; x++)
        // {
        // System.out.println(String.format("%d - %s", x, songDirs[x].split(" ",
        // 2)[1]));
        // }
        // System.out.println(songDirs[songDirs.length - 1]);
        // System.out.println(songDirs.length);

        for (int a = 0; a < songDirs.length; a++) {

            String tempVal;

            System.out.println(a);
            String[] tempFile = new File(f[a].toString()).list();

            for (String tempF : tempFile) {
                String[] tempExt = tempF.split("\\.");

                if (tempExt.length > 1){
                    tempVal = tempExt[1];
    
                    if (tempVal.equals(ExtensionSplit)){
                        // System.out.println(String.format("%s\\%s\\%s", OsuPath, f[a].getName(), tempExt[0] + ".mp3"));
                        // System.out.println(String.format("%s%s\\%s", ExtractToPath, f[a].getName(), tempExt[0] + ".mp3"));
                        String fName = f[a].getName().split(" ", 2)[1];

                        File source = new File(String.format("%s\\%s\\%s", OsuPath, f[a].getName(), tempExt[0] + ".mp3"));
                        File dest = new File(String.format("%s%s\\%s", ExtractToPath, fName, tempExt[0] + ".mp3"));

                        try {
                            Files.createDirectories(dest.toPath().getParent());
                            Files.copy(source.toPath(), dest.toPath());
                            
                        } catch (IOException e) {
                            System.err.println(e);
                        }
        
                    }
                }
            }

        }

    }

}
