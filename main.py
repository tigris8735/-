from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty

# Устанавливаем размер для мобильного устройства
Window.size = (360, 640)

Builder.load_string('''

<MenuButton>:
    size_hint: (None, None)
    size: (dp(50), dp(50))
    background_color: (0.3, 0.3, 0.3, 1)
    background_normal: ''
    canvas.before:
        Color:
            rgba: (0.4, 0.7, 0.4, 1)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [dp(10)]
    Label:
        text: 'MENU'
        font_size: dp(12)
        color: (1, 1, 1, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


<NavButton>:
    size_hint: (1, None)
    height: dp(60)
    background_color: (0.2, 0.2, 0.2, 1)
    background_normal: ''
    Label:
        text: root.text
        font_size: dp(14)
        color: (0.4, 0.7, 0.4, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


<TrainingCard>:
    size_hint: (1, None)
    height: dp(100)
    background_color: (0.15, 0.15, 0.15, 1)
    background_normal: ''
    BoxLayout:
        orientation: 'horizontal'
        padding: dp(15)
        spacing: dp(10)
        size: root.size
        pos: root.pos
        
        Label:
            id: title_label
            text: root.title
            font_size: dp(18)
            color: (0.9, 0.9, 0.9, 1)
            halign: 'left'
            valign: 'middle'
            text_size: self.width, None
            size_hint_x: 0.7
            
        Label:
            id: duration_label
            text: root.duration
            font_size: dp(16)
            color: (0.4, 0.7, 0.4, 1)
            halign: 'right'
            valign: 'middle'
            text_size: self.width, None
            size_hint_x: 0.3


<ProfileScreen>:
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(20)
        
        Label:
            text: 'ПРОФИЛЬ'
            font_size: dp(24)
            color: (0.4, 0.7, 0.4, 1)
            size_hint_y: None
            height: dp(50)
            
        BoxLayout:
            orientation: 'vertical'
            spacing: dp(15)
            
            Label:
                text: 'Имя: Пользователь'
                font_size: dp(18)
                color: (0.9, 0.9, 0.9, 1)
                halign: 'left'
                
            Label:
                text: 'Уровень: Продвинутый'
                font_size: dp(18)
                color: (0.9, 0.9, 0.9, 1)
                halign: 'left'
                
            Label:
                text: 'Тренировок выполнено: 42'
                font_size: dp(18)
                color: (0.9, 0.9, 0.9, 1)
                halign: 'left'
            
        Button:
            text: 'Назад'
            size_hint_y: None
            height: dp(50)
            background_color: (0.4, 0.7, 0.4, 1)
            on_press: root.manager.current = 'main'
''')

class MenuButton(Button):
    pass

class NavButton(Button):
    pass

class TrainingCard(Button):
    title = StringProperty('')
    duration = StringProperty('')

class ProfileScreen(Screen):
    pass

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()
    
    def build_ui(self):
        """Создание интерфейса главного экрана"""
        # Основные цвета
        dark_gray = (0.1, 0.1, 0.1, 1)
        light_gray = (0.3, 0.3, 0.3, 1)
        green = (0.4, 0.7, 0.4, 1)
        
        # Главный макет
        main_layout = BoxLayout(orientation='vertical', spacing=dp(5))
        
        # Верхняя панель
        top_panel = self.create_top_panel(light_gray, green)
        
        # Прокручиваемая область
        scroll_area = self.create_scroll_area(green)
        
        # Нижняя навигация
        nav_panel = self.create_nav_panel()
        
        main_layout.add_widget(top_panel)
        main_layout.add_widget(scroll_area)
        main_layout.add_widget(nav_panel)
        
        self.add_widget(main_layout)
    
    def create_top_panel(self, bg_color, btn_color):
        """Создание верхней панели с поиском"""
        panel = BoxLayout(
            size_hint=(1, None),
            height=dp(50),
            spacing=dp(5),
            padding=[dp(5), 0, dp(5), 0]
        )
        
        # Кнопка меню
        self.menu_btn = MenuButton()
        self.menu_btn.bind(on_release=self.show_menu)
        
        # Поле поиска
        self.search_input = TextInput(
            hint_text='Поиск...',
            hint_text_color=(0.5, 0.5, 0.5, 1),
            size_hint=(1, None),
            height=dp(40),
            background_color=bg_color,
            foreground_color=(0.9, 0.9, 0.9, 1),
            font_size=dp(16),
            padding=[dp(10)]*4
        )
        
        # Кнопка поиска
        self.search_btn = Button(
            text='ПОИСК',
            size=(dp(80), dp(40)),
            background_color=btn_color,
            color=(1, 1, 1, 1),
            font_size=dp(14),
            bold=True
        )
        
        panel.add_widget(self.menu_btn)
        panel.add_widget(self.search_input)
        panel.add_widget(self.search_btn)
        
        return panel
    
    def create_scroll_area(self, scroll_color):
        """Создание прокручиваемой области с контентом"""
        scroll_view = ScrollView(
            bar_width=dp(4),
            bar_color=scroll_color,
            bar_inactive_color=(0.4, 0.7, 0.4, 0.3)
        )
        
        content = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            spacing=dp(10),
            padding=[dp(10), dp(5)]*2
        )
        content.bind(minimum_height=content.setter('height'))
        
        # Добавление карточек тренировок
        workouts = [
            ('Силовая тренировка', '45 мин'),
            ('Кардио сессия', '30 мин'),
            ('Йога для начинающих', '60 мин'),
            ('Кроссфит WOD', '50 мин')
        ]
        
        for title, duration in workouts:
            content.add_widget(TrainingCard(title=title, duration=duration))
        
        scroll_view.add_widget(content)
        return scroll_view
    
    def create_nav_panel(self):
        """Создание нижней панели навигации"""
        panel = BoxLayout(
            size_hint=(1, None),
            height=dp(60),
            spacing=dp(2)
        )
        
        # Элементы навигации
        buttons = ['ГЛАВНАЯ', 'ТРЕНИРОВКИ', 'ПРОГРЕСС', 'ПРОФИЛЬ']
        for text in buttons:
            btn = NavButton(text=text)
            if text == 'ПРОФИЛЬ':
                btn.bind(on_release=lambda x: self.switch_to_profile())
            panel.add_widget(btn)
        
        return panel
    
    def show_menu(self, instance):
        """Отображение всплывающего меню"""
        menu_content = BoxLayout(
            orientation='vertical',
            spacing=dp(10),
            padding=dp(20)
        )
        
        menu_items = [
            ('Мой профиль', self.switch_to_profile),
            ('Настройки', lambda: print("Настройки")),
            ('Выйти', App.get_running_app().stop)
        ]
        
        for text, callback in menu_items:
            btn = Button(
                text=text,
                size_hint_y=None,
                height=dp(50),
                background_color=(0.2, 0.2, 0.2, 1),
                color=(0.4, 0.7, 0.4, 1)
            )
            btn.bind(on_release=lambda x, cb=callback: cb())
            menu_content.add_widget(btn)
        
        Popup(
            title='Меню',
            content=menu_content,
            size_hint=(0.8, None),
            height=dp(250),
            background_color=(0.1, 0.1, 0.1, 1)
        ).open()
    
    def switch_to_profile(self):
        """Переключение на экран профиля"""
        self.manager.current = 'profile'

class FitnessApp(App):
    def build(self):
        """Создание приложения с экранами"""
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(ProfileScreen(name='profile'))
        return sm

if __name__ == '__main__':
    FitnessApp().run()