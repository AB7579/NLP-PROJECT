import gradio as gr
import joblib
from clean import clean_text

# Load the trained classifier
pipeline = joblib.load('sentiment-analysis-model.joblib')

# Define a function to predict the sentiment of a given text
def predict_sentiment(text):
    # Clean the input text
    cleaned_text = clean_text(text)

    # Make a prediction on the input text
    predicted_label = pipeline.predict([cleaned_text])[0]

    return predicted_label

# Define the Gradio interface
interface = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.inputs.Textbox(label="Enter text here"),
    outputs=gr.outputs.Label(label="Sentiment"),
    title="Sentiment Analysis",
    description="This model predicts the sentiment of input text as positive, negative, or neutral."
)

# Launch the interface
interface.launch()
