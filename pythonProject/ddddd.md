fit_transform(): 데이터를 학습하고 동시에 변환(훈련 데이터에 사용)

transform(): 이미 학습된 정보를 사용하여 데이터를 변환(테스트 데이터, 새로운 데이터에 사용)

pd.DataFrame()	데이터를 테이블 형태로 변환

train_test_split()	데이터를 훈련용/테스트용으로 나눔

CountVectorizer()	텍스트 데이터를 숫자 벡터로 변환

MultinomialNB()	Naive Bayes 분류기 초기화

fit()	모델을 훈련 데이터로 학습

predict()	새로운 데이터에 대해 예측

accuracy_score()	모델의 정확도를 계산