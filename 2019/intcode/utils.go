package intcode

import (
    "strconv"
)

// converts string array to integer array
func Arrconv(arr []string) (ret []int) {
    for _, i := range arr {
        j, err := strconv.Atoi(i)
        if err != nil {
            panic(err)
        }
        ret = append(ret, j)
    }
    return ret
}
