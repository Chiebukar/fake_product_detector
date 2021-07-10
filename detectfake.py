import cv2
from qr_barcode import Code
from database import Database
from datetime import date


def dfFromDb():
    query = """
             select * from products;
            """
    columns = ['S/N', 'product', 'serial code','mnfg_data',
               'exp_date', 'price', 'validity']
    db = Database('127.0.0.1', 'root', '10041225')
    data = db.readQuery(query, 'projects')
    df = db.t0DataFrame(data, columns)
    return df


def checkGenuine(qrData, df, column):
    df_column = df[column]
    genuine = list(df_column.values)
    if qrData in genuine:
        return True
    return False


def getExpDate(qrData, df, column):
        expDate = df[df[column]==qrData]['exp_date'].values[0]
        return expDate


def checkExpiration(qrData, df, column):
    expDate = getExpDate(qrData, df, column)
    today = date.today()
    if expDate < today:
        return 'Not Expired'
    else:
        return 'Expired'


def detect(df, column, image, dataList, polyList, rectList):
    red = (0, 0, 255)
    green = (0, 255, 0)

    for qrData, polyPoints, rectPoints in zip(dataList, polyList, rectList):
        x, y, width, height = rectPoints
        genuine = checkGenuine(qrData, df, column)
        if genuine:
            product = df[df[column] == qrData]['product'].values[0]
            expiration = checkExpiration(qrData, df, column)
            validity = df[df[column] == qrData]['validity'].values[0]

            space = 20
            cv2.polylines(image, polyPoints, True, green, 1)
            cv2.putText(image, 'Authentic', (x-10, y-5),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, green, 2)
            for info, text in zip(['Product', 'Expiration', 'Validity'],
                                  [product, expiration, validity]):
                if text in ['Code Used', 'Expired']:
                    color = red
                else:
                    color = green
                cv2.putText(image, info + ': ' + text,
                            (x+width, y+space),
                            cv2.FONT_HERSHEY_COMPLEX,
                            0.5, color, 2)
                space += 20
        else:
            cv2.putText(image, 'Fake', (x, y-5),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, red, 2)
        cv2.putText(image, qrData, (x-10, y+height+15),
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)
    return image



def main():
    df = dfFromDb()
    code = Code()
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 1024)

    while True:
        ret, frame = cap.read()
        image, dataList,  polyList, rectList = code.decode(frame, draw=False)
        detect(df, 'serial code', image, dataList, polyList, rectList)
        cv2.imshow('Webcam', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# # testing with images
# df = dfFromDb()
# code = Code
# image = cv2.imread('sample_qr2.png')
# image, dataList,  polyList, rectList = code.decode(image, draw=False)
# cv2.imshow('image', image)
# cv2.waitKey(0)
# image = detect(df, 'serial code', image, dataList, polyList, rectList)
# cv2.imshow('image', image)
# cv2.waitKey(0)

main()