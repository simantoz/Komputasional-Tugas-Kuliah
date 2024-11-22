package main

import "fmt"

func main() {
	var huruf string
	var hasil bool
	fmt.Scan(&huruf)
	hasil = int(huruf[0]) >= 65 && int(huruf[0]) <= 90
	fmt.Print(hasil)

}
