package intcode

import (
    "fmt"
)

func Process(idx int, arr []int) (bool, int) {
    opcode := arr[idx] % 100
    if opcode == 1 {
        add(idx, arr)
        return true, 4
    } else if opcode == 2 {
        mult(idx, arr)
        return true, 4
    } else if opcode == 3 {
        // read int, store at arr[idx + 1]
        var val int
        fmt.Scan(&val)
        arr[idx + 1] = val
        return true, 2
    } else if opcode == 4 {
        // print arr[idx + 1] to stdout
        fmt.Println(arr[idx + 1])
        return true, 2
    } else if arr[idx] == 99 {
        return false, 0
    }
    fmt.Println("unknown command %d at idx %d", arr[idx], idx)
    return false, 0
}

func add(idx int, arr []int) (bool) {
    sum := arr[arr[idx + 1]] + arr[arr[idx + 2]]
    arr[arr[idx + 3]] = sum
    return true
}

func mult(idx int, arr []int) (bool) {
    product := arr[arr[idx + 1]] * arr[arr[idx + 2]]
    arr[arr[idx + 3]] = product
    return true
}
