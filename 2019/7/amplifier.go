package main

import (
    "advent/2019/intcode"
    "fmt"
)

func main() {
    // combinatorics for amplifier signal (first input)
    // second input is previous amplifier's output
    combos := []int{0, 1, 2, 3, 4}
    perms := permutations(combos)
    var result []int
    for i := 0; i < len(perms); i++ {
        fmt.Println("New permutation.\nInsert input first, then previous answer second.")
        fmt.Println("Inputs: ", perms[i])
        for j := 0; j < len(perms[i]); j++ {
            fmt.Println("Next thruster. Input is ", perms[i][j])
            intcodes := intcode.Getarr()
            idx := 0
            for {
                ret, v := intcode.Process(idx, intcodes)
                idx += v
                if !ret || idx >= len(intcodes) {
                    break
                }
            }
        }
        fmt.Println("End permutation. Last output is output for this combo.")
        fmt.Print("Enter the output for storage: ")
        var r int
        fmt.Scan(&r)
        result = append(result, r)
    }
    fmt.Println("Results: ", result)
    fmt.Println("Max: ", getMax(result))
}

func getMax(arr []int) (max int) {
    for _, el := range arr {
        if el > max {
            max = el
        }
    }
    return max
}

func permutations(arr []int)[][]int{
    var helper func([]int, int)
    res := [][]int{}

    helper = func(arr []int, n int){
        if n == 1{
            tmp := make([]int, len(arr))
            copy(tmp, arr)
            res = append(res, tmp)
        } else {
            for i := 0; i < n; i++{
                helper(arr, n - 1)
                if n % 2 == 1{
                    tmp := arr[i]
                    arr[i] = arr[n - 1]
                    arr[n - 1] = tmp
                } else {
                    tmp := arr[0]
                    arr[0] = arr[n - 1]
                    arr[n - 1] = tmp
                }
            }
        }
    }
    helper(arr, len(arr))
    return res
}
