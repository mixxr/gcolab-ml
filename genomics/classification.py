import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Sample DNA Data (Text sequences and their labels)
# 0 = Non-promoter, 1 = Promoter region
dna_sequences = ["ATGCGTACGTA", "TGCGTACGTAC", "GTACGTACGTA", "AAAAATTTTCC"]
labels = [1, 1, 0, 0]

# 2. Function to split DNA text into overlapping 3-mers
def get_kmers(sequence, size=3):
    return [sequence[x:x+size].lower() for x in range(len(sequence) - size + 1)]

# Convert sequences to space-separated k-mer strings
kmer_sequences = [" ".join(get_kmers(seq)) for seq in dna_sequences]

# 3. Vectorize: Convert text into numerical feature matrices
cv = CountVectorizer()
X = cv.fit_transform(kmer_sequences).toarray()
y = np.array(labels)

# 4. Train a Random Forest Classifier
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
classifier = RandomForestClassifier(n_estimators=100)
classifier.fit(X_train, y_train)

# 5. Predict
predictions = classifier.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, predictions) * 100}%")
