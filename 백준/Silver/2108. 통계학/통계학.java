import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
    private static List<Integer> arr = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int sum = 0;
        for (int i = 0; i < n; i++) {
            int item = sc.nextInt();
            sum += item;
            arr.add(item);
        }
        arr.sort(Integer::compareTo);
        int mid = arr.get(n / 2);
        PriorityQueue<Node> pq = new PriorityQueue<>();
        int i = 0;
        while (i < n) {
            int item = arr.get(i);
            int cnt= 0;
            while (i < n && item == arr.get(i) ) {
                cnt++;
                i++;
            }
            pq.offer(new Node(item, cnt));
        }
        
        Node node1 = pq.poll();
        int frequencyValue = node1.key;

       if(pq.size() > 1) {
            Node node2 = pq.poll();
            if (node1.cnt == node2.cnt)
                frequencyValue = node2.key;
        }

        System.out.println(Math.round((double)sum / arr.size()));
        System.out.println(mid);
        System.out.println(frequencyValue);
        System.out.println(arr.get(arr.size() - 1) - arr.get(0));
    }
}

class Node implements Comparable<Node>{
    int key;
    int cnt;

    public Node(int key, int cnt) {
        this.key = key;
        this.cnt = cnt;
    }

    @Override
    public int compareTo(Node o) {
        if (cnt == o.cnt)
            return key - o.key;
        return o.cnt - cnt;
    }

    @Override
    public String toString() {
        return key +","+ cnt;
    }
}
