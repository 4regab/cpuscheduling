print("First Come First Serve CPU Scheduling")
n = int(input("Number of Processes: "))
arrival_time = []
burst_time = []

for i in range(n):
    print(f"\nProcess P{i+1}:")
    AT = int(input("Arrival Time:"))
    BT = int(input("Burst Time:"))
    arrival_time.append(AT)
    burst_time.append(BT)

order = sorted(range(n), key=lambda i: arrival_time[i])

completion_time = [0] * n
waiting_time = [0] * n
turnaround_time = [0] * n
current_time = 0
gantt_order = []
gantt_times = [0]

for i in order:
    if current_time < arrival_time[i]:
        current_time = arrival_time[i]

    current_time = current_time + burst_time[i]
    CT = current_time
    completion_time[i] = (CT)

    TT = CT - arrival_time[i]
    turnaround_time[i] = (TT)

    WT = TT - burst_time[i]
    waiting_time[i] = (WT)

    gantt_order.append(f"P{i+1}")
    gantt_times.append(current_time)

print(f"\n{'Process':<10} {'AT':<10} {'BT':<10} {'CT':<10} {'TT':<10} {'WT':<10}")

for i in range(n):
    print(f"P{i+1:<10}{arrival_time[i]:<11}{burst_time[i]:<11}{completion_time[i]:<11}{turnaround_time[i]:<11}{waiting_time[i]:<11}")

ATT = sum(turnaround_time)/n
AWT = sum(waiting_time)/n

print("\nGantt Chart:")
print("-" * (len(gantt_order) * 8))
print("|" + "|".join(f"{p:^7}" for p in gantt_order) + "|")
print("-" * (len(gantt_order) * 8))

timeline = ""
timeline = str(gantt_times[0])

for i in range(1, len(gantt_times)):
    spaces_needed = 8 - len(str(gantt_times[i]))
    timeline += " " * spaces_needed + str(gantt_times[i])
print(timeline)

print(f"\nAverage Turnaround Time: ({' + '.join(str(waiting_time[i]) for i in range(n))}) / {n} = {ATT:.2f}")
print(f"Average Waiting Time: ({' + '.join(str(turnaround_time[i]) for i in range(n))}) / {n} = {AWT:.2f}")
