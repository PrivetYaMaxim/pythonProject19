import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
# from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.app import runTouchApp
import webbrowser
# I set the color constants to then color the text on the buttons (this is optional)
red = (255 / 255, 67 / 255, 67 / 255)
green = (0 / 255, 158 / 255, 60 / 255)
from kivy.properties import StringProperty
from kivy.uix.carousel import Carousel

f=open('тест.txt','r')





KV = """
#:import webbrowser webbrowser


WindowManager:
	FirstWindow:
	SecondWindow:
	ThirdWindow:
	FourthWindow:
	Umsc:
	LOm:
<OpL1@MDLabel>:
    halign:'center'
    color:'black'
    font_size:16
    pos_hint: {"center_x": .5, "center_y": .46}
    color:'orange'
<OpL2@MDLabel>:
    color:'orange'
    halign:'center'
    font_size:16
	pos_hint: {"center_x": .5, "center_y": .64}
<OpL3@MDLabel>:
    color:'orange'
    halign:'center'
    font_size:16
	pos_hint: {"center_x": .5, "center_y": .280}
<OpS@MDRaisedButton>:
    text:'Перейти на сайт'
	font_size:32
	pos_hint: {"center_x": .5, "center_y": .1}
<Back@MDRaisedButton>:
    text: "  Назад  "
	pos_hint: {"center_x": .1, "center_y": .95}
	font_size: 32
<OP@MDScreen>:
    FitImage:
        source:'5.jpg'
    Back:
		on_release: 
			app.root.current = "second"
			root.manager.transition.direction = "right"

    

<FirstWindow>:
    name:"first"
    MDScreen:
        FitImage:
            source: '5.jpg'


        MDRaisedButton:
            text: "Подобрать курсы"
            font_size:36
            pos_hint: {"center_x": .5, "center_y": .6}
            on_release: 

				app.root.current = "second"
				root.manager.transition.direction = "left"

        MDRaisedButton:
            text: "Выйти"
            font_size:36
            pos_hint: {"center_x": .5, "center_y": .4}
            on_release: app.close_application()
<SecondWindow>:######################################################################################################################################################
	name: "second"
	MDScreen:
        FitImage:
            source: '5.jpg'
        MDFillRoundFlatButton:
            text: "  Курсы  "
            font_size:32
            custom_color: "black"
            line_color:'orange'
            text_color:'black'
            halign: "center"
            pos_hint:{'center_x':0.5,'center_y':0.85}
            disabled: False
            background_disabled_down:'orange'
		MDIconButton:
            icon: "1fox.png"
            icon_size: "50sp"
            pos_hint: {"center_x": .37, "center_y": .4}
            on_release:
				app.root.current = "fourth"
				root.manager.transition.direction = "left"
        MDRaisedButton:
            font_size:24
            text: "Фоксфорд"
            pos_hint: {"center_x": .5, "center_y": .4}
            on_release: 
				app.root.current = "fourth"
				root.manager.transition.direction = "left"
        MDIconButton:
            icon: "1.png"
            icon_size: "50sp"
            pos_hint: {"center_x": .37, "center_y": .6}
            on_release:
				app.root.current = "fifth"
				root.manager.transition.direction = "left"

        MDRaisedButton:
            font_size:24
            text: "  Умскул  "
            pos_hint: {"center_x": .5, "center_y": .6}
            on_release: 
				app.root.current = "fifth"
				root.manager.transition.direction = "left"
		MDIconButton:
            icon: "100.png"
            icon_size: "50sp"
            pos_hint: {"center_x": .37, "center_y": .5}
            on_release:
				app.root.current = "fifth"
				root.manager.transition.direction = "left"

        MDRaisedButton:
            font_size:24
            text: "   Сотка   "
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: 
				app.root.current = "third"
				root.manager.transition.direction = "left"
        MDRaisedButton:
            font_size:24
            text: " Skysmart "
            halign:'center'
            pos_hint: {"center_x": .5, "center_y": .7}
            on_release: 
				app.root.current = "six"
				root.manager.transition.direction = "left"
        MDIconButton:
            icon: "12.png"
            icon_size: "50sp"
            pos_hint: {"center_x": .37, "center_y": .7}
            on_release:
                app.root.current = "six"
                root.manager.transition.direction = "left"
	    Back:
			on_release: 
				app.root.current = "first"
				root.manager.transition.direction = "right"
###################################################################################################################################################################
<ThirdWindow>:
    name:"third"
    OP:
        Back:
			on_release: 
				app.root.current = "second"
				root.manager.transition.direction = "right"
        MDCard:
            size_hint: .98, .6
            focus_behavior: False
            pos_hint: {"center_x": .5, "center_y": .5}
            color: (56,56,56)
        
 
 
        MDFillRoundFlatButton:
            text: "  Описание:  "
            font_size:24
            custom_color: "black"
            line_color:'orange'
            text_color:'black'
            halign: "center"
            pos_hint:{'center_x':0.5,'center_y':0.73}
            disabled: False
            background_disabled_down:'orange'
        MDFillRoundFlatButton:
            text: "  Предметы:  "
            font_size:24
            custom_color: "black"
            line_color:'orange'
            text_color:'black'
            halign: "center"
            pos_hint:{'center_x':0.5,'center_y':0.55}
            disabled: False
            background_disabled_down:'orange'
        MDFillRoundFlatButton:
            text: "  Цена:  "
            font_size:24
            custom_color: "black"
            line_color:'orange'
            text_color:'black'
            halign: "center"
            pos_hint:{'center_x':0.5,'center_y':0.370}
            disabled: False
            background_disabled_down:'orange' 
        OpL2:
            text:"Сотка-это одна из лидирующих онлайн школ подготовки к ЕГЭ и ОГЭ,позволяющая подготовиться к экзаменам в интересном и увлекательном формате."
        OpL1:
            text:"Английский язык, биология,физика,химия,история, информатика,литература,математика,обществознание,русский язык"
        OpL3:
            text:"Обучение стоит от 3750р до 4030р в месяц в зависимости от выбрвнного тарифа. В эту цену включена полноценная подготовка по всем предметам,которые сдает ученик. Доплачивать не нужно.\\n Также Сотка предоставляет возможность оплатить обучение на 6 месяцев за 16045р. Кроме этого есть возможность оплатить обучение на весь учебный год за 30040р."
        OpS:
            on_release:
                webbrowser.get().open_new_tab("https://sotkaonline.ru/")

		    
<FourthWindow>:
    name:"fourth"
    OP:
        Back:
			on_release: 
				app.root.current = "second"
				root.manager.transition.direction = "right"
        MDCard:
            size_hint: .98, .6
            focus_behavior: False
            pos_hint: {"center_x": .5, "center_y": .5}
            color: (56,56,56)
        
 
 
        MDFillRoundFlatButton:
            text: "  Описание:  "
            font_size:24
            custom_color: "black"
            line_color:'orange'
            text_color:'black'
            halign: "center"
            pos_hint:{'center_x':0.5,'center_y':0.73}
            disabled: False
            background_disabled_down:'orange'
        MDFillRoundFlatButton:
            text: "  Предметы:  "
            font_size:24
            custom_color: "black"
            line_color:'orange'
            text_color:'black'
            halign: "center"
            pos_hint:{'center_x':0.5,'center_y':0.55}
            disabled: False
            background_disabled_down:'orange'
        MDFillRoundFlatButton:
            text: "  Цена:  "
            font_size:24
            custom_color: "black"
            line_color:'orange'
            text_color:'black'
            halign: "center"
            pos_hint:{'center_x':0.5,'center_y':0.370}
            disabled: False
            background_disabled_down:'orange' 		
        OpL2:
            size: self.texture_size
            text:"Фоксфорд — онлайн-школа для учеников 1−11 классов, учителей и родителей. На онлайн-курсах и индивидуальных занятиях с репетитором школьники готовятся к ЕГЭ, ОГЭ, олимпиадам, изучают школьные предметы. Занятия ведут преподаватели МГУ, МФТИ, ВШЭ и других ведущих вузов страны."
        OpL1:
            text_size: root.width, None
            size: self.texture_size
            text:"Английский язык, биология,физика,химия,история, информатика,литература,математика,обществознание,русский язык,литература,история"
        OpL3:
            text:" Фоксфорд предоставляет разные тарифные планы для обучения.\\n Их цена варируется от 1990р - до 55000р в месяц "
        OpS:
            on_release:
                webbrowser.get().open_new_tab("https://externat.foxford.ru/high")
       
<Umsc>:
    name:'fifth'
    OP:
        Back:
			on_release: 
				app.root.current = "second"
				root.manager.transition.direction = "right"
        MDCard:
            size_hint: .98, .6
            focus_behavior: False
            pos_hint: {"center_x": .5, "center_y": .5}
            color: (56,56,56)
        
 
 
        MDFillRoundFlatButton:
            text: "  Описание:  "
            font_size:24
            custom_color: "black"
            line_color:'orange'
            text_color:'black'
            halign: "center"
            pos_hint:{'center_x':0.5,'center_y':0.73}
            disabled: False
            background_disabled_down:'orange'
        MDFillRoundFlatButton:
            text: "  Предметы:  "
            font_size:24
            custom_color: "black"
            line_color:'orange'
            text_color:'black'
            halign: "center"
            pos_hint:{'center_x':0.5,'center_y':0.55}
            disabled: False
            background_disabled_down:'orange'
        MDFillRoundFlatButton:
            text: "  Цена:  "
            font_size:24
            custom_color: "black"
            line_color:'orange'
            text_color:'black'
            halign: "center"
            pos_hint:{'center_x':0.5,'center_y':0.370}
            disabled: False
            background_disabled_down:'orange' 
        OpL2:
            size: self.texture_size
            text:"Умскул - Онлайн-школа для подготовки к выпускным экзаменам.Умскул уже выпустил более 34000 учеников, которые сдали ЕГЭ на 90+ баллов. Также Умскул успел подготовить 2367 учеников, которые сдали единый государственный экзамен на 100 баллов.   "
        OpL1:
            text_size: root.width, None
            size: self.texture_size
            text:"Английский язык, биология,физика,химия,история, информатика,литература,математика,обществознание,русский язык,литература,история"
        OpL3:
            text:"Умсул предоставляет разные тарифные планы для обучения.\\n Их цена варируется от 3890р - до 6390р в месяц "
        OpS:
            on_release:
                webbrowser.get().open_new_tab("https://umschool.net/?utm_source=yandex&utm_medium=cpc&utm_campaign=UMS_304795_yd_s_mg_obshie_ege_rus%7Cs%7Cya_search%7Cm%7Ccpc%7Cpr%7C109%7Cd%7C102%7Csub%7C102%7Cse%7C102%7Cr%7C102%7Cp%7C104%7C88708661&utm_content=cid%7C88708661%7Cgid%7C5210632617%7Caid%7C14285610733%7Cap%7Cno%7Cphr%7C45069929908%7Crt%7C45069929908%7Cdvc%7Cdesktop%7Cpos%7Cpremium4%7Cmch%7C%7Csrc%7Cnonempid_UMS_304795_yd_s_mg_obshie_ege_russya_searchmcpcpr109d102sub1&utm_term=---autotargeting&yclid=450063880880652287")
       
       
<LOm>:
    name:'six'
    OP:
        Back:
            on_release: 
                app.root.current = "second"
                root.manager.transition.direction = "right"
            
        MDCard:
            size_hint: .98, .6
            focus_behavior: False
            pos_hint: {"center_x": .5, "center_y": .5}
            color: (56,56,56)
        
 
 
        MDFillRoundFlatButton:
            text: "  Описание:  "
            font_size:24
            custom_color: "black"
            line_color:'orange'
            text_color:'black'
            halign: "center"
            pos_hint:{'center_x':0.5,'center_y':0.73}
            disabled: False
            background_disabled_down:'orange'
        MDFillRoundFlatButton:
            text: "  Предметы:  "
            font_size:24
            custom_color: "black"
            line_color:'orange'
            text_color:'black'
            halign: "center"
            pos_hint:{'center_x':0.5,'center_y':0.55}
            disabled: False
            background_disabled_down:'orange'
        MDFillRoundFlatButton:
            text: "  Цена:  "
            font_size:24
            custom_color: "black"
            line_color:'orange'
            text_color:'black'
            halign: "center"
            pos_hint:{'center_x':0.5,'center_y':0.370}
            disabled: False
            background_disabled_down:'orange'        
        OpL2:
            text:"Skysmart - Онлайн-школа,которая позволяет обучаться в абсолютно разных направлениях. Здесь вы можете не только подготовиться к грядущим экзаменам,но и обучиться например игре в шахматы или созданию игр."

        OpL1:
            markup:True
            text_size: root.width, None
            size: self.texture_size
            text:"Английский язык,физика,химия,информатика,математика,обществознание,русский язык"
        OpL3:
            text:" Skysmart предоставляет возможность оплачивать обучение либо каждый месяц, либо оплатить подписку на 3-12 месяцев. Цена: 1 месяц - 9960р в месяц; 3 месяца - 8076р в месяц; 6 месяцев - 6360р в месяц; 12 месяцев - 5960р в месяц."
        OpS:
            on_release:
                webbrowser.get().open_new_tab("https://umschool.net/?utm_source=yandex&utm_medium=cpc&utm_campaign=UMS_304795_yd_s_mg_obshie_ege_rus%7Cs%7Cya_search%7Cm%7Ccpc%7Cpr%7C109%7Cd%7C102%7Csub%7C102%7Cse%7C102%7Cr%7C102%7Cp%7C104%7C88708661&utm_content=cid%7C88708661%7Cgid%7C5210632617%7Caid%7C14285610733%7Cap%7Cno%7Cphr%7C45069929908%7Crt%7C45069929908%7Cdvc%7Cdesktop%7Cpos%7Cpremium4%7Cmch%7C%7Csrc%7Cnonempid_UMS_304795_yd_s_mg_obshie_ege_russya_searchmcpcpr109d102sub1&utm_term=---autotargeting&yclid=450063880880652287")
           
       
"""




class FirstWindow(Screen):
	pass
class ThirdWindow(Screen):
    pass
class SecondWindow(Screen):
    pass
class FourthWindow(Screen):
    pass
class Umsc(Screen):
    pass
class LOm(Screen):
    source = StringProperty()
    text = StringProperty()
    shadow = StringProperty()
class WindowManager(ScreenManager):
    pass




class MainApp(MDApp):
    def close_application(self):
        App.get_running_app().stop()
        Window.close()
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.root = Builder.load_string(KV)


MainApp().run()
