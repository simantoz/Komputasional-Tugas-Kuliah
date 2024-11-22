package main

import "fmt"

func main() {
	var x int
	var d1, d2, d3 int

	fmt.Print("Masukan x = ")
	fmt.Scan(&x)

	d3 = x % 10        // ratusan
	d2 = (x / 10) % 10 // puluhan
	d1 = x / 100       // satuan

	fmt.Println("Keluaran = ", d1, d2, d3)
}
