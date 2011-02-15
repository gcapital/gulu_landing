""" UserPhoto photospec """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: imagespecs.py 556 2011-01-21 02:28:25Z gage $"

from imagekit.specs import ImageSpec
from imagekit import processors	 

class Resize40x40(processors.Resize):
	width = 40
	height = 40
	crop = True

class Resize50x50(processors.Resize):
	width = 50
	height = 50
	crop = True

class Resize84x56(processors.Resize):
	width = 84
	height = 56
	crop = True

class Resize86x58(processors.Resize):
	width = 86
	height = 58
	crop = True

class Resize121x90(processors.Resize):
	width = 121
	height = 90
	crop = True

class Resize186x119(processors.Resize):
	width = 186
	height = 119
	crop = True

class Resize185x185(processors.Resize):
	width = 185
	height = 185
	crop = True

class Resize190x125(processors.Resize):
	width = 190
	height = 125
	crop = True

class Resize160x100(processors.Resize):
	width = 160
	height = 100
	crop = True
	
class Resize284x157(processors.Resize):
	width = 284
	height = 157
	crop = True

class Resize240x140(processors.Resize):
	width = 240
	height = 140
	crop = True

class Resize600x400(processors.Resize):
	width = 600
	height = 400
	crop = True

class Resize622x417(processors.Resize):
	width = 622
	height = 417
	crop = True

class Resize630x285(processors.Resize):
	width = 630
	height = 285
	crop = True

class EnhanceSmall(processors.Adjustment):
	contrast = 1.2
	sharpness = 1.1
	
class AdminThumbnail(ImageSpec):
	access_as = 'admin_thumbnail'
	processors = [Resize50x50, EnhanceSmall]

class Image40x40(ImageSpec):
	processors = [Resize40x40, EnhanceSmall]
	pre_cache = True

class Image50x50(ImageSpec):
	processors = [Resize50x50, EnhanceSmall]
	pre_cache = True

class Image84x56(ImageSpec):
	processors = [Resize84x56, EnhanceSmall]
	pre_cache = True

class Image86x58(ImageSpec):
	processors = [Resize86x58, EnhanceSmall]
	pre_cache = True

class Image121x90(ImageSpec):
	processors = [Resize121x90, EnhanceSmall]
	pre_cache = True

class Image186x119(ImageSpec):
	processors = [Resize186x119]
	pre_cache = False

class Image185x185(ImageSpec):
	processors = [Resize185x185]
	pre_cache = False
	
class Image190x125(ImageSpec):
	processors = [Resize190x125]
	pre_cache = False
	
class Image160x100(ImageSpec):
	processors = [Resize160x100]
	pre_cache = False
	
class Image240x140(ImageSpec):
	processors = [Resize240x140]
	pre_cache = True
	
class Image284x157(ImageSpec):
	processors = [Resize284x157]
	pre_cache = True
		
class Image600x400(ImageSpec):
	processors = [Resize600x400]

class Image622x417(ImageSpec):
	processors = [Resize622x417]
	pre_cache = False
	
class Image630x285(ImageSpec):
	processors = [Resize630x285]
	pre_cache = True