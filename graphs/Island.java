public class Island {

    public static void main(String[] args) {
        int[][] grid = new int[][]{
            {1, 1, 0, 0, 0},
            {1, 1, 0, 0, 0},
            {0, 0, 1, 0, 0},
            {0, 0, 0, 1, 1}
        };
        int n = grid.length;
        int m = grid[0].length;
        Island island = new Island();
        System.out.println(island.numIslands(grid,n,m));
    }
private void visit(int[][] grid,int i, int j,int n,int m) {
    if(grid[i][j] == 0)return;     
    grid[i][j] = 0;
    if (i != 0 && (grid[i - 1][j] == 1))visit(grid, i-1, j,n,m);
    if (j != 0 && (grid[i][j-1] == 1))visit(grid, i, j-1,n,m);
    if (i != n-1 && (grid[i+1][j] == 1))visit(grid, i+1, j,n,m);
    if (j != m-1 && (grid[i][j+1] == 1))visit(grid, i, j+1,n,m);

}
public int numIslands(int[][] grid,int n,int m) {
    int count = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == 1) {
                count++;
                visit(grid, i, j,n,m);
            }
        }
    }
    return count;
}
}