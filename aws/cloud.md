# One-Day Cloud Preparation Plan (Technical Focus)

## **Morning (4-5 hours): Core Cloud Concepts and Compute Services**

### 1. **Cloud Computing Basics**
- **IaaS (Infrastructure as a Service)**: Virtual machines, storage, networks.
- **PaaS (Platform as a Service)**: Managed platforms for app deployment.
- **SaaS (Software as a Service)**: Cloud-based applications (e.g., Gmail, Office 365).

### 2. **Compute Services:**
- **AWS EC2 (Elastic Compute Cloud)**
  - Launching and managing EC2 instances.
  - **Auto-scaling**: Set up auto-scaling to handle traffic spikes.
  - **Types of EC2 Instances**: General-purpose, compute-optimized, memory-optimized.

- **Serverless Computing:**
  - **AWS Lambda**: Event-driven serverless functions.
  - **Use Case**: Create a simple Lambda function for an event (e.g., trigger on file upload to S3).

---

## **Afternoon (3-4 hours): Networking, Storage, and Database Services**

### 1. **Networking:**
- **AWS VPC (Virtual Private Cloud)**
  - Creating VPCs, subnets, route tables, and security groups.
  - **Internet Gateway**: Connect VPC to the internet.

- **Load Balancer (ELB)**: 
  - Set up **Application Load Balancer** for distributing traffic to EC2 instances.

- **AWS CloudFront (CDN)**: 
  - Set up a Content Delivery Network to serve static content globally.

### 2. **Storage:**
- **AWS S3 (Simple Storage Service)**
  - Creating buckets and uploading objects.
  - **Bucket Policies**: Manage access control for storing and retrieving files.

### 3. **Database Services:**
- **AWS RDS (Relational Database Service)**
  - Launching a PostgreSQL or MySQL database instance.
  - Connecting to RDS and performing CRUD operations.

---

## **Evening (2-3 hours): Security, IAM, and CI/CD**

### 1. **Security & IAM (Identity and Access Management):**
- **IAM Users & Roles**
  - Create users and assign roles with specific permissions.
  - Best practices: Use **Least Privilege** for access management.

### 2. **CI/CD (Continuous Integration & Deployment):**
- **AWS CodePipeline**: Automate the deployment process.
  - Set up a simple CI/CD pipeline to deploy code from GitHub/CodeCommit to EC2 or Lambda.
  
- **AWS CodeBuild**: Automate building of the application.

---

## **Quick Testing (1 hour):**
- **API Testing**: Use **Postman** or **Pytest** to test a simple API built on AWS Lambda or EC2.
- **Practice on AWS Free Tier**: Use the AWS Free Tier for practical, hands-on learning.

---

### **Key Topics to Focus On:**
- **AWS EC2**, **S3**, **RDS**, **VPC**, **IAM**, **Lambda**.
- **Basic Cloud Service Models**: IaaS, PaaS, SaaS.
- Hands-on practice with **serverless functions** using **AWS Lambda**.
- **Setting up and testing API deployments** (EC2 or Lambda).

---

### **Tips for Efficiency:**
- **Focus on Hands-On**: Real-world practice will give you the best understanding.
- **Prioritize Cloud Core Services** (EC2, S3, RDS, Lambda) and get practical experience with them.

