CodeAlpha Task 3 – Secure Coding

Overview

This project was completed as part of the CodeAlpha Cybersecurity Internship.

The objective of this task was to review a simple Python login application, identify security vulnerabilities, and implement secure coding improvements.

Programming Language

- Python

Files Included

1. Insecure_App.py

This is the original login application used for the security review. It demonstrates basic insecure coding practices that were identified during manual inspection.

2. Secure_App.py

This is the improved version of the application.

Security improvements include:

- Password hashing
- Input validation
- Maximum of three login attempts
- Login blocking after repeated unsuccessful attempts

3. Security_Review_Report.md

This report documents:

- The application and programming language
- Manual security review method
- Security vulnerabilities identified
- Secure coding recommendations
- Remediation implemented
- Testing results

Testing

The secure application was tested using valid and invalid credentials.

A valid login displayed:

"Login successful"

After three unsuccessful login attempts, the application displayed:

"Login blocked. Maximum attempts reached."

Conclusion

This project demonstrates the importance of manual security review and secure coding practices. The original application was reviewed, security weaknesses were identified, and an improved version was implemented and tested.
