from clear_img import ReadImage
import os
from PIL import Image, ImageFilter
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
	the_obj = SetImage()
	the_obj.setImage()