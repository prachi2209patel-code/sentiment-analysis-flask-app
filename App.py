from flask import Flask, request, render_template
import pickle
from preprocess import clean_text

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    result_class = ""
    emoji = ""

    if request.method == "POST":
        text = request.form.get("text")

        if not text or text.strip() == "":
            result = "Please enter text"
            result_class = "neutral"
            emoji = "😐"
        else:
            cleaned = clean_text(text)
            vectorized = vectorizer.transform([cleaned])
            prediction = model.predict(vectorized)[0]

            result = prediction

            if prediction.lower() == "positive":
                result_class = "positive"
                emoji = "😊"
            elif prediction.lower() == "negative":
                result_class = "negative"
                emoji = "😡"
            else:
                result_class = "neutral"
                emoji = "😐"

    return render_template(
        "index.html",
        result=result,
        result_class=result_class,
        emoji=emoji
    )

if __name__ == "__main__":
    app.run()

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)