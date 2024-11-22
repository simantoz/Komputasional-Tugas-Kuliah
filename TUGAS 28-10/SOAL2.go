package main

import "fmt"

func main() {
	var f, x float64
	fmt.Print("Masukan x = ")
	fmt.Scan(&x)

	f = ((x * x * x) + (3 * x)) / ((x * x * x * x) - (3 * (x * x)) + 4)

	fmt.Println("Keluaran =", f)

}
