import datetime
import time
import webbrowser

class Awakening():
        def __init__(self,hour,minute,is_alarm_set = False):
                self.hour = hour
                self.minute = minute
                self.is_alarm_set = is_alarm_set
                
        def alarm(self):
                while True:
                    if datetime.datetime.now().hour == self.hour and datetime.datetime.now().minute == self.minute:
                        print("Wake-up neuille")
                        webbrowser.open("https://www.youtube.com/watch?v=k85mRPqvMbE")
                        self.is_alarm_set = False
                        break
                    else :
                        print(datetime.datetime.now())
                        time.sleep(60)
                                                  
        def set_alarm(self,hour,minute):
            self.hour = hour
            self.minute = minute
            self.is_alarm_set = True
            self.alarm()        
            
if __name__ == "__main__":
   while True:
        try:
         hour = int(input("Choose the hour : "))
         minute = int(input("Choose the minute : "))
           
         if hour >= 0 and hour <= 23 and minute >= 0 and minute <= 59:
          print("Alarm set for :",hour,"h",minute)
          print("Your alarm is set for :",hour,"h",minute)
          break
         else:
             print("please enter a valid hour and minute")
        except: ValueError
        print('Please enter a valid number')
    
a = Awakening(hour,minute)
a.set_alarm(hour,minute)

        
            

                
            