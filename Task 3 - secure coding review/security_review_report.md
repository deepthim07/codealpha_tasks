#Security Review Report

1. Programming Language and Application

Programming Language: Python

Application: Simple Python Login Application

The application was selected for a basic security review. It accepts a username and password from the user and verifies the entered credentials.

2. Review Method

A manual code review was performed by inspecting the Python source code and identifying insecure coding practices.

The review focused on:

- Credential handling
- Password protection
- User input validation
- Login attempt control
- Secure coding practices

3. Introduction

This report reviews a simple Python login application and identifies security weaknesses in the application. The purpose of this review is to understand common security problems and apply secure coding practices.

4. Application Reviewed

The application is a basic Python login program. It asks the user to enter a username and password and checks the entered credentials before displaying a login result.

The original application was intentionally kept simple so that common security weaknesses could be identified through manual inspection.

5. Security Issues Identified

5.1 Hardcoded Credentials

The original application stores the username and password directly in the source code.

Risk:
Anyone who can access the source code may be able to see the credentials.

Recommendation:
Sensitive credentials should not be hardcoded. They should be stored securely using environment variables or a secure database.

5.2 Plain-Text Password Handling

The original application handles the password directly during the login process.

Risk:
If credentials are exposed or stored insecurely, the password could be compromised.

Recommendation:
Passwords should be protected using a dedicated password-hashing method such as Argon2 or bcrypt.

5.3 Insufficient Input Validation

The original application does not perform sufficient validation of user input.

Risk:
Unexpected or malicious input could cause security problems in a larger application.

Recommendation:
Validate user input before processing it and reject empty or invalid input.

5.4 Unlimited Login Attempts

The original application does not restrict the number of incorrect login attempts.

Risk:
An attacker could repeatedly try different passwords.

Recommendation:
Implement login-attempt limits, rate limiting, or temporary account lockout.

6. Secure Coding Recommendations

- Do not hardcode passwords.
- Use secure password hashing.
- Validate user input.
- Limit repeated login attempts.
- Keep sensitive information outside the source code.
- Use secure error messages.
- Keep software and dependencies updated.

7. Remediation Implemented

A secure version of the application was created as "Secure_App.py".

The following improvements were implemented:

1. Password hashing was used instead of comparing the password directly.
2. Empty username and password inputs are rejected.
3. Login attempts are limited to three attempts.
4. After three unsuccessful attempts, the application blocks further login attempts.

8. Testing

The secure application was tested using both valid and invalid credentials.

Successful Login Test

Valid credentials were entered and the application displayed:

Login successful

Failed Login Test

Incorrect credentials were entered repeatedly.

The application displayed the remaining number of attempts and, after three unsuccessful attempts, displayed:

Login blocked. Maximum attempts reached.

This confirmed that the login-attempt protection was functioning as expected.

9. Remediation Summary

Security Issue| Remediation
Hardcoded/plain-text credential handling| Password protection using hashing
Insufficient input validation| Empty input is rejected
Unlimited login attempts| Maximum of three attempts
Lack of secure coding practices| Secure version created and tested

10. Conclusion

The manual security review identified several weaknesses in the original login application. A secure version was then created to demonstrate practical remediation.

The improved application uses password hashing, input validation, and a limit on failed login attempts. Testing confirmed that valid credentials allow login while repeated incorrect attempts result in the login being blocked.

This exercise demonstrates the importance of identifying security vulnerabilities during code review and applying secure coding practices to reduce security risks.
3. Security Issues Identified

3.1 Hardcoded Credentials

The application stores the username and password directly in the source code.

Risk:
Anyone who can access the source code may be able to see the credentials.

Recommendation:
Sensitive credentials should not be hardcoded. They should be stored securely using environment variables or a secure database.

3.2 Plain-Text Password

The password is handled as plain text.

Risk:
If the source code or stored information is exposed, the password may also be exposed.

Recommendation:
Passwords should be stored using secure password hashing methods such as bcrypt or Argon2.

3.3 Input Validation

The application accepts user input without sufficient validation.

Risk:
Unexpected or malicious input could cause security problems in a larger application.

Recommendation:
User input should be validated before it is processed.

3.4 Unlimited Login Attempts

The application does not restrict the number of incorrect login attempts.

Risk:
An attacker could repeatedly try different passwords.

Recommendation:
Use login-attempt limits, rate limiting, or temporary account lockout.

4. Secure Coding Recommendations

- Do not hardcode passwords.
- Use secure password hashing.
- Validate user input.
 Limit repeated login attempts.
- Keep sensitive information outside the source code.
- Use secure error messages.
- Keep software and dependencies updated.

5. Conclusion

The application demonstrates a basic login process but contains several security weaknesses. Improving credential storage, password protection, input validation, and login-attempt controls can make the application more secure.

This review demonstrates the importance of applying secure coding practices when developing applications that handle user credentials.