###SCHEDULING ALGORITHMS INTRO

####1. FCFS(First Come First Served)

First in, first out (FIFO), also known as first come, first served (FCFS), is the simplest scheduling algorithm. \
FIFO simply queues processes in the order that they arrive in the ready queue.
In this, the process that comes first will be executed first and next process starts only after the previous gets
fully executed.

####2. ROUND ROBIN

Round Robin is a CPU scheduling algorithm where each process is assigned a fixed time slot in a cyclic way.

It is simple, easy to implement, and starvation-free as all processes get fair share of CPU.
One of the most commonly used technique in CPU scheduling as a core.
It is preemptive as processes are assigned CPU only for a fixed slice of time at most.
The disadvantage of it is more overhead of context switching.
