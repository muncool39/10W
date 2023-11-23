from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot')
def plot():
    # CSV 파일 로드
    file_path = 'cox-violent-parsed_filt_usable.csv'  # 파일 경로를 수정해야 합니다.
    df = pd.read_csv(file_path)

    # 성별과 재범 발생여부에 대한 교차표 생성
    contingency_table = pd.crosstab(df['sex'], df['is_recid'])

    # 시각화: 성별에 따른 재범 발생여부
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 6))
    plot = sns.countplot(x='sex', hue='is_recid', data=df)
    plt.title('성별에 따른 재범 발생여부')

    # 그래프를 이미지로 변환
    img = BytesIO()
    plot.figure.savefig(img)
    img.seek(0)
    img_data = base64.b64encode(img.getvalue()).decode()

    return f'<img src="data:image/png;base64,{img_data}">'

if __name__ == '__main__':
    app.run(debug=True)

