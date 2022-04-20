import java.util.*;

class F {
    public static void main(String[ ] args) {
        int soma = 0;
        int somapares = 0;
        int somaimpares = 0;
        Scanner scanThis = new Scanner(System.in);
        System.out.print("");
        int N = Integer.parseInt(scanThis.nextLine());
        String Ni[] = (scanThis.nextLine()).split(" ");
        System.out.print("");
        int M = Integer.parseInt(scanThis.nextLine());
        String Mi[] = (scanThis.nextLine()).split(" ");
        
        for (String l : Mi) {
            int l1 = Integer.parseInt(l);
            for (int i = 0; i < N; i++) {
                soma = l1 + Integer.parseInt(Ni[i]);
                if (soma % 2 == 0) {
                    somapares += 1;
                }
                else {
                    somaimpares += 1;
                }
            }
        }

        System.out.println(somapares + " " + somaimpares);
    }
}