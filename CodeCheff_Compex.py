uncompressed = str(raw_input())
uncompressed = list(uncompressed.split())
rows = uncompressed[0:1:1]
rows = int("".join(rows))
uncompressed = map(int, uncompressed)
start = 2
stop = 3

for number in range(0,rows):
    n = uncompressed[start:stop:1]
    n.append(0)
    def n_to_int(x):
        firstDigit = x[0]         
        return firstDigit
    n = n_to_int(n)
    n = float(n * 2.0)
    print n
    
    start += 2
    stop +=2





   



# In[7]:






