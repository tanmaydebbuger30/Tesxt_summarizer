# Tesxt_summarizer
A simple web-based text summarization app using Hugging Face's DistilBART model and Gradio. Part of @GenAi


This is a lightweight and intuitive web application built using **Gradio** and **Hugging Face Transformers** to generate concise summaries from longer text passages. It uses the `distilbart-cnn-12-6` model from Hugging Face's library.

## 🔍 What It Does

- Accepts long paragraphs of text as input
- Returns a concise summary in seconds
- Simple, clean Gradio web interface

## 🧠 Model Used

- `sshleifer/distilbart-cnn-12-6`
  - A distilled version of Facebook’s BART model
  - Trained on the CNN/DailyMail dataset
  - Suitable for summarizing news and general content

## 🚀 How to Run

### 🔧 Installation

```bash
git clone https://github.com/yourusername/text-summarizer.git
cd text-summarizer
pip install torch transformers gradio
▶️ Launch the App
bash
Copy
Edit
python Textsummary.py
Then open the Gradio link in your browser to use the app.

🖼️ Example
Inpup
Costello's was a bar and restaurant in Midtown Manhattan, known for its famous patrons including Ernest Hemingway...
Output:
Costello's was a famous bar in Midtown Manhattan popular with writers like Hemingway and cartoonists. It featured iconic wall art.
📁 Files
Textsummary.py: Main Python script


👩‍💻 Author
Tanmay Pendharkar
