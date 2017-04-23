import qrcode
from watson_developer_cloud import visual_recognition_v3 as CV
from random import randint
filename = "image.jpeg"
image = open(filename,"rb")

VR = CV.VisualRecognitionV3(version='2016-05-20', api_key='b6e68f456571c465e1f9cef14e3b1f7244147f32' )
response = VR.classify(images_file=image)

item = response["images"][0]["classifiers"][0]["classes"][0]["class"]
recyclables = {"bottled water": True, "can" : True} # add more recycables here
is_recyclable = recyclables.get(item) or False
json = {"recyle": is_recyclable, "item" : item, "points": int(is_recyclable) and randint(1,5)}


img = qrcode.make(repr(json))
img.save("qr.png")
