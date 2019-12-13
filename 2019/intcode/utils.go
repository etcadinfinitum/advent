package intcode

import (
    "fmt"
    "io/ioutil"
    "strings"
    "strconv"
)

func Getarr() (ret []int) {
    b, err := ioutil.ReadFile("data.txt")
    if err != nil {
        fmt.Print(err)
    }
    s := strings.TrimSuffix(string(b), "\n")
    tmp := strings.Split(s, ",")
    ret = Arrconv(tmp)
    return ret
}

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
