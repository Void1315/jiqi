from clear_img import ReadImage
import os
from PIL import Image, ImageFilter
from svmutil import *
class SetImage():
	"""docstring for SetImage"""
	def setImage(self):

		for root,dirs,files in os.walk("img/"):
			for the_name in files:
				img_ = Image.open("img/"+the_name)
				the_imgObj = ReadImage(img_)
				img_ = the_imgObj.no_novce(img_)
				print('成功')
				img_.save("img/"+the_name)

if __name__ == '__main__':
	y, x = [1,-1], [{1:1, 2:1}, {1:-1,2:-1}]
	prob  = svm_problem(y, x)
	param = svm_parameter('-t 0 -c 4 -b 1')
	model = svm_train(prob, param)
	yt = [1]
	xt = [{1:1, 2:1}]
	p_label, p_acc, p_val = svm_predict(yt, xt, model)
	print(p_label)