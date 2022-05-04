import phys as phys
from random import random
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.uix.dropdown import DropDown
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.modalview import ModalView
from kivy.clock import Clock
from kivy.vector import Vector


Builder.load_string("""
#:import get_color_from_hex kivy.utils.get_color_from_hex
<FirstScreen>:
    md_bg_color: app.theme_cls.bg_light
    MDFillRoundFlatButton:
        id:start
        text: "start"
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
        font_name: "Georgia"
        on_release: root.manager.current= 'dvizhuha'
        md_bg_color: app.theme_cls.primary_light

    MDFillRoundFlatButton:
        id: set1
        text: "settings"
        font_name: "Georgia"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        on_release: root.manager.current= 'settings'

    MDFillRoundFlatButton:
        id: task
        text: "tasks"
        font_name: "Georgia"
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        on_release: root.manager.current= 'tasks'
    MDFillRoundFlatIconButton:
        id: exit
        icon: "exit-to-app"
        font_name: "Georgia"
        md_bg_color: app.theme_cls.primary_dark
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        on_release: app.stop()

<Tasks>:
    MDToolbar:
        id: toolbar
        title: "Tasks"
        pos_hint: {"top": 1}

    MDSwiper:
        size_hint_y: None
        height: root.height - toolbar.height - dp(30)
        y: root.height - self.height - toolbar.height - dp(80)
        MDSwiperItem:
            MDRelativeLayout:
                orientation: 'vertical'
                MDLabel:
                    id: scale
                    text: 'Scale'
                    pos_hint: {"center_x": 0.5, "center_y": 0.7}
                    font_size: 20
                    font_name: "Georgia"
                MDLabel:
                    id: x_y
                    text: 'x, y : 100 = 1 a. u (149*10^9 m)'
                    pos_hint: {"center_x": 0.5, "center_y": 0.60}
                    font_name: "Georgia"
                MDLabel:
                    id: vx_vy
                    text: 'vx, vy : 1 = 1 m/s'
                    pos_hint: {"center_x": 0.5, "center_y": 0.55}
                    font_name: "Georgia"
                MDLabel:
                    id: m_s
                    text: 'm: 1 = 10^ 24 kg'
                    pos_hint: {"center_x": 0.5, "center_y": 0.50}
                    font_name: "Georgia"
                MDLabel:
                    id: q_s
                    text: 'q: 1= 10^18 C'
                    pos_hint: {"center_x": 0.5, "center_y": 0.45}
                    font_name: "Georgia"
        MDSwiperItem:
            MDRelativeLayout:
                orientation: 'vertical'
                MDLabel:
                    id: task1_1
                    text: 'Task 1'
                    pos_hint: {"center_x": 0.5, "center_y": 0.7}
                    font_size: 20
                    font_name: "Georgia"
                MDLabel:
                    id: task1
                    text: 'Place 2 oppositely charged objects on the screen. Add object 3 so as to avoid collision 1 and 2.'
                    pos_hint: {"center_x": 0.5, "center_y": 0.60}
                    font_name: "Georgia"
        MDSwiperItem:
            MDRelativeLayout:
                orientation: 'vertical'
                MDLabel:
                    id: task2_1
                    text: 'Task 2'
                    pos_hint: {"center_x": 0.5, "center_y": 0.7}
                    font_size: 20
                    font_name: "Georgia"
                MDLabel:
                    id: task2
                    text: 'Create a system from a massive object and 3 objects revolving around it.'
                    pos_hint: {"center_x": 0.5, "center_y": 0.60}
                    font_name: "Georgia"
        MDSwiperItem:
            MDRelativeLayout:
                orientation: 'vertical'
                MDLabel:
                    id: task3_1
                    text: 'Task 3'
                    pos_hint: {"center_x": 0.5, "center_y": 0.7}
                    font_size: 20
                    font_name: "Georgia"
                MDLabel:
                    id: task3
                    text: 'Create 2 objects so that body 2 rotates around body 1, with one of the bodies moving along the x-axis and the other moving along the y-axis. Next, add 3 stationary objects that will pull both.'
                    pos_hint: {"center_x": 0.5, "center_y": 0.60}
                    font_name: "Georgia"
        MDSwiperItem:
            MDRelativeLayout:
                orientation: 'vertical'
                MDLabel:
                    id: task4_1
                    text: 'Task 4'
                    pos_hint: {"center_x": 0.5, "center_y": 0.7}
                    font_size: 20
                    font_name: "Georgia"
                MDLabel:
                    id: task4
                    text: 'Place 2 opposite charges on the same diagonal. They must not pulled each other. You can add two extra objects.'
                    pos_hint: {"center_x": 0.5, "center_y": 0.60}
                    font_name: "Georgia"

        MDSwiperItem:
            MDRelativeLayout:
                orientation: 'vertical'
                MDLabel:
                    id: task5_1
                    text: 'Task 5'
                    pos_hint: {"center_x": 0.5, "center_y": 0.7}
                    font_size: 20
                    font_name: "Georgia"
                MDLabel:
                    id: task5
                    text: 'Place 3 bodies with a small mass at the bottom of the screen. In the upper part, place the body with more mass. The velocities of the bodies are 0. Without moving the objects, make the first three objects be pulled to the larger one.'
                    pos_hint: {"center_x": 0.5, "center_y": 0.60}
                    font_name: "Georgia"
    MDRelativeLayout:
    MDFillRoundFlatIconButton:
        id: back_tasks
        text: "back"
        icon: "arrow-left-bold-circle"
        font_name: "Georgia"
        md_bg_color: app.theme_cls.primary_dark
        pos_hint: {"center_x": 0.9, "center_y": 0.1}
        on_release: root.manager.current= 'first'
<MainScreen> :
    md_bg_color: app.theme_cls.bg_light
    MDFillRoundFlatButton:
        id: create
        text: "create"
        font_name: "Georgia"
        pos_hint: {"center_x": 0.15, "center_y": 0.05}
        on_release: on_release: root.open()
    MDFillRoundFlatButton:
        id: clearb
        text: "clear"
        font_name: "Georgia"
        pos_hint: {"center_x": 0.5, "center_y": 0.05}
        on_release: root.child.clear()
    MDFillRoundFlatIconButton:
        id: back_main
        icon: "arrow-left-bold-circle"
        text: "back"
        md_bg_color: app.theme_cls.primary_dark
        font_name: "Georgia"
        icon_size: "64sp"
        pos_hint: {"center_x": 0.85, "center_y": 0.05}
        on_release: root.manager.current= 'first'

<CustomLayout> :
    id: custom
    size_hint: None, None
    size: 1000, 1900
    pos: 0,1900

<SecondScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        adaptive_size: True
        MDTextField:
            id:x
            max_text_length: 4
            font_name: "Georgia"
            hint_text: ' x'
            multiline: False
            helper_text: "Error"
            helper_text_mode: "on_error"
            error: False
            on_text: root.set_error_message(x)
        MDTextField:
            id:y
            font_name: "Georgia"
            max_text_length: 4
            hint_text: ' y'
            multiline: False
            helper_text: "Error"
            helper_text_mode: "on_error"
            error: False
            on_text: root.set_error_message(y)

        MDTextField:
            id:vx
            font_name: "Georgia"
            max_text_length: 8
            hint_text: ' vx'
            multiline: False
            helper_text: "Error"
            helper_text_mode: "on_error"
            error: False
            on_text: root.set_error_message(vx)
        MDTextField:
            id:vy
            font_name: "Georgia"
            max_text_length: 8
            hint_text: ' vy'
            multiline: False
            helper_text: "Error"
            helper_text_mode: "on_error"
            error: False
            on_text: root.set_error_message(vy)
        MDTextField:
            id:m
            font_name: "Georgia"
            max_text_length: 10
            hint_text: ' m'
            multiline: False
            helper_text: "Error"
            helper_text_mode: "on_error"
            error: False
            on_text: root.set_error_message_m(m)
        MDTextField:
            id:q
            font_name: "Georgia"
            max_text_length: 5
            hint_text: ' q'
            multiline: False
            helper_text: "Error"
            helper_text_mode: "on_error"
            error: False
            on_text: root.set_error_message(q)
        MDBoxLayout:
            adaptive_size: True
            MDIconButton:
                icon: "minus"
                size_hint: None, None
                size: 200, 200
                pos_hint: {"center_x": 0.1, "center_y": 0.5}
                on_release: root.m_p(size, 1)
            MDTextButton:
                id: size
                text: "50"
                pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDIconButton:
                icon: "plus"
                size_hint: None, None
                size: 200, 200
                pos_hint: {"center_x": 0.7, "center_y": 0.5}
                on_release: root.m_p(size, 0)
        MDBoxLayout:
            adaptive_size: True
            MDIconButton:
                icon: "check-outline"
                size_hint: None, None
                size: 200, 200
                pos_hint: {"center_x": 0.4, "center_y": 0.5}
                on_release:
                    root.create_object(x.text, y.text, vx.text, vy.text, m.text, q.text,
                    x.error, y.error, vx.error, vy.error, m.error, q.error)
                    root.dismiss()
            MDIconButton:
                icon: "arrow-left-bold"
                size_hint: None, None
                size: 200, 200
                pos_hint: {"center_x": 0.6, "center_y": 0.5}
                on_release: root.dismiss()

<SettingScreen>:
    md_bg_color: app.theme_cls.bg_light
    MDBoxLayout:
        orientation: 'vertical'
        MDToolbar:
            id: tool
            title: "Settings"
        MDRelativeLayout:

            orientation: 'vertical'


            MDFillRoundFlatButton:
                id:change
                text:'Change language'
                font_name: "Georgia"
                pos_hint: {'center_x': 0.5, 'center_y': 0.7}
                on_release: dropdown.open(self)
            MDRelativeLayout:

                MDIconButton:
                    id: purple
                    icon: "circle"
                    size_hint: None, None
                    size: 200, 200
                    md_bg_color: get_color_from_hex('9C27B0')
                    pos_hint: {"center_x": 0.3, "center_y": 0.5}
                    on_release:
                        app.theme_cls.primary_palette = "Purple"
                        root.manager.get_screen('settings').ids.purple.md_bg_color = get_color_from_hex('9C27B0')
                        root.manager.get_screen('settings').ids.red.md_bg_color = get_color_from_hex('D32F2F')
                        root.manager.get_screen('settings').ids.green.md_bg_color = get_color_from_hex('388E3C')
                        root.manager.get_screen('first').ids.start.md_bg_color = app.theme_cls.primary_light
                        root.manager.get_screen('first').ids.exit.md_bg_color = app.theme_cls.primary_dark
                        root.manager.get_screen('dvizhuha').ids.back_main.md_bg_color = app.theme_cls.primary_dark
                        root.manager.get_screen('tasks').ids.back_tasks.md_bg_color = app.theme_cls.primary_dark

                MDIconButton:
                    id: red
                    icon: "circle"
                    size_hint: None, None
                    size: 200, 200
                    md_bg_color: get_color_from_hex('D32F2F')
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    on_release:
                        app.theme_cls.primary_palette = "Red"
                        root.manager.get_screen('settings').ids.purple.md_bg_color = get_color_from_hex('9C27B0')
                        root.manager.get_screen('settings').ids.red.md_bg_color = get_color_from_hex('D32F2F')
                        root.manager.get_screen('settings').ids.green.md_bg_color = get_color_from_hex('388E3C')
                        root.manager.get_screen('first').ids.start.md_bg_color = app.theme_cls.primary_light
                        root.manager.get_screen('first').ids.exit.md_bg_color = app.theme_cls.primary_dark
                        root.manager.get_screen('dvizhuha').ids.back_main.md_bg_color = app.theme_cls.primary_dark
                        root.manager.get_screen('tasks').ids.back_tasks.md_bg_color = app.theme_cls.primary_dark
                MDIconButton:
                    id: green
                    icon: "circle"
                    size_hint: None, None
                    size: 200, 200
                    md_bg_color: get_color_from_hex('388E3C')
                    pos_hint: {"center_x": 0.7, "center_y": 0.5}
                    on_release:
                        app.theme_cls.primary_palette = "Green"
                        root.manager.get_screen('settings').ids.purple.md_bg_color = get_color_from_hex('9C27B0')
                        root.manager.get_screen('settings').ids.red.md_bg_color = get_color_from_hex('D32F2F')
                        root.manager.get_screen('settings').ids.green.md_bg_color = get_color_from_hex('388E3C')
                        root.manager.get_screen('first').ids.start.md_bg_color = app.theme_cls.primary_light
                        root.manager.get_screen('first').ids.exit.md_bg_color = app.theme_cls.primary_dark
                        root.manager.get_screen('dvizhuha').ids.back_main.md_bg_color = app.theme_cls.primary_dark
                        root.manager.get_screen('tasks').ids.back_tasks.md_bg_color = app.theme_cls.primary_dark
            MDFillRoundFlatIconButton:
                id: back_set
                icon: "arrow-left-bold-circle"
                size_hint: None, None
                size: 300, 200
                text: "back"
                font_name: "Georgia"
                md_bg_color: app.theme_cls.primary_dark
                icon_size: "64sp"
                pos_hint: {"center_x": 0.5, "center_y": 0.3}
                on_release: root.manager.current= 'first'

    DropDown:
        id:dropdown
        dropdown : self.dismiss()

        MDTextButton:
            text: 'rus'
            font_name: "Georgia"
            size_hint:  None, None
            size:  100, 30
            on_release:
                root.change(
                root.manager.get_screen('settings').ids.change,
                root.manager.get_screen('settings').ids.tool,
                root.manager.get_screen('first').ids.start,
                root.manager.get_screen('first').ids.set1,
                root.manager.get_screen('dvizhuha').ids.create,
                root.manager.get_screen('dvizhuha').ids.clearb,
                root.manager.get_screen('dvizhuha').ids.back_main,
                root.manager.get_screen('settings').ids.back_set,
                root.manager.get_screen('tasks').ids.toolbar,
                root.manager.get_screen('tasks').ids.task1_1,
                root.manager.get_screen('tasks').ids.task2_1,
                root.manager.get_screen('tasks').ids.task3_1,
                root.manager.get_screen('tasks').ids.task4_1,
                root.manager.get_screen('tasks').ids.task5_1,
                root.manager.get_screen('tasks').ids.task1,
                root.manager.get_screen('tasks').ids.task2,
                root.manager.get_screen('tasks').ids.task3,
                root.manager.get_screen('tasks').ids.task4,
                root.manager.get_screen('tasks').ids.task5,
                root.manager.get_screen('tasks').ids.scale,
                root.manager.get_screen('tasks').ids.x_y,
                root.manager.get_screen('tasks').ids.vx_vy,
                root.manager.get_screen('tasks').ids.m_s,
                root.manager.get_screen('tasks').ids.q_s,
                root.manager.get_screen('tasks').ids.back_tasks,
                1 )

        MDTextButton:
            text: 'eng'
            font_name: "Georgia"
            size_hint:  None, None
            size:  100, 30

            on_release:
                root.change(
                root.manager.get_screen('settings').ids.change,
                root.manager.get_screen('settings').ids.tool,
                root.manager.get_screen('first').ids.start,
                root.manager.get_screen('first').ids.set1,
                root.manager.get_screen('dvizhuha').ids.create,
                root.manager.get_screen('dvizhuha').ids.clearb,
                root.manager.get_screen('dvizhuha').ids.back_main,
                root.manager.get_screen('settings').ids.back_set,
                root.manager.get_screen('tasks').ids.toolbar,
                root.manager.get_screen('tasks').ids.task1_1,
                root.manager.get_screen('tasks').ids.task2_1,
                root.manager.get_screen('tasks').ids.task3_1,
                root.manager.get_screen('tasks').ids.task4_1,
                root.manager.get_screen('tasks').ids.task5_1,
                root.manager.get_screen('tasks').ids.task1,
                root.manager.get_screen('tasks').ids.task2,
                root.manager.get_screen('tasks').ids.task3,
                root.manager.get_screen('tasks').ids.task4,
                root.manager.get_screen('tasks').ids.task5,
                root.manager.get_screen('tasks').ids.scale,
                root.manager.get_screen('tasks').ids.x_y,
                root.manager.get_screen('tasks').ids.vx_vy,
                root.manager.get_screen('tasks').ids.m_s,
                root.manager.get_screen('tasks').ids.q_s,
                root.manager.get_screen('tasks').ids.back_tasks,
                0 )
<Object>
    size_hint: None, None
    size: self.size
    pos: 0,100
<Move>
    size_hint: None, None
    size: 1000, 1900
    pos: 0,100
""")


