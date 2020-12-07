package main

import (
    "log"
    "bufio"
    "os"
    "fmt"
    "strings"
)

type Rule struct {
    children []string
    parents []string
}

// readLines reads a whole file into memory
// and returns a slice of its lines.
func readLines(path string) (map[string]Rule, error) {
    file, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer file.Close()

    bags := make(map[string]Rule)
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        line := scanner.Text()
        contents := strings.Split(line, " bags contain ")
        kids := []string{}
        if contents[1] != "no other bags." {
            parts := strings.Split(contents[1], ", ")
            for _, part := range parts {
                words := strings.Split(part, " ")
                kids = append(kids, words[1] + " " + words[2])
            }
        }
        bags[contents[0]] = Rule{children: kids, parents: []string{}}
    }
    return bags, scanner.Err()
}

func findGoldBags(bags map[string]Rule, bag string) bool {
    if len(bags[bag].children) == 0 {
        return false
    }
    for _, child := range bags[bag].children {
        if child == "shiny gold" {
            return true
        } else {
            if findGoldBags(bags, child) {
                return true
            }
        }
    }
    return false
}

func main() {
    if len(os.Args) < 2 {
        log.Fatal("Usage: go run run.go <relative_path_to_input_file>")
    }
    bags, err := readLines(os.Args[1])
    if err != nil {
        log.Fatal(err)
    }

    found := 0
    for color, _ := range bags {
        if findGoldBags(bags, color) {
            found += 1
        }
    }
    fmt.Printf("valid containing bags found (part 1): %d\n", found)
}
