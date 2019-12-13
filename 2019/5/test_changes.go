package main

import (
    "fmt"
    "advent/2019/intcode"
    "io/ioutil"
    "strings"
)

func getArr() (ret []string) {
    b, err := ioutil.ReadFile("data.txt")
    if err != nil {
        fmt.Print(err)
    }
    s := strings.TrimSuffix(string(b), "\n")
    ret = strings.Split(s, ",")
    return ret
}

func main() {
    arr := intcode.Arrconv(getArr())
    fmt.Println(arr)
    idx := 0
    for {
        ret, v := intcode.Process(idx, arr)
        idx += v
        if !ret || idx >= len(arr) {
            break
        }
    }
    fmt.Println(arr)
}
