# Q1)Convert the time entered in hh,min and sec into seconds.

hour=int(input("enter time in hours :"))
minute=int(input("enter time in minutes"))
sec=int(input("enter time in sec: "))
hour_sec= hour*3600
print('hours converts into seconds',hour_sec)
minute_sec=minute*60
print('minutes converts into seconds',minute_sec)
sec_sec= sec*1
print("seconds convert into seconds",sec_sec)