class FirstScreen(MDScreen):
    pass
class Tasks (MDScreen):
    pass


class CustomLayout(BoxLayout):
    def __init__(self, dispatcher, **kwargs):
        super(CustomLayout, self).__init__(**kwargs)
        self.dispatcher = dispatcher

    def clear(self):
        self.clear_widgets()
        Object.num_new = Object.num +1

class MainScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.child = CustomLayout(Widget())
        self.second = SecondScreen(self.child)
        self.add_widget(self.child)

    def open(self):
        self.second.open()


class SecondScreen(ModalView):
    def __init__(self, child_screen, **kw):
        super().__init__(**kw)
        self.child_screen = child_screen
        self.size_point = 0
        self.pointsize = [50, 50]
    def create_object(self, x, y, vx, vy, mas, electric_charge, x_error, y_error, vx_error, vy_error, m_error, q_error):
        if x_error == True:
            pass
        elif y_error == True:
            pass
        elif vx_error == True:
            pass
        elif vy_error == True:
            pass
        elif m_error == True:
            pass
        elif q_error== True:
            pass
        else:
            Object.num += 1
            self.object = Move(Object.num)
            self.object.create(x=float(x) + 100, y=float(y) + 100, size=self.pointsize,
                               vx=float(vx), vy=float(vy),
                               mas=float(mas), electric_charge=float(electric_charge))

            self.child_screen.add_widget(self.object)

            self.clock()

    def m_p(self, size, n):
        if n == 1 and self.size_point != 10:
            size.text = str(int(size.text) - 10)
            self.size_point = int(size.text)
            self.pointsize = [self.size_point, self.size_point]
        elif n == 0 and self.size_point != 100:
            size.text = str(int(size.text) + 10)
            self.size_point = int(size.text)
            self.pointsize = [self.size_point, self.size_point]
        else:
            pass

    def clock(self):
        my_clock = Clock
        my_clock.schedule_once(self.object.update, 0)
        my_clock.schedule_interval(self.object.update, 0.1)

    def set_error_message(self, text_field):
        try:
            float(text_field.text)
            text_field.error = False
        except ValueError:
            text_field.error = True
    def set_error_message_m(self, m):
        try:
            float(m.text)
            m.error = False
            if float(m.text) <= 0:
                m.error = True
        except ValueError:
            m.error = True



