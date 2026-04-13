

# 🚨 Container Security Monitor

## 📌 Objective
To detect unauthorized privileged container activity and visualize real-time alerts using a simple monitoring dashboard.

---

## 🧠 Project Overview
This project simulates a real-world container security scenario where an attacker machine (Kali Linux) sends malicious requests to a vulnerable service running on Ubuntu. The system detects abnormal behavior and displays alerts in real time.

---

## 🏗️ System Architecture

```

Kali Linux (Attacker)
↓
Ubuntu (Flask Server + Detection Logic)
↓
Web Dashboard (Real-Time Alerts)

````

---

## ⚙️ Technologies Used

- Python (Flask)
- HTML, CSS, JavaScript
- Kali Linux (Attacker Machine)
- Ubuntu (Server Machine)
- VirtualBox (Virtualization)
- Networking (NAT Network)

---

## 🚀 Features

- 🔥 Simulated attack from Kali Linux
- 🚨 Real-time alert detection
- 🌐 Attacker IP tracking
- ⏱️ Timestamp logging
- 🔄 Auto-refresh dashboard
- 📊 Attack counter display

---

## 🛠️ Implementation Steps

### Step 1: Start Server (Ubuntu)
```bash
cd container-lab/dashboard
python3 server.py
````

---

### Step 2: Open Dashboard

Open browser:

```
http://127.0.0.1:5000
```

---

### Step 3: Trigger Attack (Kali Linux)

```bash
curl http://<Ubuntu_IP>:5000/run-attack
```

---

### Step 4: Detection

* Alert appears on dashboard
* Attacker IP is logged
* Timestamp is recorded

---

## 📸 Screenshots

### 🖥️ Dashboard

<img width="1535" height="738" alt="image" src="https://github.com/user-attachments/assets/d43efd2e-68f5-47d0-8a46-ef5e34f9f185" />


### ⚔️ Attack from Kali


<img width="824" height="433" alt="image" src="https://github.com/user-attachments/assets/6198376e-46a7-4bb4-a797-9f215e85a0ef" />

### 🚨 Alert Generated


<img width="1535" height="738" alt="image" src="https://github.com/user-attachments/assets/c511739b-93a6-4ba3-9033-33a9ee35097e" />

---

## 📊 Output

* Unauthorized container activity detected
* Attacker IP displayed
* Alerts updated in real time
* Attack counter increases dynamically

---

## 🧪 Sample Alert

```
Rule: Privileged Container Started
Priority: CRITICAL
Message: Unauthorized container activity detected from 10.0.2.x
Time: 22:40:28
```

---

## 🔍 Key Concepts

* Container Security
* Privileged Container Risk
* Attack Simulation
* Real-time Monitoring
* Intrusion Detection Basics

---

## ⚠️ Limitations

* Simulation-based (not full real attack)
* No kernel-level detection (Falco not integrated)
* Local network only

---

## 🔮 Future Scope

* 🔥 Integration with Falco (real-time kernel monitoring)
* 🤖 AI-based anomaly detection
* ☁️ Cloud deployment (AWS/Docker)
* 📩 Email/SMS alert system
* 📊 Advanced analytics dashboard

---

## 🎯 Conclusion

This project demonstrates how container-based attacks can be simulated, detected, and visualized in real time. It highlights the importance of container security and provides a foundation for building advanced intrusion detection systems.

---

## 👨‍💻 Author

* Your Name: Aliyu Gambo Abubakar
* Course: Computer Engineering
* Semester: 4th

---

## ⭐ Acknowledgment

This project was developed as part of academic learning to understand container security and real-time monitoring systems.

```




