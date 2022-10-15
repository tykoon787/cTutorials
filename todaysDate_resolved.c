#include "todaysDate.h"
#include <stdio.h>
#include <stdbool.h>

// Function to determine number of days
int numberOfDays(struct date d)
{
	int days; 
	bool isLeapYear (struct date d);

	const int daysPerMonth[12] = 
	{
	31, 28, 31, 30, 31, 30, 
	31, 31, 30, 31, 30, 31
	};

	if (isLeapYear(d) == true && d.month == 2)
		days = 29;
	
	else
		days = daysPerMonth[d.month - 1];

	return (days);

}

// Function to Determine a leap year
bool isLeapYear(struct date d)
{
	bool leapYearFlag;


	if ((d.year % 4 == 0 && d.year % 100 != 0) || d.year % 400 == 0)
		leapYearFlag = true; 
	else 
		leapYearFlag = false;

	return (leapYearFlag);
}

int main(int argc, char **argv)
{
	date today, tomorrow; 
	int numberOfDays(struct date d);

	printf("Enter todays date (mm dd yyyy): \n");
	scanf("%i%i%i", &today.month, &today.day, &today.year);

	if (today.day != numberOfDays(today))
	{
		tomorrow.day = today.day + 1;
		tomorrow.month = today.month; 
		tomorrow.year = today.year; 

		/* 
		* The if statement here is used to check whether the day 
		* is at the end of the month
		*/
	}

	else if (today.month == 12)
	{
		tomorrow.day = 1; 
		tomorrow.month = 1; 
		tomorrow.year = today.year + 1; 

		/* 
		* If the day does indeed fall on the end of the day of the month, the 
		* program goes to check if the month is at the end of the year. 
		*
		* if it is, then the day is set to 1 and the month to 1 and the year 
		* appended by one (+1)
		*/
	}

	else
	{
		tomorrow.day = 1; 
		tomorrow.month = today.month + 1; 
		tomorrow.year = today.year; 

		/* 
		* If the day falls at the end of the day of the month but does not fall
		* at the end of the year i.e., (month == 12) then the day is just set to one 
		* and the month appended by one (+1)
		*/
	}

	printf("Tomorrow's date is %i/%i/%.2i.\n", 
	tomorrow.month, 
	tomorrow.day, 
	tomorrow.year);
	return (0);
}
