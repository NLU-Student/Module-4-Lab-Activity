str_time = input("What time is it now?")
str_wait_time = input("What is the number of hours to wait?") # nours = hours
time = int(str_time)
wait_time = int(str_wait_time) #wait was misspelled

time_when_alarm_go_off = time + wait_time
time_of_day = time_when_alarm_go_off % 24 #add % function to complete the progam
print(time_of_day)
