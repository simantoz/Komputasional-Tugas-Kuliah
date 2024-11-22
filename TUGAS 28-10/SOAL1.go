package main

import "fmt"

func main() {
	var f, x, y float64

	fmt.Print("Masukan x : ")
	fmt.Scan(&x)

	fmt.Print("Masukan y : ")
	fmt.Scan(&y)

	fmt.Println("x = ", x, "dan y =", y)

	f = (1 / ((3 * (x * x)) + 10)) + (10 * y) + 7

	fmt.Println("keluaran =", f)
}
