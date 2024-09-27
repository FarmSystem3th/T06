# T06 
**👐🏻 Farm System 3기 T06팀 레포지토리입니다.**
<br/>
[📘 팀 노션 바로가기](https://www.notion.so/470c785e8cf248a1b4c1b1b516cea14c?pvs=4)
<br/><br/>

## 📅 개발 기간
 - 2024-08-07 ~ 2024-09-27
<br/><br/>

## 👧🏻 프로젝트 주제: 온라인 설문조사(ai 챗봇활용)를 통한 아동학대 자가진단
### **1️⃣ 프로젝트 개요**
- 배경 : 코로나 시기에 학생들이 건강 상태를 자가진단 앱으로 보고했던 것처럼, 학생들은 정기적으로 ai챗봇을 통해 자신의 정신적·신체적 건강 상태와 가정 환경을 기록. 이후 ai가 학대 의심 여부를 판단해 신고의무자인 교사에게 (선별)학생들의 결과 전달.
- 목적 : 아동 학대 유형 중 과반수를 차지하는 **정서학대** 발굴에 초점을 맞춘 시스템의 필요성, 교실에서 직접 대면으로 이루어지던 기존 실태조사 방식의 변화로 편안한 분위기를 도출해내 솔직한 응답 기대 가능
<br/><br/>

### **2️⃣ 리서치**
- 오픈소스 (ai-hub) https://aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=71680
  만7~12세 아동·청소년 3,596건의 신체적, 정신적 문제와 상황을 포괄한 7문항 18항목 이상의 상담데이터 ---> **데이터셋 구축**
  ![image](https://github.com/user-attachments/assets/862c76be-7d26-4a66-b8ef-770cfe5b975e)

- 보건복지부 2022 아동학대 주요통계
  만 7~15세가 과반수를 차지 ---> **초중고 아동**을 대상으로 선정
  ![image](https://github.com/user-attachments/assets/c2f661db-0688-4638-bc3a-912adfecb120)

<br/><br/>

### **3️⃣ 핵심 기능** 
- 1차 공통질문(체크리스트)
 챗봇 상담의 첫 번째 단계에서는 모든 아동이 정신적, 신체적 건강 상태와 가정 불화에 대한 11개의 질문으로 구성된 체크리스트를 작성합니다. 예/아니오로 응답할 수 있으며, 이 1차 질문에서 예라고 답한 항목이 있을 경우에 2차의 추가 상담이 진행됩니다.

- ai 챗봇의 2차 심화 상담
 1차 질문에서 위험 신호가 발견된 아동들은 ai챗봇과의 대화형 심화 상담 화면으로 이어집니다. 챗봇은 1차 체크리스트 응답에서 나타난 문제에 대해 더 심층적으로 질문하며, 예를 들어 “부모님에게 맞을 때는 보통 어떤 상황이에요?”등의 구체적인 질문을 통해 상담 데이터를 축척합니다.
  
- ai 분석 및 보고
  2차 챗봇 상담이 종료되면 ai는 챗봇을 통해 이뤄진 질의응답 내용을 분석하여 예측 모델에 학습시킵니다. 이 상담데이터를 기반으로 학대 의심 여부를 예측하고, 신고 의무자인 담당 교사에게 예측 결과를 전달하거나 하여 적절한 조치를 취할 수 있도록 돕습니다.


[ 예시 구현 화면 ]
https://github.com/user-attachments/assets/171a97f2-5376-4e2a-bd61-7bee708aeb12


<br/><br/>

### **4️⃣ 개발 환경**
#### AI
![python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)&nbsp; ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) &nbsp;<br>
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) &nbsp; ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) &nbsp; ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)&nbsp;<br>
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)&nbsp; ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)&nbsp; ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white) &nbsp; ![amazon](https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white) 

#### Etc.
![figma](https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white) &nbsp; ![notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white) ![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)
<br>
