import cv2
import numpy as np
from pyzbar.pyzbar import decode
from barcode import EAN13
from barcode.writer import ImageWriter
import qrcode


class Code:

    def __init__(self, box_size=10, border=4):

        self.qr = qrcode.QRCode(box_size=10, border=4)
        # self.QrDecoder = cv2.QRCodeDetector()

    @staticmethod
    def generateBar(data, filename='code'):
        barcode = EAN13(data, writer=ImageWriter())
        barcode.save(filename)

    def generateQr(self, data, name='code', file_type='jpg', fit=True):
        filename = ''.join([name, '.', file_type])
        self.qr.add_data(data)
        self.qr.make(fit=fit)
        image = self.qr.make_image()
        image.save(filename)
        self.qr.clear()

    @staticmethod
    def decode(image, draw=True, polyColor= (0, 255, 0)):
        dataList = []
        polyList = []
        rectList = []
        try:
            for code in decode(image):
                data = code.data.decode('utf-8')
                polyPoints = np.array([code.polygon], np.int32)
                polyPoints = polyPoints.reshape(-1, 1, 2)
                polyList.append(polyPoints)
                rectPoints = code.rect
                rectList.append(rectPoints)

                if draw:
                    cv2.polylines(image, polyPoints, True, polyColor, 1, )
                    cv2.putText(image, data, (rectPoints[0], rectPoints[1]), cv2.FONT_HERSHEY_PLAIN,
                                1, polyColor, 2)
                dataList.append(data)
            return image, dataList,  polyList, rectList

        except Exception as e:
            print('Could not detect code', e)




