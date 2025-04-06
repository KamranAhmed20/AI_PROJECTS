import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')

faqs = {
    "What is the return policy?": "You can return any item within 30 days of purchase.",
    "How do I track my order?": "You can track your order using the tracking number sent to your email.",
    "What are the payment options?": "We accept all major credit cards and PayPal.",
    "How can I contact customer support?": "You can contact customer support via email or phone."
}

def preprocess(text):
    stemmer = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    filtered_tokens = [stemmer.stem(word) for word in tokens if word.isalnum() and word not in stop_words]
    return ' '.join(filtered_tokens)

def build_faq_system(faqs):
    questions = list(faqs.keys())
    answers = list(faqs.values())
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(questions)
    return vectorizer, vectors, answers

def get_response(user_query, vectorizer, vectors, answers):
    user_query = preprocess(user_query)
    query_vector = vectorizer.transform([user_query])
    similarities = cosine_similarity(query_vector, vectors)
    index = similarities.argmax()
    return answers[index]

def main():
    vectorizer, vectors, answers = build_faq_system(faqs)
    
    print("Welcome to the FAQ chatbot! Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        response = get_response(user_input, vectorizer, vectors, answers)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
