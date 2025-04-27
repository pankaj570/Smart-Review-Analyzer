## 🚀 Project: **Smart Product Review Analyzer & Decision Engine**

### 🎯 Goal:

Help an e-commerce company automatically:

1. Analyze product reviews (DS),
2. Predict if the review is from a churn-risk customer (ML),
3. Generate a custom reply to the customer (GenAI),
4. Make a decision via MCP (e.g., alert manager, send discount, escalate issue).

### 🧱 Architecture Overview

📦 Review Input
   │
   ├── 📊 Data Science (explore reviews, detect trends)
   │
   ├── 🤖 ML (predict churn or satisfaction score)
   │
   ├── ✍️ GenAI (generate personalized response)
   │
   └── 🧠 MCP (orchestrates all agents, makes final decision)

# 🔧 Tools Used

✅ **Data Science**

✅ **Machine Learning**

✅ **Generative AI (Gemini model)**

✅ **Multi-Context Protocol (MCP)**

✅ Optional UI: **Streamlit dashboard**

# Smart Review Analyzer

This project combines Data Science, ML, Generative AI (Gemini), and MCP to analyze customer reviews, predict churn, generate replies, and make decisions.

## Setup

1. **Install dependencies:** pip install -r requirements.txt
2. **Generate Traning Data** : python generate_large_reviews.py
3. **Train Model and Save as Pickle file** : python train_model.py
4. **Set your Gemini API key in a `.env` file**: GEMINI_API_KEY=your-api-key-here
5. **Run the app:** streamlit run dashboard/streamlit_app.py
