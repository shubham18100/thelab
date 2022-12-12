from kivy.app import App 
from kivy.uix.image import AsyncImage


class myapp(App):
    def build(self):
        return AsyncImage(source ='https://www.google.com/search?q=image&rlz=1C1CHBF_enIN962IN962&sxsrf=ALiCzsYQ_zayiUQ4fXW-3LIMuz0L-8WIug:1668577934911&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjvmdyYgbL7AhVITWwGHbRNC4MQ_AUoAXoECAIQAw&biw=1536&bih=722&dpr=1.25#imgrc=4POnWjbftJPE5M')

myapp().run()