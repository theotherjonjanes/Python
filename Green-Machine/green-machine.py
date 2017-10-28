import datetime

now = datetime.datetime.now()

dateAndTime = now.strftime("%d-%b-%Y %I:%M%p")

f = open('green-machine.txt','a')
f.write('\n' + dateAndTime)
f.close()