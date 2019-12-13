package main

import (
    "fmt"
    "io/ioutil"
    "strings"
    "advent/2019/intcode"
)

func main() {
    b, err := ioutil.ReadFile("data.txt")
    if err != nil {
        fmt.Print(err)
    }
    s := strings.TrimSuffix(string(b), "\n")
    arr := strings.Split(s, ",")
    iarr := intcode.Arrconv(arr)
    i := 0
    for {
        ret, v := intcode.Process(i, iarr);
        i += v
        if !ret || i >= len(iarr) {
            break
        }
    }
    fmt.Println(iarr[0])
}

