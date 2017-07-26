from PIL import Image, ImageFilter
from svmutil import *
from svm import *
import os
class SVMImage():
	"""docstring for SVMImage
		特征化图片+机器学习+机器识别
	"""
	file_model = "data_svm/model.txt"
	file_test = "data_svm/test.txt"
	def __init__(self,img):
		self.img = img
		self.list_date = self.set_feature()
		self.svmDate = self.getSvmDate()

	def set_feature(self):#特征化
		h,w = self.img.size
		pix_cnt_x = 0
		pix_cnt_y = 0
		pixel_cnt_list = []
		for x in range(w):
			for y in range(h):
				if self.img.getpixel((x, y)) == 0:  # 黑色点
					pix_cnt_x += 1
			pixel_cnt_list.append(pix_cnt_x)
		for y in range(h):
			for x in range(w):
				if self.img.getpixel((x, y)) == 0:
					pix_cnt_y += 1
			pixel_cnt_list.append(pix_cnt_y)
		return pixel_cnt_list


	def getStrDate(self,label=0):
		list_date = self.list_date
		list_date = {index+1:i for index,i in enumerate(list_date)}
		str_date = str(label)+" "+str(svm_date)[1:-1].replace(" ",'').replace(","," ")+"\n"
		return str_date
	def getSvmDate(self):
		list_date = self.list_date
		svmDate = {index+1:i for index,i in enumerate(list_date)}
		return svmDate
		

	def svmDateSave(self,str_date):
		file_p = open(self.file_model,'a')
		file_p.writelines(str_date)
		file_p.close()

	def getSvmCode(self):
		pass


	def testDate(self):
		test_date = [self.svmDate]
		label = [5]
		y,x = svm_read_problem(the_obj.file_model)
		param = svm_parameter('-t 1 -b 1 -q')
		model = svm_problem(y, x)
		model = svm_train(model,param)
		print('test:')
		# print((label))
		p_label, p_acc, p_val = svm_predict(label,test_date,model)
		print(p_label, p_acc)



if __name__ == '__main__':
	
	img = Image.open("split_img/1500967740.6504016.png")
	# img = Image.open("sucai/9/1500953797.8504016.png")
	the_obj = SVMImage(img)
	the_obj.testDate()


	# sucai_ = '9'
	# for root,dirs,files in os.walk("sucai/"+sucai_+'/'):
	# 	for the_name in files:
	# 		img = Image.open('sucai/'+sucai_+'/'+the_name)
	# 		the_obj = SVMImage(img)
	# 		str_date = the_obj.getStrDate()
	# 		the_obj.svmDateSave(str_date)










			# y,x = svm_read_problem(the_obj.file_model)
			# yt,xt = svm_read_problem(the_obj.file_test)
			# model = svm_train(y,x)
			# print('test:')
			# p_label, p_acc, p_val = svm_predict(yt, xt, model)
			# print(p_label)


	# y, x = [1,-1], [{1:1,2:1}, {1:-1,2:-1}]
	# prob  = svm_problem(y, x)
	# model = svm_train(prob)
	# yt = [1]
	# xt = [{1:1, 2:1}]
	# p_label, p_acc, p_val = svm_predict(yt, xt, model)
	# print(p_acc)