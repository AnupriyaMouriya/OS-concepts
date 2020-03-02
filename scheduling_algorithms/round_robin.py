'''
ROUND ROBIN SCHEDULING
* Assuming all the process has arrived at the same time

1- Create an array rem_bt[] to keep track of remaining
   burst time of processes. This array is initially a
   copy of bt[] (burst times array)
2- Create another array wt[] to store waiting times
   of processes. Initialize this array as 0.
3- Initialize time : t = 0
4- Keep traversing the all processes while all processes
   are not done. Do following for i'th process if it is
   not done yet.
    a- If rem_bt[i] > quantum
       (i)  t = t + quantum
       (ii) bt_rem[i] -= quantum;
    c- Else // Last cycle for this process
       (i)  t = t + bt_rem[i];
       (ii) wt[i] = t - bt[i]
       (ii) bt_rem[i] = 0; // This process is over

'''


def find_waiting_time(waiting_time, quantum, burst_time, remaining_burst_time, n):
    print(remaining_burst_time)
    t = 0
    while (1):
        done = True
        for i in range(n):
            if (remaining_burst_time[i] > 0):
                done = False
                if (remaining_burst_time[i] > quantum):
                    t += quantum
                    remaining_burst_time[i] -= quantum
                else:
                    t = t + remaining_burst_time[i]
                    waiting_time[i] = t - burst_time[i]
                    remaining_burst_time[i] = 0
        if (done == True):
            break

    """
    while (1):
        done = True
        for i in range(n):
            if (remaining_burst_time[i] > 0):
                done = False
                if remaining_burst_time[i] > quantum:
                    t = t + quantum
                    remaining_burst_time[i] -= quantum
                else:
                    t = t + remaining_burst_time[i]
                    waiting_time[i] = t - burst_time[i]
                    remaining_burst_time[i] = 0
        if (done == True):
            break
    return waiting_time
"""

def find_avg_time(processes, n, quantum, burst_time):
    waiting_time = [0] * n
    remaining_burst_time = burst_time
    find_waiting_time(waiting_time, quantum, burst_time, remaining_burst_time, n)
    print(waiting_time)
    turn_around_time = [0] * n
    for i in range(n):
        turn_around_time[i] = burst_time[i] + waiting_time[i]
    avg_waiting_time = sum(waiting_time) / n
    avg_turn_around_time = sum(turn_around_time) / n
    print(avg_turn_around_time, avg_waiting_time)


if __name__ == '__main__':
    print("Round Robin scheduling")
    processes = [1, 2, 3]
    n = len(processes)
    quantum = 2;
    burst_time = [10, 5, 8]
    find_avg_time(processes, n, quantum, burst_time)
