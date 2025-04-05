from textblob import TextBlob

print("Hello! I'm a Sentiment Bot. Type 'exit' to stop.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    blob = TextBlob(user_input)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        print("Bot: 😊 That sounds positive!")
    elif sentiment < 0:
        print("Bot: 😟 That sounds negative.")
    else:
        print("Bot: 😐 That seems neutral.")
