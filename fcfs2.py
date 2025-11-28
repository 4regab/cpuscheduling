print("First Come First Serve CPU Scheduling")
n = int(input("Number of Processes: "))              # get anoumt of processes
arrival_time = []                                  # empty list
burst_time = []

# input loop for Process, AT, and BT
# range(n) repeats n times (once per process)
# ex. If n = 3, this runs 3 times with i being 0, then 1, then 2.
for i in range(n):
    # this will print "Process P1", "Process P2", etc. length depends on the user input range(n)
    print(f"\nProcess P{i+1}:")
    AT = int(input("Arrival Time:"))    # input AT
    BT = int(input("Burst Time:"))      # input BT
    # adds the input values to the arrival_time list
    arrival_time.append(AT)
    # adds the input values to the burst_time list
    burst_time.append(BT)

# fcfs sorting rearranges them by arrival time
# range(n) creates ex. [0, 1, 2, 3, 4] (process indices)
# sorted() rearranges them by arrival time by using key=lambda i
# lambda creates a small temporary function without giving it a name
# `key=lambda i` looks at arrival_time[i] and it gets sorted
order = sorted(range(n), key=lambda i: arrival_time[i])

# result list
# [0] * n list that repeats using n range value ex. If n=3, each becomes [0, 0, 0].
# [] - an empty list
# [0] - a list with one specific value (0) will add more later
# 0 - a list that starts at 0
completion_time = [0] * n
waiting_time = [0] * n
turnaround_time = [0] * n
current_time = 0  # CPU clock time
gantt_order = []  # stores which processes ran (P4, P1, P2...)
gantt_times = [0]  # tracks when each process finishes (starts with 0)

# Main calculation loop for FCFS
for i in order:
    # Loops through processes in sorted order (earliest arrival first)
    # If CPU is idle (current time is before process arrives), jump forward to when process arrives.
    # ex. If current_time=2 but next process arrives at time 5, CPU waits until time 5.
    if current_time < arrival_time[i]:
        current_time = arrival_time[i]  # wait until process arrives

    # Adds burst time to current time (process finishes)
    # CT - completion time (when process is done)
    # Stores it in the list
    # Updates the CPU clock by adding how long the process (burst time) runs
    # example: if current_time = 10 and burst_time[i] = 5
    # current_time = 10 + 5, current_time = 15
    current_time = current_time + burst_time[i]

    # Copies the current time into CT
    CT = current_time

    # Stores the completion time in the list at position 
    # [i] - the position for specific process
    completion_time[i] = (CT)

    # Turnaround Time = Completion Time - Arrival Time (Total time from arrival to completion)
    # example
    # CT = 15 (finished at time 15) 
    # arrival_time[i] = 10 (arrived at time 10) 
    # TT = 15 - 10 = 5
    TT = CT - arrival_time[i]

    # stores the turnaround time in the list at position
    # ex. if i = 0 and TT = 5: turnaround_time[0] = 5  The list becomes: [5, 0, 0]
    turnaround_time[i] = (TT)

    # Waiting Time = Turnaround Time - Burst Time (Time spent waiting for CPU)
    # Calculates how long the process waited before running
    # ex. TT = 5 (total time was 5), burst_time[i] = 3 (actually ran for 3) 
    # WT = 5 - 3 = 2 (waited for 2)
    WT = TT - burst_time[i]

    # Stores the waiting time in the list
    # ex. If i = 0 and WT = 2: waiting_time[0] = 2  The list becomes: [2, 0, 0]
    waiting_time[i] = (WT)

    # Records which process ran and when it finished
    # Adds the process name to the gantt_order list.
    # gantt_order - list tracking which processes ran
    # .append() - adds something to the end of the list
    # f"P{i+1}" - creates the process name sequentially
    # ex. If i = 0: f"P{i+1}" = f"P{0+1}" = "P1" gantt_order.append("P1")  
    # gantt_order becomes: ["P1"]  
    # If i = 1, gantt_order becomes: ["P1", "P2"]
    gantt_order.append(f"P{i+1}")

    # gantt_times - list tracking when each process finished
    # current_time - the time right now (when this process finished)
    # ex. If current_time = 15: gantt_times.append(15)  
    # gantt_times becomes: [0, 15]  
    # If current_time = 20, gantt_times becomes: [0, 15, 20]
    gantt_times.append(current_time)

