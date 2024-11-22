package main

import "fmt"

func main() {
	var digit string
	fmt.Scan(&digit)
	fmt.Printf("%c%c%c%c", digit[0], digit[0], digit[1], digit[1])
}
