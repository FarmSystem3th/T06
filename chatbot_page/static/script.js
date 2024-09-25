document.getElementById('user-form').addEventListener('submit', function(e) {
    e.preventDefault();
    document.getElementById('user-form').style.display = 'none';
    document.getElementById('checklist-form').style.display = 'block';

    // 체크리스트 질문
    const questions = [
        "1. 집에서 보호받지 못한다는 기분을 느끼나요?",
        "2. 최근 일주일 이내에 심하게 우울해서 힘든 적이 있나요?",
        "3. 최근 일주일 이내에 자살이나 죽음에 대해 생각해본 적이 있나요?",
        "4. 내가 원하지 않는데 누군가가 내 몸을 만지거나 보여 달라고 한 적 있나요?",
        "5. 최근 일주일 이내에 배가 고픈데 집에 먹을 게 없어서 굶은 적이 있나요?",
        "6. 주위 어른들 중에 나를 때리거나 위협을 가하는(혹은 가했던) 사람이 있나요?",
        "7. 부모님에게 맞거나 욕을 들은 적이 있나요?",
        "8. 어른들이 나를 어디에 가두고 못 나오게 한 적이 있나요?",
        "9. 최근 일주일 이내에 어디 아픈 곳이 있는데 어른들이 병원에 데려가지 않은 적이 있나요?",
        "10. 집으로 가는게 두렵거나, 집 안에서 편안함을 느낄 수 없나요?",
        "11. 현재 나는 다른 어른의 도움이 필요한 상태인가요?"
    ];

    const questionsDiv = document.getElementById('questions');
    questions.forEach((question, index) => {
        const questionDiv = document.createElement('div');
        questionDiv.classList.add('question');
        
        const p = document.createElement('p');
        p.textContent = question;
        questionDiv.appendChild(p);
        
        const yesLabel = document.createElement('label');
        yesLabel.innerHTML = `<input type="radio" name="q${index+1}" value="yes" required> 예`;
        questionDiv.appendChild(yesLabel);

        const noLabel = document.createElement('label');
        noLabel.innerHTML = `<input type="radio" name="q${index+1}" value="no" required> 아니오`;
        questionDiv.appendChild(noLabel);

        questionsDiv.appendChild(questionDiv);
    });
});

// 서버 전송
document.getElementById('checklist-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const checklistResponses = Array.from(document.querySelectorAll('input[type="radio"]:checked')).map(input => input.value === 'yes');
    
    fetch('/submit-checklist', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            name: document.getElementById('name').value,
            dob: document.getElementById('dob').value,
            checklist: checklistResponses
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'chatbot') {
            window.location.href = "/chat";
        }
        else if (data.status === 'end') {
            window.location.href = data.redirect_url;
        }
        else {
            alert('과정이 종료되었습니다.');
        }
    });
});