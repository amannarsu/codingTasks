# Sentiment analysis report
Libraries used: 
- **Spacy** for NLP processing
- **Pandas** for data manipulation
- **SpacyTextBlob** for sentiment analysis

## A description of the dataset used.
The data set I have used for this project is the ‘amazon_product_reviews’ from Kaggle:
https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products
This data contains a list of aver 32,000 consumer reviews for Amazon products provided by Datafiniti's Product Database. This dataset is just a sample of the original dataset

## Details of the preprocessing steps.
The data from this dataset was processed by removing the null values from the ‘review.text’ column which was used for this task. We also used a sample text to test the functions created for the preprocessing.
![image](https://github.com/amannarsu/codingTasks/assets/30980894/b4f109e0-4b96-46d4-bec5-fbea9f96ba78)

Once the null values were removed, I removed the stop words and anything else that’s not an alphabet and them converting that into string as saving it into another column for comparison and understanding if the code have done its done correctly.
![image](https://github.com/amannarsu/codingTasks/assets/30980894/199a4ae7-53b3-44a3-9199-91ad5f41bd77)

## Evaluation of results.
After processing we were able to see that the model is working well where its able to display the polarity of the customer review if it was Positive, Negative or neither of these. 
![image](https://github.com/amannarsu/codingTasks/assets/30980894/73998047-7ab5-4e61-beee-e9372a411f04)

Giving us a sense of understanding of users who are pleased or displease of the product.
We have also compared the values of 2 different comments from the data frame to get understand of the similarities of the customer’s review
![image](https://github.com/amannarsu/codingTasks/assets/30980894/bb74ecb0-d1b0-44f1-8892-bd9d008bc2af)

## Insights into the model's strengths and limitations.
I have done a very basic preprocessing of the data, and it will really benefit by usage of Regex to remove very specific signs, and punctuations/errors from the reviews and using lemmatisation to get the root form of the words. This will help if collating similar reviews and more complex data handling that could help in further processing the data for understanding trends, and customer requirements with respect to the current model of data.
Though I am sure it can be user similarly on other data sets as well to come to different conclusions.
