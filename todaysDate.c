#include "todaysDate.h"
#include <stdio.h> 

/* 
 * Note that this function does not print the correct tomorrow date after when the month 
 * is a leap year 
 *
 * To resolve this, there is another file called `todaysDate_resolved.c` that resolves this 
 * caveat with the use of a function
 * 
 * Be sure to check that out after this demonstration
 *
 */
int main(int argc, char **argv)
{
	date today, tomorrow; 

	const int daysPerMonth[12] = 
		{
		31, 28, 31, 30, 31, 30, 
		31, 31, 30, 31, 30, 31
		};

	printf("Enter todays date (mm dd yyyy): \n");
	scanf("%i%i%i", &today.month, &today.day, &today.year);

	if (today.day != daysPerMonth[today.month - 1])
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
