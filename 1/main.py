import time

while True:
    f = open("./shared/file.txt", "r")
    print(f.read())
    f.close();
    time.sleep(0.3)
