import numpy as np 
import cv2
import openpyxl


wb_name = ''
res = input('是否创建一个新的签到表：(yes/no)')
if 'yes' == res.lower():
    wb = openpyxl.Workbook()
    ws = wb.active
    num = 0
else:
    wb_name = input('请输入已有的excel文件名：')
    wb = openpyxl.load_workbook(wb_name + '.xlsx')
    ws = wb.active
    num = 1

face_cascade = cv2.CascadeClassifier('/home/xzt/OpenCV-Python-Series/src/cascades/data/haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)


value_list = []

ID = input("Enter your name:")
for cells in ws['A']:
    value_list.append(cells.value)
    num = num + 1
if ID not in value_list:
    cell = ws.cell(row=num, column=1, value=ID)

while(ID):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        img_item = ID + ".png"
        cv2.imwrite('./images/' + img_item, roi_gray) 
        print('get!')
       
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
if not wb_name:
    wb_name = input('请输入表格名称:')
wb.save('./workbooks/' + wb_name + '.xlsx')
print('Finish!!!')