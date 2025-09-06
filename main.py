import requests
import qrcode
from io import BytesIO
from kivy.core.image import Image as CoreImage
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton

URL = "https://edu.donstu.ru/api/UserInfo/PassGeneration"

HEADERS = {
    "accept": "*/*",
    "authorization": "Bearer ВАШ_BEARER_ТОКЕН",
    "user-agent": "Mozilla/5.0",
    "referer": "https://edu.donstu.ru/WebApp/"
}

COOKIES = {
    "ASP.NET_SessionId": "ВАШ_SESSIONID",
    "authToken": "ВАШ_AUTH_TOKEN"
}


class QRPassApp(MDApp):
    def build(self):
        self.layout = BoxLayout(orientation="vertical")
        self.qr_image = Image(size_hint=(1, 0.9))
        self.button = MDRaisedButton(
            text="Обновить QR", size_hint=(1, 0.1), on_release=self.update_qr
        )

        self.layout.add_widget(self.qr_image)
        self.layout.add_widget(self.button)

        self.update_qr(None)
        return self.layout

    def update_qr(self, instance):
        try:
            resp = requests.get(URL, headers=HEADERS, cookies=COOKIES)
            if resp.status_code == 200:
                token = str(resp.json().get("data"))

                qr = qrcode.QRCode(box_size=10, border=2)
                qr.add_data(token)
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")

                buf = BytesIO()
                img.save(buf, format="PNG")
                buf.seek(0)
                core_img = CoreImage(buf, ext="png")
                self.qr_image.texture = core_img.texture

                self.button.text = f"QR: {token}"
            else:
                self.button.text = f"Ошибка {resp.status_code}"
        except Exception as e:
            self.button.text = f"Ошибка: {e}"


if __name__ == "__main__":
    QRPassApp().run()
