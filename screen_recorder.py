from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.utils import platform
from plyer import screenrecorder
import os

class ScreenRecorderApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.start_button = Button(text="Начать запись", on_press=self.start_recording)
        self.stop_button = Button(text="Остановить запись", on_press=self.stop_recording, disabled=True)

        layout.add_widget(self.start_button)
        layout.add_widget(self.stop_button)

        return layout

    def start_recording(self, instance):
        if platform == 'android':
            save_path = os.path.join('/storage/emulated/0/Download', 'screen_record.mp4')
            screenrecorder.start(save_path)
            self.start_button.disabled = True
            self.stop_button.disabled = False

    def stop_recording(self, instance):
        if platform == 'android':
            screenrecorder.stop()
            self.start_button.disabled = False
            self.stop_button.disabled = True

if __name__ == "__main__":
    ScreenRecorderApp().run()
