from qr_barcode import Code
from database import Database
import matplotlib.pyplot as plt
import os
import cv2


code = Code()


# with open('textfile.txt') as f:
#     words, numbers = f.read().splitlines()
#     for word, number in zip(words.split(','), numbers.split(',')):
#         code.generateQr(word, ('./codes/' + word))
#         print(number)
#         # code.generateQr(number, ('./codes/' + number))
#         code.generateBar(number, ('./codes/' + number))
#
# path = './codes/'
# codespath = os.listdir(path)
# fig = plt.figure(figsize=(15, 9))
# for i, imgpath in enumerate(codespath):
#     filename = os.path.join(path, imgpath)
#     image = cv2.imread(filename)
#     fig.add_subplot(4, 3, i+1)
#     plt.imshow(image)
#     plt.axis(False)
# plt.show()

# image = cv2.imread('Figure_1.png')
# datalist, image = code.decode(image)
# cv2.imshow('Decoded', image)
# cv2.waitKey(0)
# print(datalist)

# image = cv2.imread('./codes/123456789101.png')
# datalist, image = code.decode(image)
# cv2.imshow('Decoded', image)
# cv2.waitKey(0)
# print(datalist)



# cap = cv2.VideoCapture(0)
# cap.set(3, 1280)
# cap.set(4, 1024)
#
# while True:
#     ret, frame = cap.read()
#     image, dataList, polyList, rectList = code.decode(frame, draw=False)
#     cv2.imshow('Webcam', image)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

# query = """
#              select * from products;
#             """
# columns = ['S/N', 'product', 'serial code','mnfg_data',
#            'exp_date', 'price', 'used']
# db = Database('127.0.0.1', 'root', '10041225')
# data = db.readQuery(query, 'projects')
# print(data)
# df = db.t0DataFrame(data, columns)
# print(df)
