#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/sem.h>

#define KEY 0x1111

union semun {
    int val;
    struct semid_ds *buf;
    unsigned short  *array;
};

struct sembuf p = { 0, -1, SEM_UNDO};
struct sembuf v = { 0, +1, SEM_UNDO};

int main()
{
    int id = semget(KEY, 1, 0666 | IPC_CREAT);
    if(id < 0)
    {
        perror("semget"); exit(11);
    }
    union semun u;
    u.val = 1;
    if(semctl(id, 0, SETVAL, u) < 0)
    {
        perror("semctl"); exit(12);
    }
    
    int pid;
    pid =  fork();
    if(pid < 0)
    {
        perror("fork"); exit(1);
    }
    else if(pid)
    {
    	while(1){
            if(semop(id, &p, 1) < 0)
            {
                perror("semop p"); exit(13);
            }
            printf("hijo ocupando sem\n");
			sleep(1);
            if(semop(id, &v, 1) < 0)
            {
                perror("semop p"); exit(14);
            }

        }    
    }
    else
    {
    	while(1){
            if(semop(id, &p, 1) < 0)
            {
                perror("semop p"); exit(15);
            }
            printf("padre ocupando sem\n");
			sleep(5);
            if(semop(id, &v, 1) < 0)
            {
                perror("semop p"); exit(16);
            }
        }
    }
}
