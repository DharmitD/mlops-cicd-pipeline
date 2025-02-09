# 🚀 MLOps CI/CD Pipeline with OpenShift AI & Kubeflow

This repository provides an **end-to-end MLOps CI/CD pipeline** using **GitHub Actions, Kubeflow Pipelines (KFP), and OpenShift AI**. It automates the **entire machine learning lifecycle**, including:
- **Building & versioning ML images** (stored in Quay).
- **Generating & deploying Kubeflow DSL pipelines**.
- **Running model training & extracting ML metrics** (accuracy, precision, recall, confusion matrix, ROC curves, etc.).
- **Deploying trained models as an inference service**.

---

## 📌 **Features**
✅ **Automated ML Pipeline Generation** – Converts ML scripts into Kubeflow DSL.  
✅ **CI/CD with GitHub Actions** – Includes syntax checks, linting, and testing.  
✅ **Version Control for Builds** – Branch-specific image tagging and deployment.  
✅ **Production-Like Testing** – Deploys ML pipelines to a **Kind cluster** before OpenShift AI.  
✅ **Real-Time Model Deployment** – Serves trained models via **REST API**.  
