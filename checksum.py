import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button

def cal(num1, num2):
    tmp1 = int(num1, 2)
    tmp2 = int(num2, 2)
    norm = int('10000000000000000', 2)
    ret = tmp1 + tmp2
    if ret >= norm:
        ret = ret - norm + 1
    tmp = bin(ret)[2:]
    if len(tmp) != 16:
        tmp = '0' + tmp
    return tmp

def flip(num):
    var = ''
    for i in num:
        if i == '1':
            var = var + '0'
        if i == '0':
            var = var + '1'
    return var

textbox1 = TextBox(plt.axes([0.3, 0.8, 0.5, 0.075]), 'number1',initial='0110011001100000')
textbox2 = TextBox(plt.axes([0.3, 0.7, 0.5, 0.075]), 'number2',initial='0101010101010101')
textbox3 = TextBox(plt.axes([0.3, 0.6, 0.5, 0.075]), 'number3',initial='1000111100001100')
button = Button(plt.axes([0.3, 0.5, 0.5, 0.075]), "submit")

def button_clicked(event):
    textbox4 = TextBox(plt.axes([0.3, 0.4, 0.5, 0.075]), 'sum',
                       initial=cal(cal(textbox1.text, textbox2.text), textbox3.text))
    textbox5 = TextBox(plt.axes([0.3, 0.3, 0.5, 0.075]), 'result',
                       initial=flip(cal(cal(textbox1.text, textbox2.text), textbox3.text)))
    textbox6 = TextBox(plt.axes([0.3, 0.2, 0.5, 0.075]), 'check',
                       initial=cal(textbox1.text,cal(textbox2.text,cal(textbox3.text,textbox5.text))))
    plt.show()


button.on_clicked(button_clicked)
plt.show()
