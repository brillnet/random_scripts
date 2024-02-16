package helper

import "strings"

func ValidateUserInput(firstName string,
	lastName string,
	email string,
	userTickets uint,
	remainingTickets uint) (bool, bool, bool) {
	// Assigning bool values to variables.
	isValidName := len(firstName) >= 2 && len(lastName) >= 2
	isValidEmail := strings.Contains(email, "@")
	isValidTicketNumber := userTickets > 0 && userTickets <= remainingTickets

	return isValidName, isValidEmail, isValidTicketNumber
}
