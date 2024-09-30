
import java.io.*;
import java.util.*;

/**
 * N개의 섬으로 이루어진 나라
 * 몇 개의 섬 사이에는 다리가 설치됨
 * 2개의 섬에 공장을 세움 -> 다른 공장으로 생산 중인 물품 수송 필요
 * 다리마다 중량 제한이 있음
 * 초과하면 무너짐
 * 한 번 이동에서 옮길 수 있는 중량의 최댓값 구하기
 * <p>
 * 언제 이분 탐색을 푸느냐?
 * 최적의 값(매개 변수)를 찾고 싶을 때,
 * 시뮬레이션을 통해서 가능 여부를 판단할 수 있으면!
 * 그리고 해당 시뮬레이션은 따로 함수로 구현하면 편함!
 * 이분 탐색 자체가 걸리는 시간은 가질 수 있는 MAX 값의 log!
 * 지금은 log(C)
 * 그런데 이 이분 탐색을 하는 데에 내부에서 BFS를 함
 * NLogM (N은 노드 수, M은 edge
 */

public class Main {
    int n, m;
    int a, b, c;
    int s, e;
    HashMap<Integer, HashMap<Integer, Integer>> h = new HashMap<>();

    public boolean test(int value) {

        int cur = s;
        boolean[] visited = new boolean[n + 1];
        visited[cur] = true;

        Queue<Integer> q = new LinkedList<>();
        q.offer(cur);

        while (!q.isEmpty()) {
            cur = q.poll();
            for (int node : h.get(cur).keySet()) {
                if (visited[node] || h.get(cur).get(node) < value) {
                    continue;
                }

                if (node == e) {
                    return true;
                }

                visited[node] = true;
                q.offer(node);

            }
        }
        return false;
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for (int i = 1; i < n + 1; i++) {
            h.put(i, new HashMap<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            h.get(a).put(b, c);
            h.get(b).put(a, c);
        }
        st = new StringTokenizer(br.readLine());
        s = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());

        int start = 0;
        int end = 1000000000;

        int mid = (end + start) / 2;
        int answer = end;

        while (start <= end) {
            if (test(mid)) {
                start = mid + 1;
                answer = mid;
            } else {
                end = mid - 1;
            }
            mid = (end + start) / 2;
        }

        System.out.println(answer);
    }

    public static void main(String args[]) throws Exception {
        new Main().solution();
    }
}
