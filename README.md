# Python-Fundamentals---Survey-Feedback-Analyzer-

Survey Feedback Analyzer – Python Fundamentals

Project Overview

The Survey Feedback Analyzer is a Python-based project designed to collect, clean, and analyze customer survey feedback.
The project uses a dictionary of lists to store customer names, written feedback, serial numbers, and ratings. It applies fundamental Python programming concepts to process textual feedback and extract meaningful insights.

Objectives

Store survey feedback using a dictionary of lists.
Collect additional feedback from users.
Perform basic text cleaning.
Identify frequently used words in feedback.
Calculate average customer ratings.
Find the feedback with the longest comment.
Extract unique words from all feedback entries.

Tools Used

Python

Python Concepts Used

Variables and Data Types
Dictionary and Lists
User Input (input())
For Loops
Conditional Statements
User-Defined Functions
String Manipulation
String Methods (replace(), split(), join(), strip(), lower())
Built-in Functions (sum(), len(), max())
Lambda Functions
Sets
zip() and sorted()

Project Implementation

1. Preloaded Feedback Data
Created a dictionary named feedback_data containing 10 predefined customer feedback entries with their serial numbers, names, written comments, and ratings.

2. Adding More Feedbacks
Collected additional feedback entries from users.
Accepted customer names, written feedback, and ratings.
Automatically generated serial numbers starting from 11.
Appended new entries to the existing dictionary.

3. Text Cleaning

Performed text cleaning on all feedback entries by:
Removing punctuation marks such as periods, commas, exclamation marks, and question marks.
Removing unnecessary spaces.
Replacing multiple spaces with a single space.
Converting all feedback text into lowercase.

4. Word Count Insights

Created a user-defined function count_word_in_feedbacks(word) to identify how many feedback entries contain a particular word.
Analyzed the occurrence of:
Good
Poor
Excellent

5. Final Summary & Insights
Performed the following analysis:
Displayed the final cleaned feedback dictionary.
Calculated the average customer rating.
Identified the feedback with the longest comment based on word count.
Extracted unique words across all feedback entries using sets.

6. Optional Analysis
Sorted feedback entries by rating in descending order using zip() and sorted().
Key Learnings

Through this project, I gained practical experience in:
Working with Python dictionaries and lists.
Collecting and managing user input.
Applying loops and functions.
Cleaning and processing textual data.
Using built-in Python functions for analysis.
Extracting useful insights from unstructured text data.

Conclusion

This project helped me understand the fundamentals of Python programming and how they can be applied to real-world data processing and basic text analysis tasks.
It provided hands-on experience in managing survey data, cleaning textual information, and generating meaningful insights from customer feedback.

