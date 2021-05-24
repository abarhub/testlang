import java.util.Arrays;
 
public class Main
{
    
    private static long last = 0;

    private static int randomNumber(int max)
{
    last = (25214903917l * last + 11l) % 281474976710656l;
    long tmp = (last >= 0) ? last : -last;
    int tmp2=(int)tmp;
    tmp2=(tmp2>=0)?tmp2:-tmp2;
    return tmp2 % max;
}

private static int[] createArray(int len, int maxValue)
{
    int p_array[] = new int[len];
    for (int i = 0; i < len; i++)
    {
        p_array[i] = randomNumber(maxValue);
    }
    return p_array;
}

    public static void main(String[] args)
    {
        int tabSize = 10000000;
        int maxValue = 5000000;
    
        // Our arr contains 8 elements
        int[] arr = createArray(tabSize,maxValue);
 
        Arrays.sort(arr);
 
        //System.out.printf("Modified arr[] : %s\n",
                          //Arrays.toString(arr));
        System.out.printf("Modified arr[] : \n");
        int i = 0;
        for (i = 0; i < arr.length && i < 10; ++i)
        {
            System.out.printf("%d ", arr[i]);
        }
        if (i < arr.length)
        {
            System.out.printf("...");
        }
        System.out.printf("\n");

    }
}