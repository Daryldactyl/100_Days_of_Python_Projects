import requests

#Getting questions from API
response = requests.get(url='https://opentdb.com/api.php?amount=10&type=boolean')
response.raise_for_status()
data = response.json()
question_data = data["results"]
# question_data = []
# answer_data = []
# print(data)

# for i in range(10):
#     question_data.append(data['results'][i]['question'])
#     answer_data.append(data['results'][i]['correct_answer'])