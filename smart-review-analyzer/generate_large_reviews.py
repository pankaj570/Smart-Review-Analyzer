import pandas as pd
import random

positive_phrases = [
    "Loved it", "Amazing product", "Excellent service", "Fast delivery", "Highly recommend",
    "Very satisfied", "Top quality", "Will buy again", "Awesome experience", "Friendly support"
]

negative_phrases = [
    "Terrible experience", "Very disappointed", "Never buying again", "Package arrived broken",
    "Worst customer service", "Delayed shipment", "Product was defective", "Horrible support",
    "Refund requested", "Extremely unhappy"
]

# Generate 5000 positive reviews
positive_reviews = []
for _ in range(5000):
    sentence = random.choice(positive_phrases) + ". " + random.choice([
        "Thanks for the great service.", 
        "Everything was perfect.", 
        "Five stars.", 
        "I'm impressed.", 
        "Best purchase ever."
    ])
    positive_reviews.append((sentence, 0))

# Generate 5000 negative reviews
negative_reviews = []
for _ in range(5000):
    sentence = random.choice(negative_phrases) + ". " + random.choice([
        "Worst experience of my life.", 
        "I want a refund.", 
        "Very poor quality.", 
        "Extremely dissatisfied.", 
        "Won't recommend to anyone."
    ])
    negative_reviews.append((sentence, 1))

# Combine and shuffle
all_reviews = positive_reviews + negative_reviews
random.shuffle(all_reviews)

# Save to CSV
df = pd.DataFrame(all_reviews, columns=["review_text", "label_churn"])
df.to_csv("app/data/large_reviews.csv", index=False)

print("✅ large_reviews.csv created with", len(df), "reviews.")
