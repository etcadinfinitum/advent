package intcode

import (
    "fmt"
)

func Process(idx int, arr []int) (bool, int) {
    opcode := arr[idx] % 100
    p1mode := ((arr[idx] % 1000) - opcode) / 100
    p2mode := ((arr[idx] % 10000) - opcode - (p1mode * 100)) / 1000
    // p3mode := (arr[idx] % 100000) - opcode - (p1mode * 100) - (p2mode * 1000)
    if opcode == 1 {
        lhs := arr[idx + 1]
        rhs := arr[idx + 2]
        dest := arr[idx + 3]
        if p1mode == 0 {
            lhs = arr[lhs]
        }
        if p2mode == 0 {
            rhs = arr[rhs]
        }
        add(arr, lhs, rhs, dest)
        return true, 4
    } else if opcode == 2 {
        lhs := arr[idx + 1]
        rhs := arr[idx + 2]
        dest := arr[idx + 3]
        if p1mode == 0 {
            lhs = arr[lhs]
        }
        if p2mode == 0 {
            rhs = arr[rhs]
        }
        mult(arr, lhs, rhs, dest)
        return true, 4
    } else if opcode == 3 {
        // read int, store at arr[idx + 1]
        var val int
        fmt.Scan(&val)
        arr[arr[idx + 1]] = val
        return true, 2
    } else if opcode == 4 {
        // print arr[idx + 1] to stdout
        val := arr[idx + 1]
        if p1mode == 0 {
            val = arr[val]
        }
        fmt.Println(val)
        return true, 2
    } else if arr[idx] == 99 {
        return false, 0
    }
    fmt.Println("unknown command %d at idx %d", arr[idx], idx)
    return false, 0
}

func add(arr []int, lhs int, rhs int, dest int) (bool) {
    sum := lhs + rhs
    arr[dest] = sum
    return true
}

func mult(arr []int, lhs int, rhs int, dest int) (bool) {
    product := lhs * rhs
    arr[dest] = product
    return true
}
