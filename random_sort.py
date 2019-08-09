import tkinter
import random

window = tkinter.Tk()
window.title('随机筛选人员')
window.geometry('600x700')

def get_list():
    global namelist
    names = str(entry2.get())
    namelist = names.split('，')
def random_sort():
    global i
    global namelist
    if len(namelist)>0:
        order = random.randint(0,len(namelist)-1)
        text1.insert(float(float(i)+0.0),'第'+str(i)+'个人是：')
        text1.insert(float(float(i)+0.8),namelist[order]+'\n')
        namelist.pop(order)
        i =i+1
    else:
        text1.insert(float(float(i)+0.0),'没人了！\n')
def clear_up():
    global i
    text1.delete('1.0','end')
    i = 1
label1 = tkinter.Label(window,text = '随机筛选结果为：',font = ('微软雅黑',10))
label1.place(x = 200,y = 150,anchor = 'ne')
label2 = tkinter.Label(window,text = '请输入人员姓名：',font = ('微软雅黑',10))
label2.place(x = 200,y = 40,anchor = 'ne')
entry2 = tkinter.Entry(window,show = None,width = 40)
entry2.place(x = 200,y = 40,anchor = 'nw')

text1 = tkinter.Text(window,width = 30,height = 40)
text1.place(x = 200,y = 150,anchor = 'nw')

global i 
i = 1

button1 = tkinter.Button(window,text = '随机抽取',font = ('微软雅黑',10),relief = tkinter.SOLID,width = 10,height = 1,command = random_sort)
button1.place(x = 300,y = 100,anchor = 'center')
button2 = tkinter.Button(window,text = '清除筛选结果',font = ('微软雅黑',10),width = 10,height = 1,relief = tkinter.SOLID,command = clear_up)
button2.place(x = 400,y = 100,anchor = 'center')
button3 = tkinter.Button(window,text = '获取人员列表',font = ('微软雅黑',10),width = 10,height = 1,relief = tkinter.SOLID,command = get_list)
button3.place(x = 200,y = 100,anchor = 'center')
window.mainloop() 
