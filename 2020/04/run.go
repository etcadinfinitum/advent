package main

import (
    "log"
    "bufio"
    "os"
    "fmt"
    "strings"
    "regexp"
    "strconv"
)

// readLines reads a whole file into memory
// and returns a slice of its lines.
func readLines(path string) ([]map[string]string, error) {
    file, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer file.Close()

    var passports []map[string]string
    scanner := bufio.NewScanner(file)
    currPass := make(map[string]string)
    for scanner.Scan() {
        line := scanner.Text()
        if len(line) == 0 {
            if len(currPass) > 0 {
                passports = append(passports, currPass)
                currPass = make(map[string]string)
            }
        } else {
            tokens := strings.Split(line, " ")
            for _, token := range tokens {
                parts := strings.Split(token, ":")
                currPass[parts[0]] = parts[1]
            }
        }
    }
    return passports, scanner.Err()
}

func part1(passports []map[string]string) int {
    count := 0
    for _, passport := range passports {
        if len(passport) >= 8 {
            count += 1
        } else if len(passport) == 7 {
            if _, ok := passport["cid"]; !ok {
                count += 1
            }
        }
    }
    return count
}

func part2(passports []map[string]string) int {
    eyecolors := map[string]bool{
                    "amb": true, "blu": true, "brn": true,
                    "gry": true, "grn": true, "hzl": true,
                    "oth": true,
                    }
    count := 0
    for _, passport := range passports {
        if val, ok := passport["byr"]; !ok {
            continue
        } else {
            yr, err := strconv.Atoi(val)
            if err != nil {
                continue
            }
            if yr < 1920 || yr > 2002 {
                continue
            }
        }
        if val, ok := passport["iyr"]; !ok {
            continue
        } else {
            yr, err := strconv.Atoi(val)
            if err != nil {
                continue
            }
            if yr < 2010 || yr > 2020 {
                continue
            }
        }
        if val, ok := passport["eyr"]; !ok {
            continue
        } else {
            yr, err := strconv.Atoi(val)
            if err != nil {
                continue
            }
            if yr < 2020 || yr > 2030 {
                continue
            }
        }
        if val, ok := passport["hgt"]; !ok {
            continue
        } else {
            incm := val[len(val) - 2:]
            num, err := strconv.Atoi(val[:len(val) - 2])
            if err != nil {
                continue
            }
            if incm == "cm" {
                if num < 150 || num > 193 {
                    continue
                }
            } else if incm == "in" {
                if num < 59 || num > 76 {
                    continue
                }
            } else {
                fmt.Println("height suffix wasn't matched. value was ", val)
                continue
            }
        }
        if val, ok := passport["hcl"]; !ok {
            continue
        } else {
            matched, err := regexp.Match(`#[0-9a-f]{6}`, []byte(val))
            if err != nil {
                log.Fatal(err)
            }
            if !matched {
                fmt.Println("Regex for hair color did not match. hair color was: ", val)
                continue
            }
        }
        if val, ok := passport["ecl"]; !ok {
            continue
        } else {
            if _, valid := eyecolors[val]; !valid {
                continue
            }
        }
        if val, ok := passport["pid"]; !ok {
            continue
        } else {
            if len(val) != 9 {
                continue
            }
            _, err := strconv.Atoi(val)
            if err != nil {
                continue
            }
        }
        count += 1
    }
    return count
}

func main() {
    if len(os.Args) < 2 {
        log.Fatal("Usage: go run run.go <relative_path_to_input_file>")
    }
    passports, err := readLines(os.Args[1])
    if err != nil {
        log.Fatal(err)
    }

    valid := part1(passports)
    fmt.Printf("Total valid passports (part 1): %d\n", valid)
    valid = part2(passports)
    fmt.Printf("Total valid passports (part 2): %d\n", valid)
}
