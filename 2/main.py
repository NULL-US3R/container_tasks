import time

while True:
    f = open("./shared/file.txt", "w")
    f.write(time.asctime(time.gmtime(time.time())))
    f.close()
    time.sleep(1)
