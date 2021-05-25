package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

var last = 0

func randomNumber(max int) int {
	last = (25214903917*last + 11) % 281474976710656
	var tmp = 0
	if last >= 0 {
		tmp = last
	} else {
		tmp = -last
	}
	return tmp % max
}

func createArray(len int, maxValue int) []int {
	tab := make([]int, len)
	for i := 0; i < len; i++ {
		tab[i] = randomNumber(maxValue)
	}
	return tab
}

func main() {

	var tabSize = 10000000
	var maxValue = 5000000
	var noOutput = false
	var debug = false

	var argsWithoutProg = os.Args[1:]
	for _, s := range argsWithoutProg {
		if s == "--nooutput" {
			noOutput = true
		} else if strings.HasPrefix(s, "--nbop=") {
			i, err := strconv.Atoi(s[7:])
			if err != nil {
				// handle error
				fmt.Println(err)
				os.Exit(2)
			} else if i > 0 {
				tabSize = i
			}
		} else if s == "--debug" {
			debug = true
		}
	}

	if debug {
		for i, s := range os.Args {
			fmt.Printf("   argv[%d] : '%s'\n", i, s)
		}
		fmt.Printf("lang=go;tabSize=%d;maxValue=%d;noOutput=%t;debug=%t\n",
			tabSize, maxValue, noOutput, debug)
	}

	ints := createArray(tabSize, maxValue)
	sort.Ints(ints)
	if !noOutput {
		fmt.Print("Ints:   ", ints[0:10])
		if tabSize > 10 {
			fmt.Print(" ...")
		}
		fmt.Println()
	}

}
