from pywhatkit import whats

number = ['+6281959200036','08762762']

for i in number:
    whats.sendwhatmsg(i,'Halooo, ini dikirim lewat coding python dan pywhatkit',16,9,tab_close=True,close_time=3)
