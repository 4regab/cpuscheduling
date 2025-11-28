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
    current_time = current_time + burst_time[i]
    CT = current_time
    completion_time[i] = (CT)

    # Turnaround Time = Completion Time - Arrival Time (Total time from arrival to completion)
    TT = CT - arrival_time[i]
    turnaround_time[i] = (TT)

    # Waiting Time = Turnaround Time - Burst Time (Time spent waiting for CPU)
    WT = TT - burst_time[i]
    waiting_time[i] = (WT)

    # Records which process ran and when it finished
    gantt_order.append(f"P{i+1}")
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
    print(
        f"P{i+1:<10}{arrival_time[i]:<11}{burst_time[i]:<11}{completion_time[i]:<11}{turnaround_time[i]:<11}{waiting_time[i]:<11}")

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

print(
    f"\nAverage Turnaround Time: ({' + '.join(str(waiting_time[i]) for i in range(n))}) / {n} = {ATT:.2f}")
print(
    f"Average Waiting Time: ({' + '.join(str(turnaround_time[i]) for i in range(n))}) / {n} = {AWT:.2f}")
