from flask import Flask, render_template, request, jsonify, session as flask_session
from flask import redirect, url_for
from sqlalchemy import create_engine, Column, Integer, String, Text, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os
from chat import chat_bot
from DB_to_csv import DB_to_csv
import atexit

# Flask 설정
app = Flask(__name__)
app.secret_key = 'secret_key'

# SQLite 데이터베이스 설정
engine = create_engine('sqlite:///db.sqlite3')
Base = declarative_base()

# 데이터베이스 테이블 정의
class UserResponse(Base):
    __tablename__ = 'responses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    dob = Column(Date)
    checklist_q1 = Column(String)
    checklist_q2 = Column(String)
    checklist_q3 = Column(String)
    checklist_q4 = Column(String)
    checklist_q5 = Column(String)
    checklist_q6 = Column(String)
    checklist_q7 = Column(String)
    checklist_q8 = Column(String)
    checklist_q9 = Column(String)
    checklist_q10 = Column(String)
    user_question1 = Column(Text)
    bot_response1 = Column(Text)
    user_question2 = Column(Text)
    bot_response2 = Column(Text)
    user_question3 = Column(Text)
    bot_response3 = Column(Text)
    user_question4 = Column(Text)
    bot_response4 = Column(Text)
    user_question5 = Column(Text)
    bot_response5 = Column(Text)
    # chatbot_history = Column(Text)

# 데이터베이스 테이블 생성
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
db_session = Session()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-checklist', methods=['POST'])
def submit_checklist():
    data = request.json
    name = data['name']
    dob = data['dob']
    checklist = data['checklist']

    dob = datetime.strptime(dob, '%Y-%m-%d').date()

    flask_session['name'] = name
    flask_session['dob'] = dob

    # '예' 응답 개수 계산
    yes_count = sum(1 for answer in checklist if answer)


    # 체크리스트 질문 목록
    questions = [
        "1. 집에서 보호받지 못한다는 기분을 느끼나요?",
        "2. 최근 일주일 이내에 심하게 우울해서 힘든 적이 있나요?",
        "3. 최근 일주일 이내에 자살이나 죽음에 대해 생각해본 적이 있나요?",
        "4. 내가 원하지 않는데 누군가가 내 몸을 만지거나 보여 달라고 한 적 있나요?",
        "5. 최근 일주일 이내에 배가 고픈데 집에 먹을 게 없어서 굶은 적이 있나요?",
        "6. 주위 어른들 중에 나를 때리거나 위협을 가하는(혹은 가했던) 사람이 있나요?",
        "7. 부모님에게 맞거나 욕을 들은 적이 있나요?",
        "8. 최근 일주일 이내에 어디 아픈 곳이 있는데 어른들이 병원에 데려가지 않은 적이 있나요?",
        "9. 집으로 가는게 두렵거나, 집 안에서 편안함을 느낄 수 없나요?",
        "10. 현재 나는 다른 어른의 도움이 필요한 상태인가요?"
    ]

    # 질문에 대한 응답 리스트
    checklist_summary = "\n".join([f"{questions[i]}: {'예' if result else '아니오'}" for i, result in enumerate(checklist)])
    flask_session['checklist_summary'] = checklist_summary
    


    # 데이터베이스에 저장
    response = UserResponse(
        name=name,
        dob=dob,
        checklist_q1='예' if checklist[0] else '아니오',
        checklist_q2='예' if checklist[1] else '아니오',
        checklist_q3='예' if checklist[2] else '아니오',
        checklist_q4='예' if checklist[3] else '아니오',
        checklist_q5='예' if checklist[4] else '아니오',
        checklist_q6='예' if checklist[5] else '아니오',
        checklist_q7='예' if checklist[6] else '아니오',
        checklist_q8='예' if checklist[7] else '아니오',
        checklist_q9='예' if checklist[8] else '아니오',
        checklist_q10='예' if checklist[9] else '아니오',
        # chatbot_history=chatbot_history,
        user_question1=None,
        bot_response1=None,
        user_question2=None,
        bot_response2=None,
        user_question3=None,
        bot_response3=None,
        user_question4=None,
        bot_response4=None,
        user_question5=None,
        bot_response5=None
    )
    db_session.add(response)
    db_session.commit()

    if yes_count >= 1:
        flask_session['conversation_count'] = 0  # 횟수 제한
        # 대화 기록 초기화
        flask_session['conversation_history'] = []
        return jsonify({'status': 'chatbot', 'message': '챗봇 상담 시작'})
    else:
        return jsonify({'status': 'end', 'message': '과정 종료', 'redirect_url': url_for('finish')})

# 대화를 처리하는 새로운 라우트 추가
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        data = request.json
        user_input = data.get('message')  # 사용자가 보낸 메시지

        # 대화 횟수 제한
        conversation_count = flask_session.get('conversation_count', 0)

        conversation_history = flask_session.get('conversation_history', [])

        # 대화 진행
        response = chat_bot(user_input, conversation_history)

        # 사용자 기록 불러와 질문과 답변 추가
        user_record = db_session.query(UserResponse).filter_by(name=flask_session.get('name')).first()

        if conversation_count == 0:
            user_record.user_question1 = user_input
            user_record.bot_response1 = response
        elif conversation_count == 1:
            user_record.user_question2 = user_input
            user_record.bot_response2 = response
        elif conversation_count == 2:
            user_record.user_question3 = user_input
            user_record.bot_response3 = response
        elif conversation_count == 3:
            user_record.user_question4 = user_input
            user_record.bot_response4 = response
        elif conversation_count == 4:
            user_record.user_question5 = user_input
            user_record.bot_response5 = response

        db_session.commit()

        # 대화 횟수 증가 후 세션에 저장
        flask_session['conversation_count'] = conversation_count + 1

        if conversation_count >= 5:
            return jsonify({'response': '대화가 종료되었습니다.', 'redirect_url': url_for('finish')})

        return jsonify({'response': response})
    else:
        # 체크리스트 요약 가져오기
        checklist_summary = flask_session.get('checklist_summary', '')
        conversation_history = flask_session.get('conversation_history', [])
        initial_message = f"다음은 사용자의 체크리스트 결과입니다:\n{checklist_summary}\n'예'라고 답한 문항들을 종합하여, 학대 아동 발굴을 위한 질문을 만들어 상담을 진행하세요. 단, '한 번에 질문은 하나씩'만 하세요."
        response = chat_bot(initial_message, conversation_history)
        conversation_history.append(f"상담 챗봇: {response}")
        flask_session['conversation_history'] = conversation_history
        return render_template('chat.html', initial_message=response)

@app.route('/finish')
def finish():
    return render_template('finish.html')

@atexit.register
def on_shutdown():
    DB_to_csv()

if __name__ == '__main__':
    app.run(debug=True)