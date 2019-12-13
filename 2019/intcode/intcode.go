package intcode

import (
    "fmt"
)

func Process(idx int, arr []int) (bool) {
    if arr[idx] == 1 {
        add(idx, arr)
        return true
    } else if arr[idx] == 2 {
        mult(idx, arr)
        return true
    } else if arr[idx] == 99 {
        return false
    }
    fmt.Println("unknown command %d at idx %d", arr[idx], idx)
    return false
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
