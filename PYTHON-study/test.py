'''  

We'd like to be able to determine which IP addresses are still blocked at a particular time based on the log. Write a program that uses the log file to tell us which IP addresses remain blocked at 2 AM (02:00:00.000)

For example, if we had the following log lines:
2021-05-07 00:45:30.034 Block 74.152.237.66
2021-05-07 00:55:05.984 Block 79.118.67.43
2021-05-07 01:05:52.435 Block 183.35.232.214
2021-05-07 01:13:08.376 Release 74.152.237.66
2021-05-07 01:15:23.802 Release 183.35.232.214
2021-05-07 02:05:52.435 Block 129.31.23.11
2021-05-07 02:55:05.984 Release 79.118.67.43

... then we would output "79.118.67.43".

Sample Output (in any format / order)
2.96.244.81
3.145.146.113
48.94.33.214
53.118.78.56
66.23.206.238
158.201.213.1
185.214.25.128

The file is at https://public.karat.io/content/test/test_log.txt

'''
import requests

url = "https://public.karat.io/content/test/test_log.txt"

response = requests.get(url)

file_path = "test_log.txt"

with open(file_path, "wb") as sh:
    sh.write(response.content)
with open(file_path, "r") as sh:
    blocked_lines = []
    released_lines = []
    for line in sh:
        parts=line.strip().split()
        if parts[2] == "Block":
            blocked_lines.append(line)
        else:
            released_lines.append(line)

print("Blocked lines: " + f"{len(blocked_lines)}")
print("Released lines: " + f"{len(released_lines)}")