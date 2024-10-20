# 1. Product Review Analysis
#### Task 1: Keyword Highlighter ####

# Write a program that searches through reviews list and looks for keywords such as "good", 
# "excellent", "bad", "poor", and "average". We want you to capitalize those keywords then print out each review. 
# Print out each review with the keywords in uppercase so they stand out.


#    reviews = [
#        "This product is really good. I'm impressed with its quality.",
#        "The performance of this product is excellent. Highly recommended!",
#        "I had a bad experience with this product. It didn't meet my expectations.",
#        "Poor quality product. Wouldn't recommend it to anyone.",
#        "The product was average. Nothing extraordinary about it."
#    ]
#So for the first string in the reviews list, we want it to say: 
"This product is really GOOD. I'm impressed with its quality."

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
keywords = ["excellent", "good", "average", "poor", "Poor", "bad"] 

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] ####TASK 2####

negative_words = ["bad", "poor", "Poor", "terrible", "horrible", "awful", "disappointing", "subpar"] ####TASK 2####

def generate_summary(text, max_length=30):####TASK 3####
    
    if len(text) <= max_length:
        return text
    
    truncated = text[:max_length].rstrip()
    if not truncated[-1].isalnum():
        return truncated + "..."

    last_space = truncated.rfind(" ")
    if last_space != -1:
        return truncated[:last_space] + "..."
    return truncated + "..." 
####Task 2####
def capitalize_keywords_and_tally(reviews, positive_words, negative_words):
    total_positive = 0
    total_negative = 0

    for review in reviews:
        positive_count = 0
        negative_count = 0

        for word in positive_words:
            occurrences = review.lower().count(word)
            positive_count += occurrences
            review = review.replace(word, word.upper())


        for word in negative_words:
            occurrences = review.lower().count(word)
            negative_count += occurrences
            review = review.replace(word, word.upper())
        
        summary = generate_summary(review) ###Task 3###
        print(f"Summary: {summary}") 
        print(review) ####TASK 1####
        print(f"Positive words: {positive_count}, Negative words: {negative_count}") ####TASK 2####

        total_positive += positive_count ####TASK 2####
        total_negative += negative_count ####TASK 2####
####Task 2
    print("\nOverall Tally:") ####TASK 2####
    print(f"Total positive words: {total_positive}") ####TASK 2####
    print(f"Total negative words: {total_negative}") ####TASK 2####

capitalize_keywords_and_tally(reviews, positive_words, negative_words)####TASK 1 and 2####


#### Task 2:# Sentiment Tally ####
#####¡¡¡¡¡¡ THIS WILL BE ADDED TO TASK 1 CODE ¡¡¡¡¡¡¡#####
# Develop a function that tallies the number of positive and negative words in each review.  
# The function should return the total count of positive and negative words.
#    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
#    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

#positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
#negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

#### Task 3: Review Summary
#####¡¡¡¡¡¡ THIS WILL BE ADDED TO TASK 1 CODE ¡¡¡¡¡¡¡#####
# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
# Ensure that the summary does not cut off in the middle of a word.

# Example: "This product is really good. I'm...",

