import requests
import time
from PIL import Image, ImageFilter
import os
from clear_img import ReadImage
from hongshui import HongShui
class SaveImage():
	"""docstring for SaveImage"""
	img_url = "http://59.69.173.117/jwweb/sys/ValidateCode.aspx"
	the_session = None#保持会话s
	def save_img(self):
		results = requests.get(self.img_url)
		if(results.status_code == 200):
			open("img/"+self.rand_name(), 'wb').write(results.content)
	def rand_name(self):
		return str(time.time())+'.png'


the_obj = SaveImage()
# for i in range(100):
# 	the_obj.save_img()
# 	print('第'+str(i+1)+"张")
for root,dirs,files in os.walk("img/"):
	for the_name in files:
		img_ = Image.open("img/"+the_name)
		the_imgObj = ReadImage(img_)
		img_ = the_imgObj.no_novce(img_)
		print('成功')
		img_.save("img/"+the_name,"PNG")
		hongshui_obj = HongShui()
		hongshui_obj.splitImg(img_)