package main

import "fmt"

func main() {
	var E0, c, E1, cc int
	fmt.Scan(&E0, &c, &E1)
	cc = (E0 - E1) / c
	fmt.Print(cc)
}
