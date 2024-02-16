package main

import (
	"booking-app/helper"
	"fmt"
	"strconv"
	"strings"
)

// Creating array of strings
var bookings []string
var conferenceName = "Go Conference"

const conferenceTickets = 50

var remainingTickets uint = 50
var firstName string
var lastName string
var email string
var userTickets uint

func main() {

	//  You can set the conditional below that will dictate how
	//  long the loop will run for.
	for remainingTickets > 0 {

		//  Greeting users
		greetUsers(conferenceName, conferenceTickets)

		// Calling function to user input. firstName, lastName, emailAddress and number
		// of tickets to be purchased.)
		firstName, lastName, email, userTickets = getUserInput(firstName, lastName, email, userTickets)

		//  The below function returns multiple bools.
		isValidName, isValidEmail, isValidTicketNumber := helper.ValidateUserInput(firstName,
			lastName,
			email,
			userTickets,
			remainingTickets)

		//  Confirming that all user input passed validation.
		if isValidName && isValidEmail && isValidTicketNumber {

			//  Calling function to book ticket for the user.
			bookings, remainingTickets = bookTicket(userTickets, firstName, lastName, email)

			// Printing firstNames from list of bookins array
			firstNames := printFirstNames(bookings)

			//  Printing bookings so far.
			fmt.Printf("These are all our bookings so far: %v\n", firstNames)

			//  Shortened if statement. If remainingTicket is 0
			//  noTicketsRemaining will be set to False.
			if remainingTickets == 0 {
				// Breaking out of for loop because no more tickets are
				// left.
				fmt.Println("Our conference is booked out. Come back next year.")
				break
			}
		} else {
			if !isValidName {
				fmt.Println("Invalid name. Please try again.")
			}
			if !isValidEmail {
				fmt.Println("Invalid email. Please try again.")
			}
			if !isValidTicketNumber {
				fmt.Println("Invalid number of tickets. Please try again.")
			}
		}
	}

	city := "London"

	switch city {
	case "New York":
		// execute code for booking New York conference tickets
	case "Singapore", "Hong Kong":
		// execute code for booking Singapore conference tickets
	case "London", "Berlin":
		// execute code for booking London conference tickets
	case "Mexico City":
		// execute code for booking Mexico City conference tickets
	default:
		fmt.Print("No valid city selected")
	}
}

func greetUsers(conferenceName string, confTickets int) {
	fmt.Printf("Welcome to our %v booking application\n", conferenceName)
	fmt.Printf("conferenceTickets is %T, remintaingTickers is %T, conferenceName is %T\n", confTickets, remainingTickets, conferenceName)
	fmt.Printf("We have total of %v tickets and %v are still available.\n", confTickets, remainingTickets)
	fmt.Println("Get your tickets here to attend")

}

// Notice the [] string on the outside of () this designates
// that this function will return a string.
func printFirstNames(bookings []string) []string {
	var firstNames = []string{}
	// For loop to iterate through the bookings array.
	// _ is used as an unused variable.
	for _, booking := range bookings {
		// Spliting booking value in to a list of names.
		// names will look like [greg,smith]
		var names = strings.Fields(booking)
		firstNames = append(firstNames, names[0])
	}
	return firstNames
}

func getUserInput(firstName string, lastName string, email string, userTickets uint) (string, string, string, uint) {
	// ask user for their name
	fmt.Println("Enter your first name: ")
	fmt.Scan(&firstName)

	fmt.Println("Enter your last name: ")
	fmt.Scan(&lastName)

	fmt.Println("Enter your email address: ")
	fmt.Scan(&email)

	fmt.Println("Enter number of tickets to be purchased: ")
	fmt.Scan(&userTickets)

	return firstName, lastName, email, userTickets
}

func bookTicket(userTickets uint, firstName string, lastName string, email string) ([]string, uint) {
	remainingTickets = remainingTickets - userTickets

	//  Creating map
	var userData = make(map[string]string)
	userData["firstName"] = firstName
	userData["lastName"] = lastName
	userData["email"] = email
	userData["numberOfUserTickets"] = strconv.FormatUint(uint64(userTickets), 10)

	// Appending first and last name of user
	// to array.
	bookings = append(bookings, firstName+" "+lastName)

	fmt.Printf("Thank you %v %v for booking %v tickets. You will recieve a confirmation email at %v\n", firstName, lastName, userTickets, email)
	fmt.Printf("Remaining Tickets: %v\n", remainingTickets)

	return bookings, remainingTickets

}
