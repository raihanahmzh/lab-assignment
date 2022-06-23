#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

void childTask(){

	char name[20];
	printf("Enter a name: ");
	fgets(name, 20, stdin);
	printf("Name is %s ", name);
	exit(0);
}

void parentTask(){

	printf("\nWaiting for child process..\n  ");
	wait(NULL);
	printf("JOB IS DONE! \n");
}


int main(void){

for(int i = 0; i<4; i++){
int pid = fork();

if(pid == 0){
	childTask();
}

else if(pid > 0){
	parentTask();
}
}
return(0);

}
