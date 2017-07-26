from PIL import Image, ImageFilter
import time
import os
import pytesseract
from clear_img import ReadImage
class HongShui():
	"""docstring for """
	def left_zone(self,img, x, y):
	    sum_ = img.getpixel((x + 1, y)) + \
	          img.getpixel((x + 1, y + 1)) + \
	          img.getpixel((x + 1, y - 1)) + \
	          img.getpixel((x, y + 1)) + \
	          img.getpixel((x, y - 1))
	    if sum_<5*255:
	        return True
	    else:
	        return False
	def right_zone(self,img, x, y):
		sum_ = img.getpixel((x - 1, y)) + \
			img.getpixel((x - 1, y + 1)) + \
			img.getpixel((x - 1, y - 1)) + \
			img.getpixel((x, y + 1)) + \
			img.getpixel((x, y - 1))
		if sum_<5*255:
			return True
		else:
			return False
	def up_zone(self,img, x, y):
		sum_ = img.getpixel((x - 1, y)) + \
		img.getpixel((x + 1, y)) + \
		img.getpixel((x - 1, y + 1)) + \
		img.getpixel((x, y + 1)) + \
		img.getpixel((x + 1, y + 1))
		if sum_<5*255:
			return True
		else:
			return False
	def down_zone(self,img, x, y):
	    sum_ = img.getpixel((x - 1, y)) + \
	          img.getpixel((x + 1, y)) + \
	          img.getpixel((x - 1, y - 1)) + \
	          img.getpixel((x, y - 1)) + \
	          img.getpixel((x + 1, y - 1))
	    if sum_<5*255:
	    	return True
	    else:
	    	return False
	def min_zone(self,img, x, y):
		if img.getpixel((x,y))==255:
			return False
		sum_ = img.getpixel((x - 1, y + 1)) + \
			img.getpixel((x - 1, y)) + \
			img.getpixel((x - 1, y - 1)) + \
			img.getpixel((x, y + 1)) + \
			img.getpixel((x, y - 1)) + \
			img.getpixel((x + 1, y + 1)) + \
			img.getpixel((x + 1, y)) + \
			img.getpixel((x + 1, y - 1))
		if sum_<8*255:
			return True
		else:
			return False
	def spilt_img(self,img,offset_x):
		list_x = []
		list_y = []
		i = 0
		s_b = False
		w,h = img.size
		for x in range(offset_x,w-1):
			for y in range(1,h-1):
				if self.min_zone(img,x,y):
					list_x.append(x)
					list_y.append(y)
					i = 0
					s_b = True
			if i>0 and s_b:
				return (min(list_x),min(list_y)+1,max(list_x),max(list_y))
			i = i+1
	# def getCode(self):

	def splitImg(self,img):
		offset_x = 1
		for i in range(4):#循环四次
			tuple_ = self.spilt_img(img,offset_x)#拆分出一个字符
			img_1 = img.crop(tuple_).resize((22,22))#小和值大小
			img_1.save('split_img/'+str(time.time())+'.png','PNG')
			try:
				offset_x = tuple_[2]+1
			except Exception as e:
				break
if __name__ == '__main__':
	the_obj = HongShui()
	for root,dirs,files in os.walk("img/"):
		for the_name in files:
			img_ = Image.open("img/"+the_name)
			offset_x = 1
			print("img/"+the_name)
			for i in range(4):
				tuple_ = the_obj.spilt_img(img_,offset_x)
				img_1 = img_.crop(tuple_).resize((22,22))
				img_1.save('split_img/'+str(time.time())+'.png','PNG')
				try:
					offset_x = tuple_[2]+1
				except Exception as e:
					break


# for i in range(65,91):
# 	os.mkdir('sucai/'+str(chr(i))) 










# for root,dirs,files in os.walk("img/"):
# 	for the_name in files:
# 		img_ = Image.open("img/"+the_name)
# 		the_imgObj = ReadImage(img_)
# 		img_ = the_imgObj.no_novce(img_)
# 		print('成功')
# 		img_.save("img/"+the_name)