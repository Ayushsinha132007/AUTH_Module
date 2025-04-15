# Multi-Factor Authentication System Integration with Windows

## Project Overview

This project implements a **Multi-Factor Authentication (MFA)** system that enhances the security of a Windows-based operating system. The system integrates a **QR code-based OTP** using **Google Authenticator** and ensures that users can securely log in by verifying their credentials (username, password, and OTP). It also locks the system if the authentication fails and runs as an **auto-start application** after login using **Windows Task Scheduler**.

## Features

- **Multi-Factor Authentication**: Combines **username/password** and **Google Authenticator OTP**.
- **Windows Integration**: Automatically runs the authentication GUI after login via **Task Scheduler**.
- **System Lock**: If incorrect credentials are provided, the system automatically locks.
- **Security**: Protects against common vulnerabilities such as buffer overflows and trapdoors.

## Project Structure

- **secure_login.py**: Main script to trigger the authentication process and lock the system if login fails.
- **gui.py**: Contains the graphical user interface for user login.
- **authenticator.py**: Handles OTP generation and verification via Google Authenticator.
- **TaskSchedulerSetup.bat**: A batch file to help set up the Task Scheduler for auto-running the script on login.

## Prerequisites

Before running this project, ensure the following are installed on your system:

- **Python 3.x**: You can download it from [Python's official site](https://www.python.org/downloads/).
- **Pip packages**:
  - **pyotp**: For generating OTP.
  - **qrcode**: For generating QR codes for Google Authenticator.

To install the necessary packages, run:

```bash
pip install pyotp qrcode
