package main

import (
    "log"
    "bufio"
    "os"
    "fmt"
)

// readLines reads a whole file into memory
// and returns a slice of its lines.
func readLines(path string) ([]string, error) {
    file, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer file.Close()

    var seats []string
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        seats = append(seats, scanner.Text())
    }
    return seats, scanner.Err()
}

func part1(seats []string) int {
    grid := seatgrid(seats)
    for i := 127; i >= 0; i-- {
        for j := 7; j >= 0; j-- {
            if grid[i][j] {
                return (i * 8) + j
            }
        }
    }
    return -1
}

func part2(seats []string) int {
    grid := seatgrid(seats)
    for i := 1; i < 885; i++ {
        if grid[(i - 1) / 8][(i - 1) % 8] == true && 
           grid[(i + 1) / 8][(i + 1) % 8] == true &&
           grid[i / 8][i % 8] == false {
            return i
        }
    }
    return -1
}

func seatgrid(seats []string) [128][8]bool {
    grid := [128][8]bool{}
    for _, seat := range seats {
        size := 128
        min := 0
        max := 127
        for i := 0; i < 7; i++ {
            size = size / 2
            if seat[i] == 'F' {
                max = max - size
            } else {
                min = min + size
            }
        }
        if min != max {
            log.Fatal("Incorrect value for row num")
        }
        row := min
        min = 0
        max = 7
        size = 8
        for i := 0; i < 3; i++ {
            size = size / 2
            if seat[i + 7] == 'L' {
                max = max - size
            } else {
                min = min + size
            }
        }
        if min != max {
            log.Fatal("Incorrect value for column num")
        }
        grid[row][min] = true
    }
    return grid
}

func main() {
    if len(os.Args) < 2 {
        log.Fatal("Usage: go run run.go <relative_path_to_input_file>")
    }
    seats, err := readLines(os.Args[1])
    if err != nil {
        log.Fatal(err)
    }

    highest := part1(seats)
    fmt.Printf("Highest seat code (part 1): %d\n", highest)
    seat := part2(seats)
    fmt.Printf("Seat number is %d\n", seat)
}
