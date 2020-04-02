# udp

https://github.com/Tknsrkk/dis-network/blob/master/checksum.py

[![GY3L90.png](https://s1.ax1x.com/2020/04/02/GY3L90.png)](https://imgchr.com/i/GY3L90)

## p2
Assuming that the ip address of A is a, the ip address of C is c.

From server to message stream:

To host A: source port:26145, destination port:7532. IP address: a

To host C: left:source port:7532, destination port:80. right: source port:26145, destination port:80. Both of them the destination IP address is c.


## p4

a.01011100 + 01100101 = 11000001
  Its one's complement : 00111110
  
b.11011010 + 01100101 = 01000000
  Its one's complement : 10111111
 
 c.The first byte: 01010100
   The second byte: 01101101
