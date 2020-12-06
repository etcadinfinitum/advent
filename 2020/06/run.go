package main

import (
    "log"
    "bufio"
    "os"
    "fmt"
    "strings"
)

// readLines reads a whole file into memory
// and returns a slice of its lines.
func readLines(path string) ([][]string, error) {
    file, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer file.Close()

    var answers [][]string
    scanner := bufio.NewScanner(file)
    currAns := []string{}
    for scanner.Scan() {
        line := scanner.Text()
        if len(line) == 0 {
            if len(currAns) > 0 {
                answers = append(answers, currAns)
                currAns = []string{}
            }
        } else {
            currAns = append(currAns, line)
        }
    }
    if len(currAns) > 0 {
        answers = append(answers, currAns)
    }
    return answers, scanner.Err()
}

func part1(answers [][]string) int {
    total := 0
    for _, group := range answers {
        yeses := make(map[rune]bool)
        for _, person := range group {
            for _, char := range person {
                if _, ok := yeses[char]; !ok {
                    yeses[char] = true
                }
            }
        }
        total = total + len(yeses)
    }
    return total
}

func part2(answers [][]string) int {
    total := 0
    for _, group := range answers {
        for _, letter := range group[0] {
            present := true
            for i := 1; i < len(group); i++ {
                if !strings.Contains(group[i], string(letter)) {
                    present = false
                }
            }
            if present {
                total += 1
            }
        }
    }
    return total
}

func main() {
    if len(os.Args) < 2 {
        log.Fatal("Usage: go run run.go <relative_path_to_input_file>")
    }
    answers, err := readLines(os.Args[1])
    if err != nil {
        log.Fatal(err)
    }

    totalAns := part1(answers)
    fmt.Printf("Unique answers across groups (part 1): %d\n", totalAns)
    totalAns = part2(answers)
    fmt.Printf("Common answers only across groups (part 2): %d\n", totalAns)
}
