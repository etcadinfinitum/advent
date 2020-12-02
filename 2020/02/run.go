package main

import (
    "log"
    "strconv"
    "bufio"
    "os"
    "fmt"
    "strings"
)

type Password struct {
    minOccur int
    maxOccur int
    letter rune
    password string
    
}

// readLines reads a whole file into memory
// and returns a slice of its lines.
func readLines(path string) ([]Password, error) {
    file, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer file.Close()

    var lines []Password
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        parts := strings.Split(scanner.Text(), " ")
        nums := strings.Split(parts[0], "-")
        min, err := strconv.Atoi(nums[0])
        if err != nil {
            return nil, err
        }
        max, err := strconv.Atoi(nums[1])
        if err != nil {
            return nil, err
        }
        lines = append(lines, Password{min, max, rune(parts[1][0]), parts[2]})
    }
    return lines, scanner.Err()
}

func part1(passwords []Password) int {
    valid := 0
    for _, entry := range passwords {
        count := 0
        for _, char := range entry.password {
            if char == entry.letter {
                count += 1
            }
        }
        if count >= entry.minOccur && count <= entry.maxOccur {
            valid += 1
        }
    }
    return valid
}

func part2(passwords []Password) int {
    valid := 0
    for _, entry := range passwords {
        if rune(entry.password[entry.minOccur - 1]) != entry.letter && rune(entry.password[entry.maxOccur - 1]) == entry.letter {
            valid += 1
        } else if rune(entry.password[entry.minOccur - 1]) == entry.letter && rune(entry.password[entry.maxOccur - 1]) != entry.letter {
            valid += 1
        }
    }
    return valid
}

func main() {
    if len(os.Args) < 2 {
        log.Fatal("Usage: go run run.go <relative_path_to_input_file>")
    }
    passwords, err := readLines(os.Args[1])
    if err != nil {
        log.Fatal(err)
    }

    valid := part1(passwords)
    fmt.Printf("Total valid passwords (part 1): %d\n", valid)

    valid = part2(passwords)
    fmt.Printf("Total valid passwords (part 2): %d\n", valid)
}
