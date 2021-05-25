import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Objects;

public class Main {

    private static long last = 0;

    private static int randomNumber(int max) {
        last = (25214903917l * last + 11l) % 281474976710656l;
        long tmp = (last >= 0) ? last : -last;
        return (int) (tmp % ((long) max));
    }

    private static List<Integer> createArray(int len, int maxValue) {
        List<Integer> p_array = new ArrayList<>(len);
        for (int i = 0; i < len; i++) {
            p_array.add(randomNumber(maxValue));
        }
        return p_array;
    }

    public static void main(String[] args) {
        int tabSize = 10000000;
        int maxValue = 5000000;
        boolean noOutput = false;
        boolean debug = false;

        for (String s : args) {
            if (Objects.equals(s, "--nooutput")) {
                noOutput = true;
            } else if (s != null && s.startsWith("--nbop=")) {
                int nb = Integer.parseInt(s.substring(7));
                if (nb > 0) {
                    tabSize = nb;
                }
            } else if (Objects.equals(s, "--debug")) {
                debug = true;
            }
        }

        if (debug) {

            for (int i = 0; i < args.length; i++) {
                System.out.printf("   argv[%d] : '%s'\n", i, args[i]);
            }
            System.out.printf("lang=java;tabSize=%d;maxValue=%d;noOutput=%b;debug=%b\n", tabSize, maxValue, noOutput,
                    debug);
        }

        // Our arr contains 8 elements
        List<Integer> arr = createArray(tabSize, maxValue);

        Collections.sort(arr);

        if (!noOutput) {
            System.out.printf("Modified arr[] : \n");
            int i = 0;
            for (i = 0; i < arr.size() && i < 10; ++i) {
                System.out.printf("%d ", arr.get(i));
            }
            if (i < arr.size()) {
                System.out.printf("...");
            }
            System.out.printf("\n");
        }

    }
}