wget https://raw.githubusercontent.com/yasheshshroff/NLPworkshop/main/labs/07a_disaster_detection_tfidf.py -O diaster_detection_tfidf.py
wget https://raw.githubusercontent.com/yasheshshroff/NLPworkshop/main/labs/07a_predict_disaster_tfidf.py -O predict_disaster_tfidf.py
wget https://github.com/yasheshshroff/NLPworkshop/raw/main/labs/dataset/disaster_data.zip
unzip disaster_data.zip
head -10 disaster_data/train.csv > disaster_data/predict.csv