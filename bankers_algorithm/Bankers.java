public class Bankers {

    final static int PID_IDX = 6; // process id

    public static void main(String[] args) {
        
        int[] avail = {3, 3, 2};
        int[][] proc = {
            {0, 1, 0, 7, 5, 3, 0},
            {2, 0, 0, 3, 2, 2, 1},
            {3, 0, 2, 9, 0, 2, 2},
            {2, 1, 1, 2, 2, 2, 3},
            {0, 0, 2, 4, 3, 3, 4},
        };
        
        int[][] result = get_bankers(proc, avail);

        if (result != null) {
            // Print in order the solution
            System.out.print("Solution: ");
            for (int i = result.length - 1; i >= 0; i --) {
                int[] p = proc[i];
                System.out.print("P" + p[PID_IDX] + " ");
            }
        }
        else System.out.println("There is no way to complete the algorithm for the given processes");
    }

    public static int[][] get_bankers(int[][] proc, int[] avail) {
        int seg_idx = proc.length; // segment, elements to the right of it are completed
        int i = 0;

        while (i < seg_idx && seg_idx > 0) {
            int[] curr_proc = proc[i];
            int res_to_use[] = {
                curr_proc[0] + avail[0],
                curr_proc[1] + avail[1],
                curr_proc[2] + avail[2]
            };

            // Check if the amount availble can complete this process
            if (res_to_use[0] >= curr_proc[3] && 
            res_to_use[1] >= curr_proc[4] && 
            res_to_use[2] >= curr_proc[5]) {
                // Complete the process and free resources
                System.out.println("P" + curr_proc[PID_IDX] + " completed");
                avail[0] += curr_proc[0];
                avail[1] += curr_proc[1];
                avail[2] += curr_proc[2];
                
                // move segment down, Swap process with one at end
                seg_idx --;
                proc[i] = proc[seg_idx];
                proc[seg_idx] = curr_proc;

                i = 0;
            }
            else i ++;
        }

        if (seg_idx == 0)
            return proc;

        return null;
    }
}