public class ASCIIStringProgram {
    public static void main(String[] args) {
        String inputString = "Hello, ASCII!";

        System.out.println("Original String: " + inputString);

        System.out.print("ASCII Values: ");
        for (int i = 0; i < inputString.length(); i++) {
            char character = inputString.charAt(i);
            int asciiValue = (int) character;
            System.out.print(asciiValue + " ");

        System.out.println("\nDecoded String: " + decodeASCII(inputString));
    }
    }
    private static String decodeASCII(String input) {
        StringBuilder decodedString = new StringBuilder();

        for (String asciiValue : input.split(" ")) {
            int intValue = Integer.parseInt(asciiValue);
            decodedString.append((char) intValue);
        }

        return decodedString.toString();
    }
}
