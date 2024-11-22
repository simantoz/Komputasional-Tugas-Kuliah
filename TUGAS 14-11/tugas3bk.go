package main

import "fmt"

func main() {
	var r, rumus, phi float64
	phi = float64(22) / 7
	fmt.Scan(&r)
	rumus = 4 * phi * (r * r)
	fmt.Println(rumus)

}
