import time

start = input("Start timer")
start_time = time.perf_counter()

stop = input("Stop timer")
stop_time = time.perf_counter()

time = stop_time - start_time
time = round(time,3)
print("Your time was", time)