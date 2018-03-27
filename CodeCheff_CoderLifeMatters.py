days = []
share = raw_input("Numbers:").split()
for word in share:
    days.append(word)
test_cases = days[:1:]
for number in test_cases:
    cases = int(number)
count = 31
startup = 2

for number in range(0,cases):
    start = int(startup)
    line = days[start:count:1]
    str_lines = str(line)
    str_line = "".join(line)
    happines = "111111"
        
    if happines in str_line:
        print "#coderlifematters"
    else:
        print "#allcodersarefun"
    startup = int(startup + 30)
    count = int(count+30)


