from PIL import Image, ImageFilter
import pytesseract


class ReadImage(object):

	threshold = 195
	def __init__(self, img):
		self.img = img

	def get_bin_table(self,):
	    
	    table  =  []
	    for  i  in  range( 256 ):
	        if  i  <  self.threshold:
	            table.append(0)
	        else:
	            table.append(255)
	    return table

	def left_zone(self,img, x, y):
	    sum = img.getpixel((x + 1, y)) + \
	          img.getpixel((x + 1, y + 1)) + \
	          img.getpixel((x + 1, y - 1)) + \
	          img.getpixel((x, y + 1)) + \
	          img.getpixel((x, y - 1))
	    if sum >= 1020:
	        return 255
	    else:
	        return 0


	def right_zone(self,img, x, y):
	    sum = img.getpixel((x - 1, y)) + \
	          img.getpixel((x - 1, y + 1)) + \
	          img.getpixel((x - 1, y - 1)) + \
	          img.getpixel((x, y + 1)) + \
	          img.getpixel((x, y - 1))
	    if sum >= 1020:
	        return 255
	    else:
	        return 0


	def up_zone(self,img, x, y):
	    sum = img.getpixel((x - 1, y)) + \
	          img.getpixel((x + 1, y)) + \
	          img.getpixel((x - 1, y + 1)) + \
	          img.getpixel((x, y + 1)) + \
	          img.getpixel((x + 1, y + 1))
	    if sum >= 1020:
	        return 255
	    else:
	        return 0

	def down_zone(self,img, x, y):
	    sum = img.getpixel((x - 1, y)) + \
	          img.getpixel((x + 1, y)) + \
	          img.getpixel((x - 1, y - 1)) + \
	          img.getpixel((x, y - 1)) + \
	          img.getpixel((x + 1, y - 1))
	    if sum >= 1020:
	        return 255
	    else:
	        return 0


	def min_zone(self,img, x, y):
	    sum = img.getpixel((x - 1, y + 1)) + \
	          img.getpixel((x - 1, y)) + \
	          img.getpixel((x - 1, y - 1)) + \
	          img.getpixel((x, y + 1)) + \
	          img.getpixel((x, y - 1)) + \
	          img.getpixel((x + 1, y + 1)) + \
	          img.getpixel((x + 1, y)) + \
	          img.getpixel((x + 1, y - 1))
	    if sum >= (255 * 6):
	        return 255
	    else:
	        return 0

	def remove_noise(self,img, x, y):
	    cur_pixel = img.getpixel((x, y))
	    width = img.width
	    height = img.height
	    if cur_pixel == 255:
	        return 255
	    else:
	        if x == 0:
	            if y == 0 or y == height:
	                return 255
	            else:
	                return self.left_zone(img, x, y)
	        if x == width:
	            if y == 0 or y == height:
	                return 255
	            else:
	                return self.right_zone(img, x, y)
	        if y == 0:
	            if x == 0 or x == width:
	                return 255
	            else:
	                return self.up_zone(img, x, y)
	        if y == height:
	            if x == 0 or x == width:
	                return 255
	            else:
	                return self.down_zone(img, x, y)

	        return self.min_zone(img, x, y)


	def list_set_img(self,list_img, img_):
	    w, h = img_.size
	    i = 0
	    for x in range(w):
	        for y in range(h):
	            if list_img[i] == None:
	                list_img[i] = 0
	            img_.putpixel((x, y), list_img[i])
	            i = i + 1
	    return img_


	def clear_img(self,img):
	    w,h = img.size
	    list_img = []
	    for x in range(w):
	        for y in range(h):
	            list_img.append(self.remove_noise(img, x, y))
	    return list_img

	def read_img(self,img_):
	    code = pytesseract.image_to_string(img_)
	    return code

	def to_black(self,img):
	    img = img.convert('L')
	    table = self.get_bin_table()
	    img_ = img.point(table, '1')
	    return img_

	def return_code(self):
	    list_img = []
	    img = self.img
	    img = self.to_black(img)
	    list_img = self.clear_img(img)
	    return self.read_img(self.list_set_img(list_img,img))

	def get_code(self):
		return self.return_code()

	def no_novce(self,img):
	    list_img = []
	    img = self.img
	    img = self.to_black(img)
	    list_img = self.clear_img(img)
	    img = self.list_set_img(list_img,img)
	    return img
	def split_img(self):
		w,h = self.img.size
		print(w,h)
		list_x = []
		list_y = []
		list_1 = []
		list_2 = []
		list_ = []
		setoff = 0
		i = 0
		for x in range(w):
			list_lineY = []
			for y in range(h):
				if self.img.getpixel((x,y)) == 0:
					list_lineY.append(y)
					i = 0
			if(i>3):
				list_1.append(list_y)
				list_y =[]
				i = 0
			if len(list_lineY)>0:
				if min(list_lineY)==max(list_lineY):
					list_y.append(min(list_lineY))

				else:
					list_y.append(min(list_lineY))
					list_y.append(max(list_lineY)+1)
			i = i+1
		i = 0
		for i in list_1:
			if i:
				# print("Ymax:",max(i))
				# print("Ymin:",min(i))
				tuple_= self.split_w(setoff,list_,min(i),max(i))
				setoff = tuple_[0]
				list_2.append(tuple_[1])
				list_ = []
		# for i in list_1:
		# 	if i:
		# 		print("Ymax:",max(i))
		# 		print("Ymin:",min(i))
		for i in list_2:
			if i:
				print("Xmax:",max(i))
				print("Xmin:",min(i))

	def split_w(self,setoff,list_2,s_h,e_h):
		i = 0
		list_x = []
		tht_bool = False
		w,h = self.img.size
		for y in range(s_h,e_h):
			list_lineX = []
			for x in range(setoff,w):
				# print(x)
				if i>4:
					tht_bool = False
					i = 0
					if(len(list_lineX)>0):
						list_x.append(min(list_lineX))
						list_x.append(max(list_lineX)+1)
						list_lineX = []
					break#该换行了
				if self.img.getpixel((x,y)) == 0:
					list_lineX.append(x)
					i = 0
					tht_bool = True
				elif tht_bool:
					i =i+1
				print(list_lineX)
			list_2.extend(list_x)
		if len(list_2)>0:
			return [max(list_2),list_2]


if __name__ == '__main__':
	img_ = Image.open('img/1500901237.339602.png')
	the_img = ReadImage(img_)
	the_img.split_img()