#!/home/michiel/Code/suid-python

from sevensegment import sevensegment
import time
import _mysql

s=sevensegment.SevenSegmentDisplay()
con=None


try:
    con = _mysql.connect('localhost', 'lcd', 'lcd', 'radius')
    con.query("""SELECT COUNT(DISTINCT `acctuniqueid`) FROM `radacct` WHERE `acctstarttime` IS NOT NULL && `acctstoptime` IS NULL && `nasporttype` = "Wireless-802.11"; """)
    
    result = con.use_result()
    
    num_online = int(result.fetch_row()[0][0])

    print("%d users are online!" % num_online)

    s.set(num_online)

except sevensegment.NumberOutOfRange:
    print("That number is out of range")

except _mysql.Error, e:
    
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

finally:
    
    if con:
        con.close()


