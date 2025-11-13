# Deep Learning Projects Portfolio

Starting a portfolio of all my deep learning projects here.  
The main aim of this repository is to apply and build upon what I learnt during my Master’s in AI, while continuing to develop my skills and experience to pursue a career in deep learning.

---

## Technologies Used

### Pneumonia Detection
- **Languages & Frameworks:** Python, TensorFlow, Keras  
- **Libraries:** NumPy, Matplotlib  
- **Techniques:** Transfer Learning (MobileNetV2), Image Augmentation, Binary Classification  
- **Tools:** ModelCheckpoint, EarlyStopping, ReduceLROnPlateau, Precision/Recall/AUC Metrics  

### Behaviour Analysis & Safety Monitoring
- **Languages & Frameworks:** Python, TensorFlow, Keras  
- **Libraries:** OpenCV, NumPy, Matplotlib, Scikit-learn, Ultralytics YOLO  
- **Techniques:** Object Detection, Behavioural Cloning, Sequence Modelling (GRU, Bidirectional GRU), Class Balancing  
- **Tools:** ModelCheckpoint, EarlyStopping, ReduceLROnPlateau  

### Injury Prevention Robot
- **Languages & Frameworks:** Python, ROS (Robot Operating System)  
- **Libraries:** NumPy, OpenCV, MediaPipe, spaCy, YOLO  
- **Techniques:** Posture Analysis, Human Pose Estimation, Natural Language Processing (NER)  
- **Tools:** rospy, Custom Neural Entity Recognition Model  

### PDF Q&A System (RAG)
- **Languages & Frameworks:** Python, Streamlit  
- **Libraries:** pdfplumber, FAISS, OpenAI API, NumPy, LangChain  
- **Techniques:** Retrieval-Augmented Generation (RAG), Embedding Search, Text Chunking  
- **Tools:** GPT-4-Turbo, OpenAI Embeddings, RecursiveCharacterTextSplitter  

### AutoTrader Price Prediction Model
- **Languages & Frameworks:** Python, Scikit-learn, XGBoost, LightGBM  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, SHAP  
- **Techniques:** Regression Modelling, Feature Scaling, Ensemble Learning, Model Evaluation (R², RMSE)  
- **Models:** Random Forest, Gradient Boosting, AdaBoost, Decision Tree, Linear Regression, Voting Regressor  

---

## Projects Overview

### Pneumonia Detection
This project explores how computer vision and machine learning can be applied to detect pneumonia at its earliest stages. By analysing medical images, the model can flag potential cases for further review. The project reflects my interest in the medical field and my goal of leveraging AI to help save lives.  

The pneumonia dataset used in this project was obtained from Kaggle: [Chest X-Ray Pneumonia Dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia).

---

### Behaviour Analysis & Safety Monitoring
For this project, I developed a system designed to analyse human behaviour and identify factors that may lead to potential violence or harm. The system can be deployed in venues or events to monitor foot traffic, track how many people enter and leave, and ensure the safety of workers and attendees.  

The project uses computer vision techniques, including YOLO for object detection, and leverages behavioural cloning and video analysis of human behaviour patterns. Data processing is handled with NumPy, enabling real-time monitoring and analysis to support proactive safety measures.

---

### Injury Prevention Robot
For my master’s project, I designed an injury prevention robot aimed at environments that involve heavy lifting. The robot assists by carrying objects from one location to another, while monitoring workers’ posture to ensure they lift items with proper technique.  

The system leverages computer vision, ROS (Robot Operating System), MediaPipe, and a custom neural entity recognition (NER) model to analyse posture and provide real-time feedback. By combining robotics and AI, this prototype helps reduce the risk of workplace injuries and promotes safe lifting practices. Although the concept can be applied broadly, this prototype was developed specifically for industrial and warehouse settings.

---

### PDF Q&A System (RAG)
For this project, I developed a prototype system that allows users to upload a PDF and ask questions about its content. The document is split into chunks, converted into embeddings using OpenAI’s embedding models, and stored in a FAISS index for similarity search. GPT-4-turbo is then used to generate answers based on the most relevant sections.  

This project was built to explore how Retrieval-Augmented Generation (RAG) works and to gain hands-on experience with the approach. I am currently developing a full, in-depth version with a complete front-end and back-end architecture.

---

### AutoTrader Price Prediction Model
During my master’s, I developed a price prediction model for AutoTrader using their live dataset, as part of a project in partnership with Manchester Metropolitan University (MMU). The model leverages machine learning techniques to estimate vehicle prices based on multiple features.  

Please note that the dataset provided by AutoTrader cannot be shared, so it is not included in this repository.
