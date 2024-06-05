public class nptel extends Thread {
public void run() {
    for (int i = 1; i < 5; i++) {
 System.out.print("i++ + ");
    }
     }
      public static void main(String []args) {
      nptel t1 = new nptel();
      t1.run();
    }
}
