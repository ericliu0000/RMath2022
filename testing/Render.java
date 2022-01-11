import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Render {
    public static void main(String[] args) {
        long startTime = System.nanoTime();

        ExecutorService executor = Executors.newFixedThreadPool(8);
        File cwd = new File(".");

        ArrayList<String> files = new ArrayList<String>();
        ArrayList<String> ignore = new ArrayList<String>(Arrays.asList(new String[] {"constants.py", "renderAll.py"}));

        // Get all Python files in directory not in exclude 
        for (File i : cwd.listFiles()) {
            String name = i.getName();
            if (name.endsWith(".py") && !ignore.contains(name)) {
                files.add(name);
            }
        }

        // Start new thread for rendering each file
        for (String file : files) {
            executor.submit(() -> {
                try {
                    ProcessBuilder pb = new ProcessBuilder("manim", file);
                    System.out.println("Rendering " + file);
                    // pb.inheritIO();
                    Process p = pb.start();
                    p.waitFor();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            });
        }

        executor.shutdown();

        // Wait for all threads to finish
        try {
            if (!executor.awaitTermination(1000, java.util.concurrent.TimeUnit.SECONDS)) {
                executor.shutdownNow();
                System.out.println("Stopped!!!");
            }
        } catch (InterruptedException e) {
            executor.shutdownNow();
            System.err.println("Interrupted");
            Thread.currentThread().interrupt();
        }

        System.out.println("Done! " + (double)(System.nanoTime() - startTime) / 1000000000 + "s");
    }
}