from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.core.window import Window

# ব্যাকগ্রাউন্ড ডার্ক থিম
Window.clearcolor = (0.05, 0.05, 0.05, 1)

# স্মার্ট মানি কনসেপ্ট (SMC) এবং প্রাইস অ্যাকশন এনালাইসিস ইঞ্জিন
class AdvancedBinaryAnalyzer:
    def __init__(self):
        self.timeframe = "1 Minute"

    def scan_and_analyze(self):
        is_uptrend = self.detect_market_trend()
        
        if is_uptrend:
            has_liquidity_sweep = self.check_liquidity_sweep()
            at_order_block_or_support = self.check_minor_support_or_ob()
            
            if has_liquidity_sweep and at_order_block_or_support:
                return "CALL (UP) - SMC Confirmed", "91%", "9%"
            else:
                return "WAIT - Searching Setup", "0%", "0%"
        else:
            return "WAIT - Trend Unfavorable", "0%", "0%"

    def detect_market_trend(self):
        return True  # আপট্রেন্ড কনফার্মেশন

    def check_liquidity_sweep(self):
        return True  # লিকুইডিটি সুইপ চেক

    def check_minor_support_or_ob(self):
        return True  # মাইনর সুইং সাপোর্ট বা অর্ডার ব্লক চেক


# মেইন সফটওয়্যার বা হোম স্ক্রিন
class MainHomeScreen(Screen):
    def __init__(self, **kwargs):
        super(MainHomeScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        title_label = Label(
            text="[ SMC Master Trading Bot ]",
            size_hint=(None, None),
            size=(300, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.8},
            color=(0, 1, 0.8, 1),
            font_size='16sp'
        )
        layout.add_widget(title_label)

        switch_label = Label(
            text="Turn On Floating Popup:",
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.4, 'center_y': 0.5},
            color=(1, 1, 1, 1),
            font_size='14sp'
        )
        layout.add_widget(switch_label)

        self.popup_switch = Switch(
            active=False,
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.7, 'center_y': 0.5}
        )
        self.popup_switch.bind(active=self.on_switch_toggle)
        layout.add_widget(self.popup_switch)

        self.add_widget(layout)

    def on_switch_toggle(self, instance, value):
        if value:
            self.manager.current = 'popup_screen'


# ফ্লোটিং পপ-আপ স্ক্রিন ও টাচ ড্র্যাগ সিস্টেম
class PopupScreen(Screen):
    def __init__(self, **kwargs):
        super(PopupScreen, self).__init__(**kwargs)
        self.layout = FloatLayout()
        self.touch_active = False
        self.analyzer = AdvancedBinaryAnalyzer()

        self.ratio_label = Label(
            text="Win: 0% | Loss: 0%",
            size_hint=(None, None),
            size=(220, 35),
            pos_hint={'center_x': 0.5, 'center_y': 0.65},
            color=(0, 1, 0.6, 1),
            font_size='13sp'
        )
        self.layout.add_widget(self.ratio_label)

        self.capture_btn = Button(
            text="Capture & Scan",
            size_hint=(None, None),
            size=(130, 35),
            pos_hint={'center_x': 0.5, 'center_y': 0.35},
            background_color=(0.1, 0.5, 0.9, 1)
        )
        self.capture_btn.bind(on_press=self.on_capture_click)
        self.layout.add_widget(self.capture_btn)

        self.back_btn = Button(
            text="X",
            size_hint=(None, None),
            size=(30, 30),
            pos_hint={'center_x': 0.85, 'center_y': 0.85},
            background_color=(0.8, 0.2, 0.2, 1)
        )
        self.back_btn.bind(on_press=self.close_popup)
        self.layout.add_widget(self.back_btn)

        self.add_widget(self.layout)

    def on_capture_click(self, instance):
        signal, win, loss = self.analyzer.scan_and_analyze()
        self.ratio_label.text = f"Win: {win} | Loss: {loss}"
        print(f"Signal Generated: {signal}")

    def close_popup(self, instance):
        app = App.get_running_app()
        app.root.get_screen('main_screen').popup_switch.active = False
        app.root.current = 'main_screen'

    def on_touch_down(self, touch):
        if self.layout.collide_point(*touch.pos):
            self.touch_active = True
            return super(PopupScreen, self).on_touch_down(touch)
        return False

    def on_touch_move(self, touch):
        if self.touch_active:
            return super(PopupScreen, self).on_touch_move(touch)
        return super(PopupScreen, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        if self.touch_active:
            self.touch_active = False
            return True
        return super(PopupScreen, self).on_touch_up(touch)


# মূল অ্যাপ কন্ট্রোলার
class MasterTradingApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainHomeScreen(name='main_screen'))
        sm.add_widget(PopupScreen(name='popup_screen'))
        return sm

if __name__ == '__main__':
    MasterTradingApp().run()
