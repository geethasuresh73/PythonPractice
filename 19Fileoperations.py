import os


file1=open('./resources/config.cfg','r')
file2=open('./resources/config_new.cfg','w')
for line in file1:
    print(line)
    file2.write(line)
file1.close()
file2.close()
