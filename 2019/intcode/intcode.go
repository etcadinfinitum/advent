package intcode

import (
    "fmt"
)

func getFirstTwoVals(arr []int, idx int, p1mode int, p2mode int) (int, int) {
    param1 := arr[idx + 1]
    param2 := arr[idx + 2]
    if p1mode == 0 {
        param1 = arr[param1]
    }
    if p2mode == 0 {
        param2 = arr[param2]
    }
    return param1, param2
}

func Process(idx int, arr []int) (bool, int) {
    opcode := arr[idx] % 100
    p1mode := ((arr[idx] % 1000) - opcode) / 100
    p2mode := ((arr[idx] % 10000) - opcode - (p1mode * 100)) / 1000
    // p3mode := (arr[idx] % 100000) - opcode - (p1mode * 100) - (p2mode * 1000)
    if opcode == 1 {
        lhs, rhs := getFirstTwoVals(arr, idx, p1mode, p2mode)
        dest := arr[idx + 3]
        add(arr, lhs, rhs, dest)
        return true, 4
    } else if opcode == 2 {
        lhs, rhs := getFirstTwoVals(arr, idx, p1mode, p2mode)
        dest := arr[idx + 3]
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
    } else if opcode == 5 {
        // jump-if-true
        jump := 3       // standard jump
        zero := arr[idx + 1]
        if p1mode == 0 {
            zero = arr[zero]
        }
        if zero != 0 {
            diff := arr[idx + 2]
            if p2mode == 0 {
                diff = arr[diff]
            }
            jump = diff - idx
        }
        return true, jump
    } else if opcode == 6 {
        // jump-if-false
        jump := 3
        zero := arr[idx + 1]
        if p1mode == 0 {
            zero = arr[zero]
        }
        if zero == 0 {
            diff := arr[idx + 2]
            if p2mode == 0 {
                diff = arr[diff]
            }
            jump = diff - idx
        }
        return true, jump
    } else if opcode == 7 {
        // less than
        param1, param2 := getFirstTwoVals(arr, idx, p1mode, p2mode)
        val := 0
        if param1 < param2 {
            val = 1
        }
        arr[arr[idx + 3]] = val
        return true, 4
    } else if opcode == 8 {
        // equals
        param1, param2 := getFirstTwoVals(arr, idx, p1mode, p2mode)
        val := 0
        if param1 == param2 {
            val = 1
        }
        arr[arr[idx + 3]] = val
        return true, 4
    } else if opcode == 99 {
        return false, 0
    }
    fmt.Println("unknown command", arr[idx],"at idx", idx)
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
