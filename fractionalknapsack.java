import java.util.*;

class Item implements Comparable<Item> {
    int weight;
    int profit;

    public Item(int weight, int profit) {
        this.weight = weight;
        this.profit = profit;
    }

    @Override
    public int compareTo(Item other) {
        double ratio1 = (double) this.profit / this.weight;
        double ratio2 = (double) other.profit / other.weight;
        if (ratio1 < ratio2)
            return 1;
        else if (ratio1 > ratio2)
            return -1;
        else
            return 0;
    }
}

public class fractionalknapsack {
    public static double getMaxProfit(Item[] items, int capacity) {
        Arrays.sort(items);

        double totalProfit = 0;
        double totalWeight = 0;

        for (Item item : items) {
            if (capacity - item.weight >= 0) {
                capacity -= item.weight;
                totalProfit += item.profit;
                totalWeight += item.weight;
            } else {
                double fraction = (double) capacity / item.weight;
                totalProfit += fraction * item.profit;
                totalWeight += fraction * item.weight;
                break;
            }
        }

        System.out.println("Total weight in knapsack: " + totalWeight);
        System.out.println("Total profit in knapsack: " + totalProfit);

        return totalProfit;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of items: ");
        int n = scanner.nextInt();

        Item[] items = new Item[n];
        for (int i = 0; i < n; i++) {
            System.out.print("Enter weight of item " + (i + 1) + ": ");
            int weight = scanner.nextInt();
            System.out.print("Enter profit of item " + (i + 1) + ": ");
            int profit = scanner.nextInt();
            items[i] = new Item(weight, profit);
        }

        System.out.print("Enter the capacity of knapsack: ");
        int capacity = scanner.nextInt();

        double maxProfit = getMaxProfit(items, capacity);
        System.out.println("Maximum profit we can obtain = " + maxProfit);

        // Calculate the average value of profit and weight
        int totalProfit = 0;
        int totalWeight = 0;
        for (Item item : items) {
            totalProfit += item.profit;
            totalWeight += item.weight;
        }
        double avgProfit = (double) totalProfit / items.length;
        double avgWeight = (double) totalWeight / items.length;

        System.out.println("Average value of profit: " + avgProfit);
        System.out.println("Average value of weight: " + avgWeight);

        scanner.close();
    }
}
