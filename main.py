from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from datetime import datetime
import csv
import os

# Set window size for mobile
Window.size = (360, 640)

class TargetScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'target'
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Title
        title = Label(
            text='🕵️ SPY-CHAT', 
            size_hint_y=None, 
            height=80,
            font_size=32,
            color=(1, 0.2, 0.2, 1)
        )
        layout.add_widget(title)
        
        # Target label
        target_label = Label(
            text='🎯 Nama Target:', 
            size_hint_y=None, 
            height=50,
            font_size=20
        )
        layout.add_widget(target_label)
        
        # Target input
        self.target_input = TextInput(
            hint_text='Ketik nama target...',
            size_hint_y=None,
            height=50,
            font_size=18,
            multiline=False
        )
        layout.add_widget(self.target_input)
        
        # Next button
        next_btn = Button(
            text='Next Page >>',
            size_hint_y=None,
            height=60,
            font_size=20,
            background_color=(0.2, 0.6, 1, 1)
        )
        next_btn.bind(on_press=self.go_to_message)
        layout.add_widget(next_btn)
        
        # View data button
        view_btn = Button(
            text='📊 Lihat Data',
            size_hint_y=None,
            height=60,
            font_size=20,
            background_color=(0.8, 0.4, 0.8, 1)
        )
        view_btn.bind(on_press=self.view_data)
        layout.add_widget(view_btn)
        
        # Spacer
        layout.add_widget(Label())
        
        self.add_widget(layout)
    
    def go_to_message(self, instance):
        if self.target_input.text.strip():
            app = App.get_running_app()
            app.target_name = self.target_input.text.strip()
            app.root.current = 'message'
        else:
            self.show_popup('Error', 'Nama target tidak boleh kosong!')
    
    def view_data(self, instance):
        app = App.get_running_app()
        app.root.current = 'data'
    
    def show_popup(self, title, message):
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.8, 0.4)
        )
        popup.open()

class MessageScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'message'
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Title
        self.title_label = Label(
            text='💬 Pesan untuk: ', 
            size_hint_y=None, 
            height=80,
            font_size=24,
            color=(0.2, 0.8, 0.2, 1)
        )
        layout.add_widget(self.title_label)
        
        # Message label
        msg_label = Label(
            text='Isi pesan di sini:',
            size_hint_y=None,
            height=50,
            font_size=18
        )
        layout.add_widget(msg_label)
        
        # Message input
        self.message_input = TextInput(
            hint_text='Ketik pesan rahasia...',
            size_hint_y=0.4,
            font_size=16
        )
        layout.add_widget(self.message_input)
        
        # Button layout
        btn_layout = BoxLayout(size_hint_y=None, height=60, spacing=10)
        
        # Back button
        back_btn = Button(
            text='⬅️ Back',
            font_size=18,
            background_color=(0.6, 0.6, 0.6, 1)
        )
        back_btn.bind(on_press=self.go_back)
        btn_layout.add_widget(back_btn)
        
        # Submit button
        submit_btn = Button(
            text='📤 Submit',
            font_size=18,
            background_color=(0.2, 0.8, 0.2, 1)
        )
        submit_btn.bind(on_press=self.submit_message)
        btn_layout.add_widget(submit_btn)
        
        layout.add_widget(btn_layout)
        
        # Spacer
        layout.add_widget(Label())
        
        self.add_widget(layout)
    
    def on_enter(self):
        app = App.get_running_app()
        if hasattr(app, 'target_name'):
            self.title_label.text = f'💬 Pesan untuk: {app.target_name}'
    
    def go_back(self, instance):
        app = App.get_running_app()
        app.root.current = 'target'
    
    def submit_message(self, instance):
        if self.message_input.text.strip():
            app = App.get_running_app()
            self.save_to_csv(app.target_name, self.message_input.text.strip())
            self.show_popup('Berhasil!', f'Pesan untuk "{app.target_name}" berhasil dikirim!')
            self.message_input.text = ''
            app.root.current = 'target'
        else:
            self.show_popup('Error', 'Pesan tidak boleh kosong!')
    
    def save_to_csv(self, nama_target, pesan):
        waktu = datetime.now().strftime('[%d/%m %H.%M]')
        
        # Get app directory
        app_dir = App.get_running_app().user_data_dir
        csv_path = os.path.join(app_dir, 'data_korban.csv')
        
        # Create CSV if doesn't exist
        if not os.path.exists(csv_path):
            with open(csv_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Data'])
        
        # Append data
        with open(csv_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([f'{waktu} {nama_target}: {pesan}'])
    
    def show_popup(self, title, message):
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.8, 0.4)
        )
        popup.open()

class DataScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'data'
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Title
        title = Label(
            text='📊 Data Tersimpan',
            size_hint_y=None,
            height=80,
            font_size=24,
            color=(0.8, 0.4, 0.8, 1)
        )
        layout.add_widget(title)
        
        # Scroll view for data
        scroll = ScrollView()
        self.data_label = Label(
            text='Memuat data...',
            text_size=(None, None),
            valign='top',
            font_size=14
        )
        scroll.add_widget(self.data_label)
        layout.add_widget(scroll)
        
        # Button layout
        btn_layout = BoxLayout(size_hint_y=None, height=60, spacing=10)
        
        # Back button
        back_btn = Button(
            text='⬅️ Kembali',
            font_size=18,
            background_color=(0.6, 0.6, 0.6, 1)
        )
        back_btn.bind(on_press=self.go_back)
        btn_layout.add_widget(back_btn)
        
        # Delete button
        delete_btn = Button(
            text='🗑️ Hapus Data',
            font_size=18,
            background_color=(1, 0.2, 0.2, 1)
        )
        delete_btn.bind(on_press=self.delete_data)
        btn_layout.add_widget(delete_btn)
        
        layout.add_widget(btn_layout)
        
        self.add_widget(layout)
    
    def on_enter(self):
        self.load_data()
    
    def load_data(self):
        app = App.get_running_app()
        app_dir = app.user_data_dir
        csv_path = os.path.join(app_dir, 'data_korban.csv')
        
        if os.path.exists(csv_path):
            try:
                with open(csv_path, 'r', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    data = list(reader)
                    
                if len(data) > 1:  # Skip header
                    data_text = '\n\n'.join([row[0] for row in data[1:] if row])
                    self.data_label.text = data_text
                    self.data_label.text_size = (Window.width - 40, None)
                else:
                    self.data_label.text = 'Belum ada data tersimpan'
            except:
                self.data_label.text = 'Error membaca data'
        else:
            self.data_label.text = 'Belum ada data tersimpan'
    
    def go_back(self, instance):
        app = App.get_running_app()
        app.root.current = 'target'
    
    def delete_data(self, instance):
        app = App.get_running_app()
        app_dir = app.user_data_dir
        csv_path = os.path.join(app_dir, 'data_korban.csv')
        
        if os.path.exists(csv_path):
            os.remove(csv_path)
            self.show_popup('Berhasil!', 'Semua data berhasil dihapus!')
            self.load_data()
        else:
            self.show_popup('Info', 'Tidak ada data untuk dihapus')
    
    def show_popup(self, title, message):
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.8, 0.4)
        )
        popup.open()

class SpyChatApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.target_name = ""
    
    def build(self):
        self.title = "Spy-Chat"
        
        # Screen manager
        sm = ScreenManager()
        
        # Add screens
        sm.add_widget(TargetScreen())
        sm.add_widget(MessageScreen())
        sm.add_widget(DataScreen())
        
        return sm

if __name__ == '__main__':
    SpyChatApp().run()
