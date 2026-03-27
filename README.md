# 🍷 Wine Quality Predictor: End-to-End ML Architecture

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://winequalitypredictionproject.streamlit.app/)
[![FastAPI Backend](https://img.shields.io/badge/FastAPI-Backend_Live-009688?logo=fastapi)](https://vercel-fastapi-dk2xhy2rd-jahanzaibshah234s-projects.vercel.app/)

## Overview
This project is a complete, production-ready Machine Learning web application that predicts the quality of red wine based on its chemical properties.

Instead of a monolithic script, this project demonstrates a professional **two-tier architecture**: a decoupled Python frontend and backend communicating via a REST API. The underlying model has been trained to classify wine into three human-readable categories: **Good**, **Average**, or **Bad**.

## 🏗️ System Architecture
1. **Frontend (Streamlit Community Cloud):** A responsive, interactive user interface that gathers user input and sends JSON payloads across the internet.  
2. **Backend API (Vercel Serverless):** A lightning-fast FastAPI service that catches the request, validates the data using Pydantic, and executes the machine learning inference.  
3. **Machine Learning Model:** A pre-trained Random Forest Classifier loaded dynamically into the API.

## ✨ Key Features
* **Real-time Predictions:** Instantly outputs a classification based on 11 chemical features (e.g., pH, Alcohol %, Density, Acidity).  
* **Imbalanced Data Handling:** The Random Forest model utilizes `class_weight="balanced"` to accurately identify rare "Good" and "Bad" wines, preventing the model from lazily defaulting to the majority "Average" class.  
* **Target Mapping:** Raw quality scores (0-10) were mapped to categorical string labels during preprocessing so the model natively outputs plain English.  
* **Scale-Agnostic:** Because tree-based models handle non-linear data well, the pipeline is lean and does not require a scaler object for inference.

## 🛠️ Tech Stack
* **Machine Learning:** `scikit-learn`, `pandas`, `numpy`, `joblib`  
* **Backend API:** `FastAPI`, `uvicorn`, `pydantic`  
* **Frontend UI:** `Streamlit`, `requests`  
* **Cloud Deployment:** Streamlit Community Cloud (Frontend) & Vercel (Backend)

## 📁 Repository Structure
* `app.py`: The Streamlit frontend application.  
* `main.py`: The FastAPI backend application.  
* `wine_quality.pkl`: The serialized Random Forest model.  
* `requirements.txt`: The master dependency list required to run both services.  
* `winequality-red.csv`: The original UCI machine learning dataset.

## 🚀 How to Run Locally

If you want to run this architecture on your own machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jahanzaibshah234/wine_quality_prediction_project.git
   cd wine_quality_prediction_project
