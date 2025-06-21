# gestures
 Hand Gesture Recognition with OpenCV &amp; MediaPipe! 🤚
I'm excited to share a simple yet powerful real-time hand gesture recognition project I recently worked on using Python, OpenCV, and Google’s MediaPipe framework.

🔍 What it does:
This script uses a webcam to detect a single hand and analyze its 21 key landmarks. Based on the position of fingers (open or closed), it can recognize various gestures like:

✔️ Open Palm
✔️ Fist (Closed)
✔️ Thumbs Up
✔️ Peace ✌️
✔️ I Love You 🤟
✔️ Rock 🤘
✔️ Index Finger
✔️ Gun
✔️ Spider-Man 🕷️
…and more!

🧠 How it works:

MediaPipe Hands detects hand landmarks in real time.

We track the x/y coordinates of each finger tip and joints.

By comparing these points, we determine which fingers are up or down.

A list of binary values represents the finger states (1 = up, 0 = down), which maps to specific gestures.

The gesture name and finger count are overlaid live on the video feed.

📌 Tech Used:

Python

OpenCV

MediaPipe

Computer Vision

Real-Time Gesture Detection

💡 Applications:

Sign language interpretation

Human-computer interaction

Gesture-based control systems

Virtual reality input

Touchless interfaces
