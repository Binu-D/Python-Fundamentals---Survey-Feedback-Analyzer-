feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj','Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
'Feedback': ['   Very GOOD Service!!!','poor support,not happy   ','GREAT experience! will come again.','okay     okay...','   not    BAD','Excellent care, excellent staff!','good food and good ambience!','Poor response and poor handling of issue',
'Satisfied. But could be better.','Good support... quick service.'],
'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]}

print(feedback_data)


n = int(input("How many more feedbacks do you want to add? "))

for i in range(n):
    print("\nEnter Feedback Details")

    name = input("Enter Name: ")
    feedback = input("Enter Feedback: ")
    rating = int(input("Enter Rating (1-5): "))

    s_no = len(feedback_data['S_No']) + 1

    feedback_data['S_No'].append(s_no)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)

print("\nUpdated Feedback Data:")
print(feedback_data)


for i in range(len(feedback_data['Feedback'])):

    text = feedback_data['Feedback'][i]

    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace('!', '')
    text = text.replace('?', '')

    text = ' '.join(text.split())

    text = text.strip()

    text = text.lower()

    feedback_data['Feedback'][i] = text

print("Cleaned Feedback Data:")
print(feedback_data['Feedback'])




def count_word_in_feedbacks(word):

    count = 0

    for feedback in feedback_data['Feedback']:

        if word.lower() in feedback.lower().split():
            count += 1

    return count


print("Word Count Insights")

print("Feedbacks containing 'good':",
      count_word_in_feedbacks('good'))

print("Feedbacks containing 'poor':",
      count_word_in_feedbacks('poor'))

print("Feedbacks containing 'excellent':",
      count_word_in_feedbacks('excellent'))




print("FINAL CLEANED FEEDBACK DATA")

print(feedback_data)

