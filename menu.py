#menu.py python code and menu.kv kivy code
from kivy.uix.relativelayout import RelativeLayout


class MenuWidget(RelativeLayout):
    def on_touch_down(self, touch):
        if self.opacity == 0:
            return False
        return super(RelativeLayout, self).on_touch_down(touch)
    pass
    
    
  -------------------------------------------------------------------------------
 #menu.kv


<MenuWidget>:
    canvas.before:
        Color:
            rgba: 0, 0, 0, .8
        Rectangle:
            size: self.size
    Label:
        font_size: dp(80)
        font_name: 'fonts/lcd/LCD Normal.ttf'
        text: root.parent.menu_title
        pos_hint: {"center_x": .5, "center_y": .6}

    Label:
        font_size: dp(30)from kivy.uix.relativelayout import RelativeLayout


class MenuWidget(RelativeLayout):
    def on_touch_down(self, touch):
        if self.opacity == 0:
            return False
        return super(RelativeLayout, self).on_touch_down(touch)
    pass


        font_name: 'fonts/lcd/LCD2B___.TTF'
        text: ' G   A   L   A   X   Y '
        size_hint: 1, 1
        pos_hint: { "down": 1, "x": 0}


    Button:
        font_size: dp(30)
        font_name: 'fonts/lcd/LCD2B___.TTF'
        text: root.parent.menu_button_title
        pos_hint: {"center_x": .5, "center_y": .3}
        size_hint: .2, .15
        on_press: root.parent.on_menu_button_pressed()
        background_normal: ''
        background_color: 1, .3, .4, .85
