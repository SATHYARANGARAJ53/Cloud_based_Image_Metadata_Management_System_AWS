# Cloud-Based Image Metadata Management System

## 📌 Project Goal
The goal of this project is to develop an automated cloud-based image metadata management system that captures and stores essential metadata whenever an image is uploaded to cloud storage. The project demonstrates how serverless AWS services can be integrated to perform event-driven processing and maintain structured metadata records efficiently.

---

## 📖 About the Project
The Cloud-Based Image Metadata Management System is a serverless AWS application designed to automatically process image uploads and maintain their metadata in a centralized database. Whenever a user uploads an image into Amazon S3, an S3 object-created event automatically triggers an AWS Lambda function.

The Lambda function extracts metadata such as image file name, file size, file type, upload timestamp, and bucket information. This extracted metadata is then stored into Amazon DynamoDB for future retrieval and management.

This project showcases an event-driven cloud workflow where no manual processing is required after image upload, making the system efficient, scalable, and fully automated.

---

## ✨ Key Features
- Upload image files into cloud storage
- Automatic metadata extraction upon image upload
- Stores image name, size, type, bucket, and upload timestamp
- Serverless event-driven architecture
- Real-time metadata insertion into DynamoDB
- Secure AWS IAM role-based permissions
- Fully automated processing without manual intervention

---

## 🛠 Tech Stack Used

- **Amazon S3** – Cloud object storage service used to upload and store image files.

- **AWS Lambda** – Serverless compute service used to automatically extract metadata when an image is uploaded.

- **Amazon DynamoDB** – NoSQL database service used to store extracted image metadata records.

- **AWS IAM** – Identity and Access Management service used to securely provide permissions between AWS resources.

---

## 🌍 Why This Project Matters
In many cloud applications, files are uploaded continuously and maintaining their metadata manually becomes inefficient and error-prone. This project solves that challenge by introducing an automated event-driven architecture where metadata is captured instantly upon file upload.

The system demonstrates the practical use of serverless computing, cloud storage events, and NoSQL metadata management, reflecting real-world cloud automation workflows used in enterprise environments.

---

## 📚 What I Gained From This Project
Through this project, I gained practical hands-on experience in:
- creating and configuring S3 buckets for cloud file storage,
- developing AWS Lambda functions for automatic serverless processing,
- configuring S3 event triggers for real-time Lambda invocation,
- extracting and storing structured metadata into DynamoDB,
- handling IAM role permissions between AWS services,
- understanding event-driven serverless cloud architecture,
- and implementing automated metadata workflows without traditional servers.

This project significantly improved my understanding of AWS serverless application design.

---

## ✅ Project Workflow
User uploads image into Amazon S3  
→ S3 object-created event triggers AWS Lambda  
→ Lambda extracts image metadata  
→ Metadata stored into Amazon DynamoDB  
→ Records available for cloud-based metadata management
