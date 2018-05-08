#include <stdio.h>
#include <limits.h>
#include <string.h>

#define BOOL int
#define true 1
#define false 0

#define bool BOOL

static unsigned int counter = 0;

bool iszero()
{
	return counter >0 ? true : false;	
}

int inc()
{
	if(counter >= UINT_MAX){
		return -1;
	}
	//printf ("%d", UINT_MAX);
	counter +=1;
	return 0;
}

unsigned int dec()
{
	/*
	if(counter != 0){
		counter -= 1;
	}
	return counter;*/
	if(counter < 1){
		return -1;
	}
	counter -=1;
	return 0;
}

int main(int arg, char **args)
{
	printf("do increase...\n");
	inc();
	printf("current counter value: %d\n", counter);
	printf("do decreas...\n");
	dec();
	printf("current counter value: %d\n", counter);
	printf("do iszero...\n");
	iszero();
	printf("current counter value: %d\n", counter);
	return 0;
}
