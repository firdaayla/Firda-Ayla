from kivy.config import Config
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '600')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle

class MenuButton(Button):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.font_size = 20
        self.bold = True
        self.color = (1, 1, 1, 1)  # Teks putih
        self.background_color = (0.8, 0.5, 0.7, 0.8)  # Pink transparan
        self.background_normal = ''  # Hilangkan background default
        self.size_hint = (1, 0.08)
        
        # Efek hover
        self.original_color = (0.8, 0.5, 0.7, 0.8)
        self.hover_color = (0.9, 0.6, 0.8, 0.9)  # Pink lebih terang saat hover
        
        # Bind events
        self.bind(on_enter=self.on_enter)
        self.bind(on_leave=self.on_leave)
    
    def on_enter(self, *args):
        """Saat mouse masuk ke button"""
        self.background_color = self.hover_color
    
    def on_leave(self, *args):
        """Saat mouse keluar dari button"""
        self.background_color = self.original_color

class DashboardAdmin(App):
    def build(self):
        self.title = "Dashboard Admin"
        
        main_layout = FloatLayout()
        
        # Background Image
        bg = Image(
            source='image.jpg',
            allow_stretch=True,
            keep_ratio=False
        )
        main_layout.add_widget(bg)
        
        # Button "Kembali" di pojok kiri atas
        back_button = Button(
            text="Kembali",
            font_size=16,
            size_hint=(0.1, 0.05),
            pos_hint={'x': 0.02, 'top': 0.98},
            background_color=(0.8, 0.5, 0.7, 0.8),  # Pink transparan
            color=(1, 1, 1, 1),  # Teks putih
            background_normal=''
        )
        back_button.bind(on_press=self.go_back)
        main_layout.add_widget(back_button)
        
        # Container untuk konten utama
        content = BoxLayout(
            orientation='vertical',
            padding=30,
            spacing=10,
            size_hint=(0.85, 0.75),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        
        # Judul
        title = Label(
            text="DASHBOARD ADMIN", 
            font_size=100,
            bold=True,
            color=(0.8, 0.5, 0.7, 0.8),  # Pink sama dengan button
            size_hint=(1, 0.3)
        )
        content.add_widget(title)
        
        # Menu buttons yang bisa diklik (sama seperti "Kembali")
        menus = [
            ("Kelola Tugas", self.kelola_tugas),
            ("Kelola Mahasiswa", self.kelola_mahasiswa), 
            ("Lihat Tugas", self.lihat_tugas),
            ("Export Excel", self.export_excel),
            ("Cek Deadline", self.cek_deadline),
            ("Backup Data", self.backup_data),
            ("Logout", self.logout)
        ]
        
        for text, command in menus:
            # Buat button dengan style sama seperti "Kembali"
            menu_btn = Button(
                text=text,
                font_size=20,
                bold=True,
                background_color=(0.8, 0.5, 0.7, 0.8),  # Pink transparan SAMA
                color=(1, 1, 1, 1),  # Teks putih SAMA
                background_normal='',
                size_hint=(1, 0.08)
            )
            
            # Tambahkan efek hover
            def make_hover(btn):
                original = (0.8, 0.5, 0.7, 0.8)
                hover = (0.9, 0.6, 0.8, 0.9)
                
                def on_enter(instance):
                    btn.background_color = hover
                
                def on_leave(instance):
                    btn.background_color = original
                
                return on_enter, on_leave
            
            on_enter_func, on_leave_func = make_hover(menu_btn)
            menu_btn.bind(on_enter=on_enter_func)
            menu_btn.bind(on_leave=on_leave_func)
            
            # Bind click event
            menu_btn.bind(on_press=command)
            
            content.add_widget(menu_btn)
        
        main_layout.add_widget(content)
        return main_layout
    
    # Fungsi-fungsi untuk button
    def go_back(self, instance):
        print("Tombol Kembali ditekan")
    
    def kelola_tugas(self, instance):
        print("Kelola Tugas ditekan")
    
    def kelola_mahasiswa(self, instance):
        print("Kelola Mahasiswa ditekan")
    
    def lihat_tugas(self, instance):
        print("Lihat Tugas ditekan")
    
    def export_excel(self, instance):
        print("Export Excel ditekan")
    
    def cek_deadline(self, instance):
        print("Cek Deadline ditekan")
    
    def backup_data(self, instance):
        print("Backup Data ditekan")
    
    def logout(self, instance):
        print("Logout ditekan")
        App.get_running_app().stop()

if __name__ == '__main__':
    DashboardAdmin().run()