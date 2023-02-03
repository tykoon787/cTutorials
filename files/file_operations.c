#include <stdio.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#include <unistd.h>
#include <stdlib.h>


int main(void)
{
	int fd; 
	char buf[12];

	/* Open File */
	fd = open("Myfile.txt", O_CREAT | O_WRONLY, 0600);

	if (fd == 1)
	{
		printf("FAiled to Create the File\n");
		exit(1);
	}

	/* Write to File */
	write(fd, "Baby Panda\n", 13);

	/* Close the File */
	close (fd);

	/* Reading from the file */
	fd = open("Myfile.txt",O_RDONLY);

	if (fd == -1)
	{
		printf("Failed to Read File\n");
		exit(1);
	}

	read (fd, buf, 10);
	buf[11] = '\0';
	printf("Buff: %s\n", buf);
	return (0);
}
