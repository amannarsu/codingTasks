# importing libraries
import spacy
import pandas as pd
from spacytextblob.spacytextblob import SpacyTextBlob

# Load language model
nlp = spacy.load('en_core_web_sm')
# Add spacytextblob extension
nlp.add_pipe('spacytextblob')
# sample text review for testing
my_text = "I dont like this bottle of juce, there is not enough fruit in it and too much sugar!!"
# file nor NPL processing, forcing dtype to str and low mem to falce to prevent processing errors
file_read = pd.read_csv('amazon_product_reviews.csv', low_memory=False, dtype=str)
# selected the required column for our processing that contains the reviews
reviews_data = pd.DataFrame(file_read['reviews.text'], columns=['reviews.text'])
# removing any blank rows from the dataset
clean_data = reviews_data[0:20].dropna()

# Function to clean the data into usable blocks and then converted to string for further processing
def clean_text(user_input):
  user_input = str(user_input).lower().strip()

  # Process the text with spaCy
  doc = nlp(user_input)
  #  removing stop words and anything else thats not an alphabet
  cleaned_tokens = [token.text for token in doc if not token.is_stop and token.is_alpha]
  # Making the list of strings in cleaned_tokens one complete sentence again
  cleaned_text = ' '.join(cleaned_tokens) 
  #returning the results to be used for the code/display
  return cleaned_text

# Function for sentiment check and display the value with its allignment 
def rev_sentiment(user_input):
    #Determining the Polarity 
    doc = nlp(user_input)
    polarity = doc._.blob.polarity
    print(f"\nPolarity of this review is {polarity}")
        
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    print(f"The Sentiment for the customer's review is {sentiment}")

# Comparing the similarity between two samples 
def rev_compare(text1, text2): 
    sen1 = nlp(text1)
    sen2 = nlp(text2)
    similarity = sen1.similarity(sen2)
    print(f"Similarity value: {similarity}")
    

    
 
# Printing a sample review
print(f"\nSample data to work on:\n{my_text}")
# Executing the function of output for text cleaning process
clean_text(my_text)
# Executing the function of output for sentiment
rev_sentiment(my_text)

# Create new column with preprocessed comments and adding it to the existing dataframe
clean_data['comments.text'] = clean_data['reviews.text'].apply(clean_text)
# Printing the first5 lines of data for comparison
print(f"\nFirst five lines of review dataset processed:\n{clean_data.head()}")

# Sentiment value of a sample from the dataframe
print(f"\nSample data to work on:\n{clean_data['reviews.text'][2]}")
rev_sentiment(clean_data['reviews.text'][2])

print("\n\nComparison of 2 reviews")
review1 = clean_data['reviews.text'][0]
review2 = clean_data['reviews.text'][1]

# Executing the function of output for comparing the similarity for review 1 and 2
rev_compare(review1,review2)