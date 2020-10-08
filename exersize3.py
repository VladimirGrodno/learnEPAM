#ложится спать в H-hours and M-minutes
#X - time for sleep in minutes
#need hours and minutes in which she has to wake up
X = int(input())
H = int(input())
M = int(input())
minutes1 = H * 60 + M
Y = minutes1 + X
hourswake = Y//60
minuteswake = Y%60
print (hourswake)
print (minuteswake)