wget https://raw.githubusercontent.com/yasheshshroff/NLPworkshop/main/labs/07a_disaster_detection_tfidf.py -O diaster_detection_tfidf.py
wget https://raw.githubusercontent.com/yasheshshroff/NLPworkshop/main/labs/07a_predict_disaster_tfidf.py -O predict_disaster_tfidf.py
wget https://github.com/yasheshshroff/NLPworkshop/raw/main/labs/dataset/disaster_data.zip
pip install rich
unzip disaster_data.zip
conda activate pytorch_p36
pip install -r airflow_requirements.txt
