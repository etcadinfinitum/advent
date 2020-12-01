package main

import (
    "errors"
    "log"
    "strconv"
    "bufio"
    "os"
    "fmt"
)

// readLines reads a whole file into memory
// and returns a slice of its lines.
func readLines(path string) ([]int, error) {
    file, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer file.Close()

    var lines []int
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        i, err := strconv.Atoi(scanner.Text())
        if err != nil {
            return nil, err
        }
        lines = append(lines, i)
    }
    return lines, scanner.Err()
}

func twoSum(freqMap map[int]int) (int, error) {
    for k, _ := range freqMap {
        if _, there := freqMap[2020 - k]; there {
            return k * (2020 - k), nil
        }
    }
    return 0, errors.New("No result found for twosum")
}

func threeSum(freqMap map[int]int) (int, error) {
    for k, _ := range freqMap {
        for m, v := range freqMap {
            if m == k && v < 2 {
                continue
            }
            if _, there := freqMap[2020 - (k + m)]; there {
                return k * m * (2020 - k - m), nil
            }
        }
    }
    return 0, errors.New("No result found for threesum")
}

func main() {
    file := os.Args[1]
    lines, err := readLines(file)
    if err != nil {
        log.Fatal(err)
    }
    freqMap := make(map[int]int)
    for i := 0; i < len(lines); i++ {
        if val, there := freqMap[lines[i]]; !there {
            freqMap[lines[i]] = 1
        } else {
            freqMap[val] = freqMap[val] + 1
        }
    }

    two, err := twoSum(freqMap)
    if err == nil {
        fmt.Printf("Two Sum: %d", two)
    }
    three, err := threeSum(freqMap)
    if err == nil {
        fmt.Printf("Three Sum: %d", three)
    }
}
