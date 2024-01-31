from django.shortcuts import render
from django.http import HttpResponse
from roboflow import Roboflow
from PIL import Image
import os
import cv2
# Create your views here.

# def index(request):
#     return render(request, 'index.html')

def post(request):
	if request.method == "POST":		#如果是以POST方式才處理
		img = request.FILES.get('myvalue')
		img_1 = Image.open(img)
		img_1 = img_1.transpose(Image.ROTATE_270)
		img_1.save(os.path.join('./myapp/static/images', 'test.jpg'))
		rf = Roboflow(api_key="WBwLaRxuckwQFXwFCETu")
		project = rf.workspace().project("item_detection-fucyd")
		model = project.version("2").model

		# detection
		predictions_dict = model.predict('./myapp/static/images/test.jpg', confidence=40, overlap=30).json()
		# model.predict('./myapp/static/images/test.jpg', confidence=40, overlap=30).save("./myapp/static/images/prediction.jpg")
		
        # add class to results
		result = []
		for prediction in predictions_dict['predictions']:
			result.append(prediction['class'])
			print("Class:", result[-1])
        
        # no class
		if len(result) == 0:
			result = "No predictions"
   	
	else:
		result = "None"
	return render(request, "post.html", locals())




