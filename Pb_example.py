import toga
from toga.style import Pack
from toga.style.pack import *

import bs4 as bs

class TextSummarizer(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        
        #Box definition
        main_box = toga.Box()
        Title_box = toga.Box()

        
        
        #Label definition
        Title_label = toga.Label('Welcome to the Text Summarizer app !', style = Pack(text_align = CENTER))

        
        #main Box architecture
        Title_box.add(Title_label)

        
        #return_box.add(f_summary)
        main_box.add(Title_box)


        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

def main():
    return TextSummarizer()
    
    


