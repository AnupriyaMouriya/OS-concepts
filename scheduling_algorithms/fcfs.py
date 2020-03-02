"""
First Come First Served ( FCFS Scheduling)

PSEUDO CODE

* Assuming arrival time is 0
1-  Input the processes along with their burst time (bt).
2-  Find waiting time (wt) for all processes.
3-  As first process that comes need not to wait so
    waiting time for process 1 will be 0 i.e. wt[0] = 0.
4-  Find waiting time for all other processes i.e. for
     process i ->
       wt[i] = bt[i-1] + wt[i-1] .
5-  Find turnaround time = waiting_time + burst_time
    for all processes.
6-  Find average waiting time =
                 total_waiting_time / no_of_processes.
7-  Similarly, find average turnaround time =
                 total_turn_around_time / no_of_processes.

"""
def find_waiting_time(burst_time,waiting_time,n):
    for i in range(1,n):
        waiting_time[i]=waiting_time[i-1]+burst_time[i-1];
    return waiting_time

def find_turn_around_time(burst_time,waiting_time,turn_around_time,n):
    for i in range(n):
        turn_around_time[i]=waiting_time[i]+burst_time[i]
    return turn_around_time

def find_avg_time(processes,n,burst_time):
    waiting_time=[0]*n
    turn_around_time=[0]*n
    waiting_time=find_waiting_time(burst_time,waiting_time,n)
    turn_around_time=find_turn_around_time(burst_time,waiting_time,turn_around_time,n)
    average_turn_around_time=sum(turn_around_time)/n
    average_waiting_time=sum(waiting_time)/n
    print("Processes Burst-time  Waiting-time  Turn-around-time")

    for i in range(n):
        print(" " + str(i + 1) + "\t\t\t" +
              str(burst_time[i]) + "\t\t\t" +
              str(waiting_time[i]) + "\t\t\t\t " +
              str(turn_around_time[i]))

    print('Average waiting-time : {} \nAverage turn-around-time : {}'\
          .format(average_waiting_time,average_turn_around_time))

if __name__=="__main__":
    print("First come first served cpu scheduling")
    processes=[1,2,3]
    n=len(processes)
    burst_time=[10,5,8]
    find_avg_time(processes,n,burst_time);
