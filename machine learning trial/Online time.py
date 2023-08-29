'''
# Importing libraries
import ntplib
from time import ctime

#Setting NTP server address and adding functions
ntp_server_addr = 'time.google.com'
c = ntplib.NTPClient()
response = c.request(ntp_server_addr, version=3)
response.offset

#Printing date-time and Server IP below
print(ctime(response.tx_time))
print (ntplib.ref_id_to_text(response.ref_id))
'''






import ntplib
from time import ctime
import datetime

server = 'time.google.com'
ntpDate = None
client = ntplib.NTPClient()
response = client.request(server, version=3)
response.offset
ntpDate = ctime(response.tx_time)
print (ntpDate)
    
print( datetime.datetime.strptime(ntpDate, "%a %b %d %H:%M:%S %Y"))
