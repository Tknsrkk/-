# udp

https://github.com/Tknsrkk/dis-network/blob/master/checksum.py

[![GY3L90.png](https://s1.ax1x.com/2020/04/02/GY3L90.png)](https://imgchr.com/i/GY3L90)

## p2
Assuming that the ip address of A is a, the ip address of C is c.

From server to message stream:

To host A: source port:26145, destination port:7532. IP address: a

To host C: left:source port:7532, destination port:80. right: source port:26145, destination port:80. Both of them the destination IP address is c.


## p4

a. 01011100 的 01100101 的和为 11000001，其反码为 00111110。

b. 11011010 和 01100101 的和为 01000000,，其反码为 10111111。 

c.  只需要两个字节同一位不同即可。比如第一个字节为 01011101，第二个字节为 01100100；或者第一个字节为 01010100，第二个字节为 01101101。 
