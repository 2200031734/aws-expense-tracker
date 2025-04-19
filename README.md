
# 💸 AWS Expense Tracker Project

This is a simple serverless **Expense Tracker** project built using AWS services like **Lambda**, **API Gateway**, **DynamoDB**, and **SNS**.

## ✅ Features

- Add, delete, and view expenses via REST API
- Stores data in **DynamoDB**
- Triggers **SNS email alert** when an expense exceeds ₹5000
- Deployed with **AWS Lambda** and exposed via **API Gateway**

## 🔧 Technologies Used

- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- Amazon SNS (Simple Notification Service)
- Python (Boto3)

## 📁 Project Structure

```
📦aws-expense-tracker
 ┣ 📜 README.md
 ┣ 📜 lambda_function.py
 ┣ 📜 test-events.json
```

## 📩 SNS Alert Example

When an expense is added with amount > ₹5000, you'll receive an email like:
```
⚠️ High Expense Alert!
Amount: ₹5500
Category: Electronics
Date: 2025-04-19
```

## 📽️ YouTube Demo

📌 Watch the full video demo: [https://youtu.be/rz0KNsUNSOg]

## 📌 How to Use

1. Deploy `lambda_function.py` to AWS Lambda
2. Create API Gateway endpoints (POST, GET, DELETE)
3. Connect Lambda with DynamoDB and SNS
4. Subscribe your email to the SNS topic and confirm
5. Use Postman or HTML Form to interact with the API

---

👨‍💻 Developed by Mouktika
