# 🛡️ Hacktify - Ethical Hacking Playground

Welcome to **Hacktify** — a safe and sandboxed vulnerable web application designed for **learning ethical hacking**, **practicing cybersecurity skills**, and **blue/red team exercises**.  
This project simulates real-world security flaws in a controlled environment and is fully documented with a YouTube walkthrough!

[🎥 **YouTube Channel**
](https://bit.ly/4d0x5WQ)

---

## 📜 Table of Contents
- [About Hacktify](#about-hacktify)
- [Built With](#built-with)
- [Getting Started](#getting-started)
- [Usage Guide](#usage-guide)
- [Vulnerabilities Included](#vulnerabilities-included)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## 🧩 About Hacktify

Hacktify is designed to mimic **real-world web security vulnerabilities** so that beginners and ethical hackers can safely practice their skills.  
The project is **Dockerized** to make it extremely easy to deploy and run anywhere!

**Core Features:**
- Vulnerable login system (SQL Injection)
- Hidden capture-the-flag (CTF) challenges
- Scoring system for successful exploits
- Beginner-friendly setup
- Complete YouTube documentation

⚠️ **Disclaimer:** This app is intentionally insecure and should only be used in a controlled environment for educational purposes!

---

## 🛠️ Built With

- [Python 3.11](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [SQLite3](https://www.sqlite.org/)
- [Docker](https://www.docker.com/)

---

## 🚀 Getting Started

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop) (for Windows/Mac)
- OR Docker Engine (Linux)

---

### Running Locally (without Docker)

```bash
# Clone the repository
git clone https://github.com/your-username/hacktify.git
cd hacktify

# Install Python dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```

Visit: [http://localhost:5000](http://localhost:5000)

---

### Running with Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/your-username/hacktify.git
cd hacktify

# Build the Docker image
docker build -t hacktify .

# Run the Docker container
docker run -d -p 5000:5000 hacktify
```

Access Hacktify at: [http://localhost:5000](http://localhost:5000)

---

## 🧠 Usage Guide

### Default Credentials
- **Username:** admin
- **Password:** adminpass

### Try SQL Injection
On the login page:
- Input username:
  ```text
  ' OR 1=1 --
  ```
- Password: anything.

This will **bypass login authentication** if the SQL Injection succeeds — leading you to the hidden **flag page**.

---

## 🧨 Vulnerabilities Included

| Vulnerability | Description |
|:--------------|:------------|
| SQL Injection | Login form directly injects user input into raw SQL queries without sanitization. |
| Weak Authentication | Default credentials included. |
| Sensitive Data Exposure | Flags hidden inside the app after successful exploits. |

---

## 🖼️ Screenshots

> (Add screenshots of login page, success page, flag capture, Docker run if you want!)

---

## 🎥 YouTube Documentation

📺 A full walkthrough video explaining:
- How Hacktify works
- How to setup & deploy
- How to exploit vulnerabilities
- How to capture hidden flags

Will be uploaded to YouTube soon!  
[**[Link]**](https://bit.ly/4d0x5WQ)

---

## 🤝 Contributing

Contributions are welcome to expand Hacktify into a full hacking playground!

Steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/yourFeature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/yourFeature`)
5. Open a Pull Request

---

## 🛡️ Created by

Made with ❤️ for ethical hacking learners and future cybersecurity experts.  
🔗 [[MohamedSelimMahjoub] ](https://bit.ly/3EHjUxa) 
🔗 [[[Ramez Hasenaoui] ]](https://github.com/RamezHas)
🎥 [[Your YouTube Channel](https://bit.ly/4d0x5WQ)] 

---

# 🚀 Happy Hacking with Hacktify!
