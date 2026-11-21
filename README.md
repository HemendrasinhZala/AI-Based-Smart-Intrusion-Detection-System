# 🛡️ AI-Based Smart Intrusion Detection System

An AI-powered security system designed to detect and monitor suspicious activities in real time. The project brings together **Computer Vision, Artificial Intelligence, and Multi-Sensor Fusion** to make intrusion detection smarter and more reliable.

It uses YOLOv8 to detect people, OpenCV to identify motion, and physical sensors to monitor movement and door activity. Based on the information collected from these sources, the system calculates a threat score and responds accordingly.

**Academic Recognition:** Developed as a GTU-approved academic project as part of the B.E. Artificial Intelligence and Machine Learning program at Ahmedabad Institute of Technology, affiliated with Gujarat Technological University (GTU).

---

## 🚀 Key Features

- **Human Detection:** Uses a pre-trained YOLOv8 model to identify people through the camera.
- **Motion Detection:** Uses OpenCV to detect movement in the monitored area.
- **Multi-Sensor Integration:** Combines camera input with PIR motion and magnetic door sensors.
- **Threat Scoring:** Evaluates detected activity and assigns a threat score.
- **Real-Time Monitoring:** Allows users to monitor the surroundings through a live camera feed.
- **Intrusion Recording:** Saves images and video recordings when suspicious activity is detected.
- **Alert System:** Uses a buzzer and three LEDs to indicate different threat levels.
- **Desktop Dashboard:** Provides a graphical interface built with PySide6.
- **Event Logging:** Keeps a record of detected activities for later review.

## 🧠 How the System Works

The system collects information from the camera and connected sensors. It processes these inputs, identifies possible intrusion activity, and calculates a threat score.

The overall workflow looks like this:

```text
             Camera Input
                  |
          OpenCV Processing
                  |
            YOLOv8 Detection
                  |
       -----------------------
       |                     |
  Motion Detection     Human Detection
       |                     |
       -----------------------
                  |
             Sensor Fusion
                  |
       -----------------------
       |                     |
    PIR Sensor          Door Sensor
       |                     |
       -----------------------
                  |
            Threat Scoring
                  |
             Threat Level
                  |
       -----------------------
       |          |          |
     Green      Yellow       Red
      LED         LED        LED
       |          |          |
       -----------------------
                  |
           Alerts & Logging
                  |
            GUI Dashboard
```

## ⚙️ Threat Level Classification

To make the system's response more meaningful, detected activities are evaluated using a threat score.

| Threat Score | Threat Level |
|---|---|
| 0–34 | Low |
| 35–69 | Medium |
| 70–100 | High |

The score helps the system decide which alert should be triggered. These are the intended classification ranges; the actual thresholds are defined in the project configuration.

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Computer Vision | OpenCV |
| Object Detection | YOLOv8 |
| Deep Learning | PyTorch |
| Numerical Processing | NumPy |
| GUI Development | PySide6 |
| Hardware Integration | GPIO Zero, RPi.GPIO |
| Target Platform | Raspberry Pi |

## 🔌 Hardware Requirements

The project is designed for a Raspberry Pi-based setup with the following components:

- Raspberry Pi 5 (target platform)
- Raspberry Pi Camera Module or USB Webcam
- HC-SR501 PIR Motion Sensor
- Magnetic Door Sensor
- Active Buzzer
- Green, Yellow, and Red LEDs
- 220Ω Resistors
- Jumper Wires
- Breadboard
- Suitable Power Supply

*Actual hardware operation depends on the connected components, GPIO configuration, and software environment.*

## 📁 Project Structure

```text
AI-Based-Smart-Intrusion-Detection-System/
│
├── assets/
│
├── core/
│   ├── camera.py
│   ├── human_detector.py
│   ├── intrusion_detector.py
│   ├── logger.py
│   ├── motion_detector.py
│   ├── recorder.py
│   ├── sound.py
│   ├── threat_scoring.py
│   └── utils.py
│
├── hardware/
│   ├── buzzer.py
│   ├── door_sensor.py
│   ├── gpio_manager.py
│   ├── led.py
│   └── pir_sensor.py
│
├── models/
│   └── yolov8n.pt
│
├── storage/
│   └── Runtime-generated images, videos and logs
│
├── tests/
│
├── ui/
│   ├── pages/
│   └── widgets/
│
├── app.py
├── app1.py
├── config.py
├── main_gui.py
├── requirements.txt
├── AI.pdf
├── SETUP_GUIDE.txt
│
└── README.md
```

## 💻 Installation and Setup

Follow these steps to set up the project on your system.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

### 2. Open the Project Folder

```bash
cd YOUR_REPOSITORY
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Environment

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / Raspberry Pi OS:**

```bash
source .venv/bin/activate
```

### 5. Install the Required Packages

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python app.py
```

**A quick note:** Some features depend on Raspberry Pi hardware and connected sensors. Make sure the GPIO configuration and hardware connections are set up correctly before running the complete system. You can also refer to `SETUP_GUIDE.txt` for additional instructions.

## 🔮 Future Improvements

There is still plenty of scope to improve the system. Some ideas for future development include:

- Adding more advanced object detection models.
- Sending intrusion alerts through a cloud service or mobile application.
- Building a mobile interface for remote monitoring.
- Using historical event data to improve threat assessment.
- Adding remote access and security management.
- Improving the accuracy of sensor fusion and threat scoring.

## 🎥 Project Demonstration

Want to see the system in action?

▶️ **[Watch the AI-Based Smart Intrusion Detection System Demo](https://drive.google.com/file/d/1jj3tKXgg7n-h1hYDP18Tn_SKWRGBnHM9/view?usp=sharing)**

The demonstration showcases the project setup and its intrusion detection alert system.

## 🎓 Academic Note

This project was developed as part of an academic project under Gujarat Technological University (GTU). It provided an opportunity to apply concepts from Artificial Intelligence, Computer Vision, and sensor integration to a practical security-related problem.

## 👨‍💻 Developer

**Hemendrasinh Zala**

B.E. Artificial Intelligence and Machine Learning  
Ahmedabad Institute of Technology  
Gujarat Technological University (GTU)

- **GitHub:** [HemendrasinhZala](https://github.com/HemendrasinhZala)
- **LinkedIn:** [Hemendrasinh Zala](https://www.linkedin.com/in/hemendrasinh-zala-9ab565410/)

## ⚠️ Disclaimer

This project was developed for academic and educational purposes. Its performance may vary depending on the environment, camera quality, hardware configuration, and sensor placement. It is intended as a demonstration of an AI-based security system and is not a replacement for certified professional security solutions.


