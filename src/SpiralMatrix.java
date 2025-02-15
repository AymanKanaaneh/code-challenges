//https://leetcode.com/problems/spiral-matrix/?envType=study-plan-v2&envId=top-interview-150

import java.util.ArrayList;
import java.util.List;

class SpiralMatrix {

    enum Directions {
        RIGHT,
        DOWN,
        LEFT,
        UP
    }

    public List<Integer> spiralOrder(int[][] matrix) {

        List<Integer> spiralMatrix = new ArrayList<>();
        int rows = matrix.length;
        int columns = matrix[0].length;
        int r = 0;
        int c = 0;
        Directions d = Directions.RIGHT;
        int visitedVal = 101;

        for (int i = 0; i < rows * columns; ++i) {

            spiralMatrix.add(matrix[r][c]);
            matrix[r][c] = visitedVal;

            switch (d) {

                case RIGHT:
                    ++c;
                    if (c == columns || matrix[r][c] == visitedVal) {
                        --c;
                        ++r;
                        d = Directions.DOWN;
                    }
                    break;
                case DOWN:
                    ++r;
                    if (r == rows || matrix[r][c] == visitedVal) {
                        --r;
                        --c;
                        d = Directions.LEFT;
                    }
                    break;
                case LEFT:
                    --c;
                    if (c < 0 || matrix[r][c] == visitedVal) {
                        ++c;
                        --r;
                        d = Directions.UP;
                    }
                    break;
                case UP:
                    --r;
                    if (r < 0 || matrix[r][c] == visitedVal) {
                        ++r;
                        ++c;
                        d = Directions.RIGHT;
                    }
                    break;

            }

        }

        return spiralMatrix;
    }
}
