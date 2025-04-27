from app.agents.data_agent import analyze_review_data
from app.agents.ml_agent import load_model, predict_churn
from app.agents.genai_agent import generate_response
from app.agents.decision_agent import make_decision
from app.utils.preprocess import clean_text

def run_pipeline(review_text):
    review_text = clean_text(review_text)
    # Load the ML model and predict churn risk
    model, vectorizer = load_model()
    churn_risk = predict_churn(review_text, model, vectorizer)
    print(f"Predict Churn Risk: {churn_risk}")
    
    insights = analyze_review_data(review_text)
    print(f"Insights: {insights}")
    
    # Generate a response using the GenAI agent
    reply = generate_response(f"Customer said: '{review_text}'. Write a polite reply.")
    # Make a decision based on the churn risk and insights
    print(f"Reply: {reply}")
    decision = make_decision(churn_risk, insights)
    print(f"Decision: {decision}")
    return {"reply": reply, "decision": decision}