# Prints table headers.
# :<10 means left align 10 character spaces
print(f"\n{'Process':<10} {'AT':<10} {'BT':<10} {'CT':<10} {'TT':<10} {'WT':<10}")

for i in range(n):
    # prints process number, arrival time number, and burst time number arranged in rows
    # {i+1} - if i=0, this becomes 1, so it prints "P1"
    # {arrival_time[i]:<11} - Gets arrival time from the list
    # if i=0 it gets the first arrival time
    # :<11 means left align 11 character spaces
    print(f"P{i+1:<10}{arrival_time[i]:<11}{burst_time[i]:<11}{completion_time[i]:<11}{turnaround_time[i]:<11}{waiting_time[i]:<11}")

# Adds all numbers in the list
# /n divides it by the number of processes
ATT = sum(turnaround_time)/n
AWT = sum(waiting_time)/n

# Prints gantt chart
print("\nGantt Chart:")

# len(gantt_order) - Counts how many items are in the gantt_order list
# Example: If gantt_order = ["P1", "P2", "P3"]: len(gantt_order) = 3
# then 3 will be multiplied by 8 = 24
# "-" * 24 - Repeats the dash line 24 times
print("-" * (len(gantt_order) * 8))

# "|" + ... + "|" this adds "|"" at the beginning and end
# "|".join() adds a | character between each item in the list
# Ex. If we have [" P1 ", " P2 ", " P3 "], output: "  P1   |  P2   |  P3   "
# f"{p:^7}" this formats each process name
# ^ this means center align
# 7 is the amount of spaces total
# for p in gantt_order - it loops through each process name
# ex. Example: If gantt_order = ["P1", "P2", "P3"], it will print "P1", then "P2", then "P3" each line
print("|" + "|".join(f"{p:^7}" for p in gantt_order) + "|")

# Prints another line of dashes same as before
print("-" * (len(gantt_order) * 8))

# Creates an empty string (empty text) to make the timeline
timeline = ""

# gantt_times[0] - Gets the first number from gantt_times list (usually 0)
timeline = str(gantt_times[0])

# len(gantt_times) - counts items in gantt_times list
# ex. range(1, 4) - Creates [1, 2, 3] (starts at 1, stops before 4)
# it starts at 1 because we already defined gantt_times[0]
for i in range(1, len(gantt_times)):

    # gantt_times[i] - Gets a time value from the list
    # ex. if gantt_times[1] = 5, needs 7 spaces
    # str(5) - converts to text: "5".
    # len("5") - counts how many characters (1 character)
    spaces_needed = 8 - len(str(gantt_times[i]))

    # add spaces and the next time number to the timeline
    # " " * 7 - creates 7 spaces
    # str(gantt_times[i]) - converts time to text: "5"
    # + - combines them: " 5"
    # += - adds to existing timeline
    timeline += " " * spaces_needed + str(gantt_times[i])
print(timeline)

# Shows how Average Turnaround Time was calculated
# for i in range(n) - loops through all processes (0, 1, 2...)  
# turnaround_time[i] - gets each waiting time  
# str(turnaround_time[i]) - converts to text  
# ' + '.join(...) - puts " + " between each number
# Example: If turnaround_time = [0, 3, 4]:  "0 + 3 + 4"
# {n} - shows how many processes (divisor)  
# {ATT:.2f} - shows result with 2 decimal places
print(f"\nAverage Turnaround Time: ({' + '.join(str(turnaround_time[i]) for i in range(n))}) / {n} = {ATT:.2f}")

# shows how Average Waiting Time was calculated
# waiting_time[i] Gets the waiting time for each process from the list
# str(waiting_time[i]) converts each number to string. Ex.  0 becomes "0"
# because join() only works with strings, not numbers.
# join() is used to combine elements into a single string, placing a chosen separator between each element
print(f"Average Waiting Time: ({' + '.join(str(waiting_time[i]) for i in range(n))}) / {n} = {AWT:.2f}")
