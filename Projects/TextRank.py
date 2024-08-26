import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import numpy as np
import networkx as nx

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Example text
text = """
Time-division multiplexing (TDM) is a method of transmitting and receiving independent signals over a common signal path by means of synchronized switches at each end of the transmission line so that each signal appears on the line only a fraction of time according to agreed rules, e.g. with each transmitter working in turn. It can be used when the bit rate of the transmission medium exceeds that of the signal to be transmitted. This form of signal multiplexing was developed in telecommunications for telegraphy systems in the late 19th century but found its most common application in digital telephony in the second half of the 20th century.
"""

# Preprocess the text: tokenize sentences and words, and remove stopwords
def preprocess_text(text):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english'))
    cleaned_sentences = []
    for sentence in sentences:
        words = word_tokenize(sentence)
        filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
        cleaned_sentences.append(' '.join(filtered_words))
    return sentences, cleaned_sentences

# Compute similarity between two sentences
def sentence_similarity(sent1, sent2):
    words1 = set(sent1.split())
    words2 = set(sent2.split())
    common_words = words1.intersection(words2)
    if len(words1) + len(words2) - len(common_words) == 0:
        return 0
    return len(common_words) / (len(words1) + len(words2) - len(common_words))

# Build the similarity matrix
def build_similarity_matrix(sentences):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
    
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i != j:
                similarity_matrix[i][j] = sentence_similarity(sentences[i], sentences[j])
    
    return similarity_matrix

# Summarize the text
def summarize_text(text, num_sentences=3):
    sentences, cleaned_sentences = preprocess_text(text)
    similarity_matrix = build_similarity_matrix(cleaned_sentences)
    
    # Create a graph from the similarity matrix
    nx_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(nx_graph)
    
    # Rank sentences based on scores
    ranked_sentences = [sentences[i] for i in sorted(scores, key=scores.get, reverse=True)]
    
    # Return the summary with the top-ranked sentences
    return ' '.join(ranked_sentences[:num_sentences])

# Generate and print the summary
summary = summarize_text(text, num_sentences=2)
print("Summary:")
print(summary)