class Object(Widget):
    items = []
    num = -1
    num_new = 0

    def __init__(self, x, y, size, vx, vy, mas, electric_charge, **kw):
        super(Object, self).__init__(**kw)
        self.x = x
        self.y = y
        self.pos = [self.x, self.y]
        self.size = size
        self.vx = vx
        self.vy = vy
        self.mas = mas
        self.electric_charge = electric_charge

        self.coords = []
        Object.items.append(self)

    def draw(self):

        color = (random(), random(), random())
        with self.canvas:
            Color(*color)

        self.ellipse = Ellipse(pos=self.pos, size=self.size)
        self.line = Line(points=(self.pos[0], self.pos[1]))
        self.canvas.add(self.ellipse)
        self.canvas.add(self.line)

    def move(self, dt, num):
        num = num-Object.num_new
        self.interact = phys.Solver( num, Object.items[Object.num_new : Object.num +1 ])
        self.coords = ((self.interact.output_coords_func()[0], self.interact.output_coords_func()[1]))
        self.pos = Vector(self.coords)
        self.ellipse.pos = self.pos
        self.line.points += (self.pos[0], self.pos[1])

    def on_touch_down(self, touch):

        if (self.pos[0] - self.size[0]) <= touch.pos[0] <= (
                self.pos[0] + self.size[0]):
            if (self.pos[1] - self.size[1]) <= touch.pos[1] <= (
                    self.pos[1] + self.size[1]):
                touch.grab(self)

                return True

    def move_touch(self):
        self.pos = Vector(self.move_pos)
        self.ellipse.pos = self.pos
        self.line.points += (self.pos[0], self.pos[1])
        self.vx = self.vx
        self.vy = self.vy

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            if (self.pos[0] - 1.5 * self.size[0]) <= touch.pos[0] <= (
                    self.pos[0] + 1.5 * self.size[0]):
                if (self.pos[1] - 1.5 * self.size[1]) <= touch.pos[1] <= (
                        self.pos[1] + 1.5 * self.size[1]):
                    self.x = touch.pos[0] - 1.5 * self.size[0] / 2
                    self.y = touch.pos[1] - 1.5 * self.size[1] / 2
                    self.move_pos = [self.x, self.y]
                    self.move_touch()
        else:
            pass

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
        else:
            pass


