import time
import csv
import datetime

# Declaring list of paths
paths_list = ['Competitve Coding' , 'Web Development' , 'Algorithms' , 'Making your own way in the world' , 'ClassWork', 'Exit']
paths_time = {'Competitve Coding' : 0 , 'Web Development' : 0 , 'Algorithms' : 0 , 'Making your own way in the world' : 0 , 'ClassWork': 0}

#####################   Functions  ##########################
# Function to show all options and take input for path
def Hello():
    # Printing all paths
    print('\n What are you working on?')
    for i in range(6):
        print ("    " + str(i+1) + ".  " + paths_list[i])
    # User input for path chosen
    path_key = paths_list[int(input('>>>  ')) - 1]
    return path_key

# function to measure time elapsed
def time_log():

    print('\n Type start on promt to start working. Type pause at any moment to pause time log. Type stop when your are done to log your progress')
    user_input = input(">>>  ")

    start_time = time.time()

    print(' Logging your time..............')
    user_input = input('>>>  ')

    if(user_input == 'stop' ):
        end_time = time.time()

    time_elapsed = end_time - start_time
    return time_elapsed

def exit_function():
    print("\n This session's log is:\n")
    for i in paths_time.keys():
        print(" " + i + "  --->  "  + time_format(paths_time[i]))

    print(" K THNX BYE ")
# Export log to excel sheet
def export_to_sheet(prev_total):

    file = open('codelog_logs.csv' , 'a')
    writer = csv.writer(file)

    data = [str(datetime.date.today())]
    present_day = 0

    for i in range(5):
        present_day += paths_time[paths_list[i]]
        timestring = time_format(paths_time[paths_list[i]])
        data.append(timestring)

    data.append(time_format(present_day))
    data.append(time_format(present_day+prev_total))
    writer.writerow(data)
    file.close()
#Covert time format
def time_format(secs):
    te_hours = int(secs/3600)
    te_mins = int(secs/60)
    te_secs = int(secs%60)
    timestring = str(te_hours) + 'H' + str(te_mins) + 'M' + str(te_secs) + 'S'
    return timestring

def total_time():
    file = ('codelog_logs')
    reader = csv.reader(file)
    reader = list(reader)
    time_string = reader[-1][-1]
    time_string_list = time_string.split()
    sec_int=0
    sec_string=''
    for i in time_string_list:
        if i=='H' or i == 'M' or i == 'S':
            sec_int += int(sec_string)
            sec_string=''
        else:
            sec_string += i
    return sec_int


###################   Main Function  #########################
print(' Welcome back!')
prev_total = total_time()
while True:

    path_key = Hello()

    # Exit loop and stop script if exit option chosen
    if path_key == 'Exit':
        export_to_sheet(prev_total)
        exit_function()
        break

    # Logging time in Dict paths_time and Displaying
    time_elapsed = time_log()
    paths_time[path_key] += time_elapsed

    print(" You have been working for --->        " + time_format(time_elapsed))
