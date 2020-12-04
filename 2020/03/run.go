package main

import (
    "log"
    "bufio"
    "os"
    "fmt"
)

// readLines reads a whole file into memory
// and returns a slice of its lines.
func readLines(path string) ([][]bool, error) {
    file, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer file.Close()

    var lines [][]bool
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        line := scanner.Text()
        boolGrid := make([]bool, len(line))
        for i, char := range line {
            if char == '#' {
                boolGrid[i] = true
            } else {
                boolGrid[i] = false
            }
        }
        lines = append(lines, boolGrid)
    }
    return lines, scanner.Err()
}

func part1(grid [][]bool, skip int) int {
    count := 0
    for i, row := range grid {
        idx := (i * skip) % len(row)
        if row[idx] {
            count += 1
        }
    }
    return count
}

func skip2Vert(grid [][]bool) int {
    count := 0
    for i := 0; i < len(grid); i += 2 {
        idx := (i / 2) % len(grid[i])
        if grid[i][idx] {
            count += 1
        }
    }
    return count
}

func main() {
    if len(os.Args) < 2 {
        log.Fatal("Usage: go run run.go <relative_path_to_input_file>")
    }
    grid, err := readLines(os.Args[1])
    if err != nil {
        log.Fatal(err)
    }

    trees := part1(grid, 3)
    fmt.Printf("Total trees in path (part 1): %d\n", trees)

    trees = part1(grid, 1) * part1(grid, 3) * part1(grid, 5) * part1(grid, 7) * skip2Vert(grid)
    fmt.Printf("Total trees in path (part 2): %d\n", trees)
}
