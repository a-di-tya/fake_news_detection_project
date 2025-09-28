import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
df = pd.read_csv('fake_news.csv')
df = df.dropna()

# Ensure correct column names
if 'text' not in df.columns or 'label' not in df.columns:
    raise ValueError("Dataset must have 'text' and 'label' columns.")

# Encode labels (e.g., "fake" -> 1, "real" -> 0)
label_encoder = LabelEncoder()
df['label'] = label_encoder.fit_transform(df['label'])

# Split into features and labels
X = df['text']
y = df['label']

# Vectorize text data
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(X)

# Split data for training/testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the model and vectorizer
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))
