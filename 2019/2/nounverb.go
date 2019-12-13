package main

import (
    "fmt"
    "io/ioutil"
    "strings"
    "advent/2019/intcode"
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
    for i := 0; i < 100; i++ {
        for j := 0; j < 100; j++ {
            arr := getArr()
            tmp := intcode.Arrconv(arr)
            tmp[1] = i
            tmp[2] = j
            idx := 0
            for {
                ret, v := intcode.Process(idx, tmp)
                idx += v
                if !ret || i >= len(tmp) {
                    break
                }
            }
            if tmp[0] == 19690720 {
                fmt.Println(100 * i + j)
                return
            }
        }
    }
    fmt.Println("no solution! :(")
}
