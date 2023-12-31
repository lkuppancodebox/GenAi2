import json
import sys
import yaml
from palm_api import send_query_to_ai
#from google_bard import send_query_to_ai

def gen_prompt(topic, n) :

    prompt_input = '''
    {} Quiz for the topic "{}"\n 
    ### 4 options required along with a correct answer \n
    ### Required in YAML Format like below ###\n
    ---
    '1':
      question: ""
      options:
        a: ""
        b: ""
        c: ""
        d: ""
      answer: 
    '2':
    and so on.."" \n
    ### Only YAML format. No other text required
    ### do not include the char ```
    '''.format(n, topic)

    return prompt_input

def get_quiz_dict(topic, count):
    prompt_input = gen_prompt(topic, count)
    while True:
        resp = send_query_to_ai(prompt_input)

        if not resp:
            sys.exit()

        try:
            quiz_dict = yaml.safe_load(resp)
            return quiz_dict
            break
        except Exception as e:
            print("Retrying.. ")

if __name__ == '__main__':

    topic = input("Enter Topic: ")
    n = input("Number of questions: ")
    quiz_dict = get_quiz_dict(topic, n)

    if isinstance(quiz_dict, str):
        print(quiz_dict)
        sys.exit()

    print("----------------------------------------------------")
    print("\tOnline Quiz Started")
    print("----------------------------------------------------\n")

    score=0
    total_count=0

    for key, value in quiz_dict.items():
        total_count+=1
        print("\nquiz: {}".format(key))
        print(quiz_dict[key]["question"])

        for k, v in quiz_dict[key]["options"].items():
            print("{}: {}".format(k, v))

        ans = input("Enter Answer: (a/b/c/d): ")

        if quiz_dict[key]["answer"] == ans :
            print("[\u2713] CORRECT")
            score+=1
        else:
            print("[X] Wrong\n")
            print("Correct Answer is {}\n\n".format(quiz_dict[key]["answer"]))

    print("\n\n---------------------------")
    print("Your SCORE: {} %".format((score/total_count)*100))
    print("---------------------------")
