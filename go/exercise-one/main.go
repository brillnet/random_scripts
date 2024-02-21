package main

import "fmt"

func main() {

	//1:48

	var n complex64 = 1 + 2i
	fmt.Printf("%w, %T\n", n, n)

	//bit shifting
	// a := 8              // 2^3
	// fmt.Println(a << 3) // 2^3 * 2^3 = 2^6
	// fmt.Println(a >> 3) // 2^3 / 2^3 = 2^0

	// a := 10 //1010
	// b := 3  //0011

	// fmt.Println(a & b)
	// fmt.Println(a | b)
	// fmt.Println(a ^ b)
	// fmt.Println(a &^ b)
}
