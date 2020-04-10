# p40
a.[1,6] and [23,26]. cwnd increases faster.  

b.[6,16] and [17,22]. cwnd grows linearly.  

c. triple duplicate ACK.  If there was a timeout, the congestion window size would be 1.   

d.timeout. The congestion window size is 1.  

e. 32. 2^5=32 is in[30,35]  

f. 21. half of the previous congestion windows size 42  

g.14. half of the previous congestion windows size 29 and round down  

h.the number of packet Sn=1(1-2^n)/1-2 for n<=6.63 packets is transmitted in the first 6 round, and packets 64-96 are sent in the 7th transmission round. Thus packet 70 is sent in the 7th transmission round.  

i.ssthresh = 8/2 = 4  

cwnd = ssthresh + 3MSS = 4+3 = 7  

j.threshold:21  

cwnd size:1  

k.1+2+4+8+16+21=52 packets
