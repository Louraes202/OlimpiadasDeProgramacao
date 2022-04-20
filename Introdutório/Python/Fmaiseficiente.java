import java.util.*;

class Fmaiseficiente {
    public static void main(String[ ] args) {
        int pares = 0;
        Scanner scanThis = new Scanner(System.in);
        System.out.print("");
        int N = Integer.parseInt(scanThis.nextLine());
        String Ni[] = (scanThis.nextLine()).split(" ");
        System.out.print("");
        int M = Integer.parseInt(scanThis.nextLine());
        String Mi[] = (scanThis.nextLine()).split(" ");
        
        for (String l : Ni ) {
            int l1 = Integer.parseInt(l);
            for (String k : Mi) {
                int k1 = Integer.parseInt(k);
                if (l1%2 == k1%2) {
                    pares += 1;

                }
            }
        }

        int calculo = (N * M) - pares;
        System.out.println(pares + " " + calculo);
    }
}