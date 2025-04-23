## Arcom Deep Live Cam
Based on the "Deep-Live-Cam" project (https://github.com/hacksider/Deep-Live-Cam), I developed a solution that simplifies the process of adding faces and backgrounds to the correct folders. Once the faces and backgrounds are placed in the designated directories, the system automatically merges the faces onto the backgrounds. This streamlines the workflow and makes it more accessible for users. To enhance ease of use, the entire project has been Dockerized, ensuring smoother management and deployment. This solution leverages the deepfake and real-time face-swapping capabilities found in the "Deep-Live-Cam" project.

**Linux**:
```python
git clone https://github.com/jakub-ml/Arcom_Deep-Live-Cam
cd Arcom_Deep-Live-Cam
sudo docker pull jmfingoweb/faceswap
sudo docker run -v ./:/app -v ./zip:/root/.insightface jmfingoweb/faceswap
```

**Windows**:
```python
git clone https://github.com/jakub-ml/Arcom_Deep-Live-Cam
cd Arcom_Deep-Live-Cam
docker pull jmfingoweb/faceswap
docker run -v .\:/app -v .\zip:/root/.insightface jmfingoweb/faceswap
```

<p align="center">
  <img src="https://github.com/user-attachments/assets/68714331-66d6-47b4-9e04-b04b5a3c3e12" alt="image">
</p>
