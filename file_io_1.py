print ("")

f = open("sportsinfo.txt", "r")
print(f.read(6))

print ("")

f = open('sportsinfo.txt', "r")
file_list = f.readlines()
for line in file_list:
  print(line)

 