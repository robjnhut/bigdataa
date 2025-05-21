import streamlit as st
from pymongo import MongoClient
import pandas as pd
import time

st.title("📺 YouTube Comment Sentiment Dashboard")

client = MongoClient("mongodb://localhost:27017/")
db = client["youtube"]
collection = db["comments"]

placeholder = st.empty()

while True:
    comments = list(collection.find({}, {"_id": 0}))
    df = pd.DataFrame(comments)

    if not df.empty:
        sentiment_counts = df["sentiment"].value_counts()

        with placeholder.container():
            st.subheader("Sentiment Distribution")
            st.bar_chart(sentiment_counts)
            st.dataframe(df[["author", "text", "sentiment", "publishedAt"]].sort_values("publishedAt", ascending=False))

    time.sleep(5)