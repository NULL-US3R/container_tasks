#/bin/bash
sudo docker build -t tsk2img2 ./2 && sudo docker build -t tsk2img1 ./1
sudo docker run -v ./shared:/app/shared -d tsk2img2
sudo docker run -v ./shared:/app/shared -it tsk2img1
