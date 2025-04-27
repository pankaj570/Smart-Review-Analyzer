from app.mcp_controller import run_pipeline

if __name__ == "__main__":
    review = "Product didn't arrive yet, very disappointed."
    result = run_pipeline(review)
    print(result)
