import requests
import json

# عنوان API المحلي
url = "http://127.0.0.1:5000/predict"

# قراءة بيانات الاختبار من JSON
with open("test_request.json", "r") as f:
    data = json.load(f)

# إرسال الطلب إلى API
response = requests.post(url, json=data)

# طباعة النتيجة
print("Response:", response.json())