class Move(Widget):
    def __init__(self, num, **kw):
        super().__init__(**kw)
        self.num = num

    def update(self, dt):
        if self.num < Object.num_new :
            pass
        else:
            self.point.move(dt, self.num)

    def create(self, x, y, size, vx, vy, mas, electric_charge):
        self.point = Object(x=x, y=y, size=size, vx=vx, vy=vy, mas=mas, electric_charge=electric_charge)

        self.point.draw()
        self.add_widget(self.point)



class SettingScreen(MDScreen):

    def change(self, change, tool, start, set1, create, clearb, back_main, back_set, toolbar, task1_1, task2_1, task3_1 , task4_1, task5_1, task1, task2, task3, task4, task5, scale, x_y, vx_vy, m_s, q_s, back_tasks, lang ):
        if lang == 1:
            change.text = 'Изменить язык'
            tool.title = 'Настройки'
            start.text = 'начать'
            set1.text = 'настройки'
            create.text = 'создать'
            clearb.text = 'очистить'
            back_main.text = 'назад'
            back_set.text = 'назад'
            toolbar.title = 'Задачи'
            task1_1.text = 'Задача 1'
            task2_1.text = 'Задача 2'
            task3_1.text = 'Задача 3'
            task4_1.text = 'Задача 4'
            task5_1.text = 'Задача 5'
            task1.text = 'Разместите 2 разноименно заряженных тела на экране. Добавьте 3 тело так, чтобы избежать столкновения 1 и 2.'
            task2.text = 'Создайте систему из массивного тела и 3 объектов, обращающихся вокруг него.'
            task3.text = 'Создайте 2 объекта так, чтобы тело 2 вращалось вокруг тела 1, при этом одно из тел должно двигаться по оси х, другок по оси у. Далее добавьте 3 неподвижный объект, который притянет оба.'
            task4.text = 'Расположите на одной диагонали 2 разноименных заряда. Сделайте так, чтобы они не притянулись друг у другу, добавив два дополнительных объекта.'
            task5.text = 'Расположите в нижней части экрана 3 тела с небольшой массой. В верхней части расположите тело с большей массой. Скорости тел равны 0. Не перемещая объекты, заставьте три первых объекта притянуться к большему.'
            scale.text = 'Масштаб'
            x_y.text = 'x, y : 100 = 1 а. е (149*10^9 м)'
            vx_vy.text = 'vx, vy : 1 = 1 м/с'
            m_s.text = 'm: 1 = 10^ 24 кг'
            q_s.text = 'q: 1= 10^18 Кл'
            back_tasks.text = 'назад'
        else:
            change.text = 'Change language'
            tool.title = 'settings'
            start.text = 'start'
            set1.text = 'settings'
            create.text = 'create'
            clearb.text = 'clear'
            back_main.text = 'back'
            back_set.text = 'back'
            toolbar.title = 'Tasks'
            task1_1.text = 'Task 1'
            task2_1.text = 'Task 2'
            task3_1.text = 'Task 3'
            task4_1.text = 'Task 4'
            task5_1.text = 'Task 5'
            task1.text = 'Place 2 oppositely charged objects on the screen. Add object 3 so as to avoid collision 1 and 2.'
            task2.text = 'Create a system from a massive object and 3 objects revolving around it.'
            task3.text = 'Create 2 objects so that body 2 rotates around body 1, with one of the bodies moving along the x-axis and the other moving along the y-axis. Next, add 3 stationary objects that will pull both.'
            task4.text = 'Place 2 opposite charges on the same diagonal. They must not pulled each other. You can add two extra objects.'
            task5.text = 'Place 3 bodies with a small mass at the bottom of the screen. In the upper part, place the body with more mass. The velocities of the bodies are 0. Without moving the objects, make the first three objects be pulled to the larger one.'
            scale.text = 'Scale'
            x_y.text = 'x, y : 100 = 1 а. u (149*10^9 m)'
            vx_vy.text = 'vx, vy : 1 = 1 m/s'
            m_s.text = 'm: 1 = 10^ 24 kg'
            q_s.text = 'q: 1= 10^18 C'
            back_tasks.text = 'back'


