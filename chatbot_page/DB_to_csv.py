import pandas as pd
from sqlalchemy import create_engine

def DB_to_csv():
    # DB 설정
    engine = create_engine('sqlite:///db.sqlite3')
    query = "SELECT * FROM responses"
    df = pd.read_sql(query, engine)

    # column
    df.columns = [
       'id', 'name', 'date', 'checklist_q1', 'checklist_q2', 'checklist_q3', 'checklist_q4',
        'checklist_q5', 'checklist_q6', 'checklist_q7', 'checklist_q8', 'checklist_q9', 'checklist_q10',
       'user_question1', 'bot_response1', 'user_question2', 'bot_response2', 'user_question3', 'bot_response3',
      'user_question4', 'bot_response4', 'user_question5', 'bot_response5'
    ]

    # CSV 파일로 생성
    df.to_csv('output.csv', index=False)
