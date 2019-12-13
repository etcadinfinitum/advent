package main

import (
    "advent/2019/intcode"
)

func main() {
    arr := intcode.Getarr()
    idx := 0
    for {
        ret, v := intcode.Process(idx, arr)
        idx += v
        if !ret || idx >= len(arr) {
            break
        }
    }
}