class CustomDropDown(DropDown):
    pass


class TestApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SettingScreen(name='settings'))
        sm.add_widget(MainScreen(name='dvizhuha'))
        sm.add_widget(Tasks(name='tasks'))

        return sm
scale = 149 * 10 ** 7 # масштаб в 1 пк
scale_m = 10**24
scale_q = 10**18
stena_x1= 0*scale
stena_x2= 1000*scale
stena_y1 = 100*scale
stena_y2 = 2200*scale

dt = 50000
ms = 1.5

G = 6.67 * 10 ** (-11)
k = 8.987551787 * 10 ** 9


class Solver:
    def __init__(self, num, particles) :
        self.objects = particles
        self.num = num
        self.N = int(len(self.objects))

    def get_dvx_dt(self, a, b):

        ax = 0.0
        try:
            ax += (-G *
                   b.mas * scale_m * (
                           a.x * scale - b.x * scale) /
                   ((a.x * scale - b.x * scale) ** 2 + (a.y * scale - b.y * scale) ** 2) ** 1.5)
            ax += (k *
                   a.electric_charge * scale_q * b.electric_charge * scale_q / (a.mas * scale_m) * (
                           a.x * scale - b.x * scale) /
                   ((a.x * scale - b.x * scale) ** 2 + (a.y * scale - b.y * scale) ** 2) ** 1.5)
        except ZeroDivisionError:
            ax = 0

        return float(ax)

    def get_dvy_dt(self, a, b):

        ay = 0.0
        try:
            ay += (-G *
                   b.mas*scale_m * (
                           a.y*scale - b.y*scale) /
                   ((a.x*scale - b.x*scale) ** 2 + (a.y*scale - b.y*scale) ** 2) ** 1.5)
            ay += (k *
                   a.electric_charge*scale_q * b.electric_charge*scale_q / (a.mas*scale_m) * (
                           a.y*scale - b.y*scale) /
                   ((a.x*scale - b.x*scale) ** 2 + (a.y*scale - b.y*scale) ** 2) ** 1.5)
        except ZeroDivisionError:
            ay = 0
        return float(ay)

    def ydar(self, a, b):
        r = (a.x - b.x) ** 2 + (a.y - b.y) ** 2
        if r <= (self.objects[self.num].size[0]) ** 2:
            a.vx = (2 * b.mas*scale_m * b.vx + a.vx * (a.mas*scale_m - b.mas*scale_m )) / (a.mas*scale_m + b.mas*scale_m)/ ms
            a.vy = (2 * b.mas*scale_m * b.vy + a.vy * (a.mas*scale_m - b.mas*scale_m )) / (a.mas*scale_m + b.mas*scale_m)/ ms

        else:
            a.vx = a.vx
            b.vy = b.vy
        return a.vx, b.vy

    def stena(self, a):

        if a.x*scale < stena_x1:
            if a.vx <= 0:
                a.vx = -a.vx/ms
            else:
                a.vx = a.vx/ms
            a.x = stena_x1 /scale + 5
        elif a.x*scale > stena_x2:
            if a.vx >= 0:
                a.vx = -a.vx/ms
            else:
                a.vx = a.vx/ms
            a.x = stena_x2/scale -  5
        elif a.y*scale < stena_y1:
            if a.vy <= 0:
                a.vy = -a.vy/ms
            else:
                a.vy = a.vy/ms
            a.y = stena_y1/scale + 5
        elif a.y*scale > stena_y2:
            if a.vy >= 0:
                a.vy = -a.vy/ms
            else:
                a.vy = a.vy/ms
            a.y = stena_y2/scale - 5
        else:
            a.vx = a.vx
            a.vy = a.vy
        return a.vx, a.vy

    def calc_object(self, object):
        for object_n in self.objects:
            if object == object_n:
                continue
            object.vx += dt * self.get_dvx_dt(object, object_n)
            object.vy += dt * self.get_dvy_dt(object, object_n)
            self.ydar(object, object_n)

        self.euler(object)

    def euler(self, object):
        self.stena(object)
        object.x = (object.x * scale + dt * object.vx)/scale
        object.y = (object.y * scale + dt * object.vy)/scale

    def output_coords_func(self):
        coords = []
        self.calc_object(self.objects[self.num])
        coords.append(self.objects[self.num].x)
        coords.append(self.objects[self.num].y)

        return coords

if __name__ == '__main__':
    TestApp().run()
