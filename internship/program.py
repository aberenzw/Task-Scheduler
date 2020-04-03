import json
import subprocess
import threading
import datetime
import time

def main():
    with open('/home/aberenzw/internship/config.json') as f:
        data = json.load(f)
    threading.Thread(target=check_time).start()
    while(True):
        name = raw_input("Enter task name: \n")
        found = False
        for i in range(len(data["task_config"])):
            if(data["task_config"][i]["task_name"] == name):
                threading.Thread(target=call_program,args=
                ("python",data["task_config"][i]["task_location"])).start()
                found = True
        if(found == False):
            print("program not found")

def call_program(language, location):
    subprocess.call([language, location])

def check_time():
    with open('/home/aberenzw/internship/config.json') as f:
        data = json.load(f)
    while(True):
        time.sleep(60)
        for i in range(len(data["task_config"])):
            if (data["task_config"][i]["task_scheduled"] == "true"):
                scheduled_time = data["task_config"][i]["task_scheduled_time"]
                if (str(datetime.datetime.now().hour) == scheduled_time[0:2] and
                str(datetime.datetime.now().minute) == scheduled_time[3:5]):
                    threading.Thread(target=call_program,args=
                    ("python",data["task_config"][i]["task_location"])).start()

if __name__ == "__main__":
    main()
