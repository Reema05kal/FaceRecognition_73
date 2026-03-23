\# Real-Time Face Recognition System using OpenCV



\## 📌 Project Title



Real-Time Face Recognition System



---



\## 📖 Problem Statement



The objective of this project is to develop a real-time face recognition system that can detect and identify human faces from a live webcam feed. The system should accurately recognize known individuals using previously trained data.



---



\## 🎯 Objectives



\* To capture face images using webcam

\* To detect faces using OpenCV Haar Cascade

\* To train a face recognition model

\* To recognize faces in real-time

\* To display name and confidence level



---



\## 🛠️ Technologies Used



\* Python 3.x

\* OpenCV

\* NumPy

\* Haar Cascade Classifier



---



\## 💻 System Requirements



\* Windows 10/11 or Linux (Ubuntu)

\* Python 3.x

\* Webcam



---



\## 📂 Project Structure



```

face\_recognition\_project/

│

├── dataset/

├── trainer/

├── haarcascade/

├── face\_dataset.py

├── train.py

├── recognize.py

├── README.md

```



---



\## ⚙️ Installation Steps



1\. Clone the repository:



```

git clone https://github.com/yourusername/FaceRecognition\_73.git

```



2\. Navigate to project:



```

cd FaceRecognition\_73

```



3\. Create virtual environment:



```

python -m venv venv

```



4\. Activate environment:



\* Windows:



```

venv\\Scripts\\activate

```



\* Linux:



```

source venv/bin/activate

```



5\. Install dependencies:



```

pip install opencv-python numpy

```



---



\## ▶️ How to Run



\### Step 1: Capture Dataset


## Update 1: Dataset collection completed
```

python face\_dataset.py

```



\### Step 2: Train Model



```

python train.py

```



\### Step 3: Run Recognition



```

python recognize.py

```



---



\## 📸 Output



\* Detects face from webcam

\* Displays name (Reema, Thensin, Shana)

\* Shows confidence percentage



---



\## ⚠️ Challenges Faced



\* Camera not detected in WSL

\* Low accuracy in recognition

\* Handling multiple users



---



\## ✅ Result



The system successfully detects and recognizes faces in real time with good accuracy.



---



\## 🔮 Future Scope



\* Improve accuracy using Deep Learning

\* Add database integration

\* Deploy as a web application

\* Add attendance system



---



\## 📚 References



\* OpenCV Documentation

\* Python Documentation

\* Online tutorials



---



\## 👩‍💻 Author



Reema



