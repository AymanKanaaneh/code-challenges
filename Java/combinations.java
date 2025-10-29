//https://leetcode.com/problems/combinations/


class Solution {
    public List<List<Integer>> combine(int n, int k) {

        // List to store the current combination being generated
        List<Integer> currComp = new ArrayList<>(Collections.nCopies(k, 0));

        // List to store all valid combinations
        List<List<Integer>> compList = new ArrayList<>();

        // Variable to store the previous size of the combination list
        int prevCompListSize = -1;

        // Pointer to track the index where changes will be made
        int currnetCompIndex = k - 1;

        // Initialize the first combination with sequential numbers (1, 2, ..., k)
        for (int i = 1; i <= k; ++i) {
            currComp.set(i - 1, i);
        }

        // Add the first combination to the list
        currComp = new ArrayList<>(currComp);
        compList.add(currComp);

        // Generate initial combinations by updating the last index (k-1) of the list
        for (int i = currnetCompIndex + 2; i <= n; ++i) {
            currComp = new ArrayList<>(currComp);
            currComp.set(currnetCompIndex, i);
            compList.add(currComp);
        }

        // Move to the previous index to continue generating new combinations
        --currnetCompIndex;

        // Generate new combinations by modifying elements at different indices
        while (currnetCompIndex >= 0) {
            prevCompListSize = compList.size();

            // Iterate over each existing combination in the list
            for (int i = 0; i < prevCompListSize; ++i) {

                // Modify the current index to generate new combinations
                for (int j = currnetCompIndex + 2; j <= n; ++j) {

                    // Ensure the new value is valid by checking it against the next index value
                    if (j < compList.get(i).get(currnetCompIndex + 1)) {
                        currComp = new ArrayList<>(compList.get(i));
                        currComp.set(currnetCompIndex, j);
                        compList.add(currComp);
                    } else {
                        break; // Stop if the value is no longer valid
                    }
                }
            }

            // Move to the previous index to continue the process
            --currnetCompIndex;
        }

        // Return the list of all valid combinations
        return compList;
    }
}
