public class StringToASCIIProgram {
    public static void main(String[] args) {
        String inputString = "I am going to school";

        // Display the original string
        System.out.println("Original String: " + inputString);

        // Convert string to ASCII values
        System.out.print("ASCII Values: ");
        for (int i = 0; i < inputString.length(); i++) {
            char character = inputString.charAt(i);
            int asciiValue = (int) character;
            System.out.print(asciiValue + " ");
 }
}
}