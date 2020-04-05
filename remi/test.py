
import remi.gui as gui
from remi import start, App
from Jumpscale.core.InstallTools import *
import threading
import time

class MyTextBox(gui.TextInput):
    def __init__(self, **kwargs):
        super(MyTextBox, self).__init__( **kwargs)
        self.lines=[]
        self.style['margin'] = 'auto'        

        self.log("""
        a
        b
        c
        d
        """)


    def trigger(self,app):
        self.text

    def log(self,line):
        line=str(line)
        if "\n" in line:
            for l in line.split("\n"):
                self.log(l.strip())
        elif line.strip()=="":
            return
        else:
            if len(self.lines)>20:
                self.lines.pop(0)
            self.lines.append(line)
        text="\n".join(self.lines)
        self.set_text(text)


class Table2(gui.Table):
    def __init__(self, **kwargs):

        super(Table2, self).__init__(**kwargs)

        self.width=300
        self.height=200
        self.margin='10px'

        self.rows=[('ID', 'First Name', 'Last Name'),
                ('101', 'Danny', 'Young'),
                ('102', 'Christine', 'Holand'),
                ('103', 'Lars', 'Gordon'),
                ('104', 'Roberto', 'Robitaille'),
                ('105', 'Maria', 'Papadopoulos')]

        # self.append_from_list(*, fill_title=True)
        self.append_from_list(self.rows, fill_title=True)


        # import pudb; pu.db

    def idle(self):
        print(1)
        

    # api function
    def api_set_text(self, value1, value2):
        self.rows.append(('106', 'ddd', 'dddddd'))
        self.append_from_list(self.rows, fill_title=True)
        # import pudb; pu.db
        headers = {'Content-type': 'text/plain'}
        return ['OK', headers]


class Menu(gui.Menu):

    def __init__(self, root, **kwargs):
        self.root = root

        super(Menu, self).__init__(**kwargs)
        self.width = 620
        self.height = 30

        m1 = gui.MenuItem('File', width=100, height=30)
        m11 = gui.MenuItem('Save', width=100, height=30)
        m12 = gui.MenuItem('Open', width=100, height=30)
        m12.onclick.do(self.menu_open_clicked)
        m111 = gui.MenuItem('Save', width=100, height=30)
        m111.onclick.do(self.menu_save_clicked)
        m112 = gui.MenuItem('Save as', width=100, height=30)
        m112.onclick.do(self.menu_saveas_clicked)

        self.append(m1)
        m1.append(m11)
        m1.append(m12)
        m11.append(m111)
        m11.append(m112)

    def menu_open_clicked(self, widget):
        self.fileselectionDialog = gui.FileSelectionDialog('File Selection Dialog', 'Select an image file', False, '.')
        self.fileselectionDialog.confirm_value.do(
            self.on_image_file_selected)
        self.fileselectionDialog.cancel_dialog.do(
            self.on_dialog_cancel)
        # here is shown the dialog as root widget
        self.fileselectionDialog.show(self)

    def menu_save_clicked(self, widget):
        pass
        
    def menu_saveas_clicked(self, widget):
        pass

    def on_image_file_selected(self, widget, file_list):
        if len(file_list) < 1:
            return
        self.image_widget.load(file_list[0])
        # self.root.set_root_widget(self.root.main)
    
    def on_dialog_cancel(self, widget):
        self.root.set_root_widget(self.root.main)



class MyApp(App):
    # def __init__(self, *args):
    #     self.text=""
    #     super(MyApp, self).__init__(*args)
        
    def idle(self):
        #this function is called automatically by remi library at specific interval
        # so here I can assign values to widget
        # self.lbl.trigger()
        pass

    def add(self,name,item):
        self.__dict__[name]=item
        self.main.append(item)

    def init(self):
        self.width=1100
        self.height=800
        self.main = gui.Container(width=self.width,height=self.height, margin='0px auto', style={'display': 'block', 'overflow': 'hidden'})

        #add the following 3 lines to your app and the on_window_close method to make the console close automatically
        tag = gui.Tag(_type='script')
        tag.add_child("javascript", """window.onunload=function(e){sendCallback('%s','%s');return "close?";};""" % (str(id(self)), "on_window_close")) 
        self.main.add_child("onunloadevent", tag)


    def main(self):

        self.init()

        horizontalContainer = gui.Container(width='100%', layout_orientation=gui.Container.LAYOUT_HORIZONTAL, 
                    margin='0px', style={'display': 'block', 'overflow': 'auto'})
        
        subContainerLeft = gui.Container(width=self.width/2,height=self.height/2, style={'display': 'block', 'overflow': 'auto', 'text-align': 'center'})
        subContainerRight = gui.Container(width=self.width/2,height=self.height/2, style={'display': 'block', 'overflow': 'auto', 'text-align': 'center'})
        
        self.img = gui.Image('/res:logo.png', height=100, margin='10px')


        # self.add("logger",MyTextBox(width='80%', height='100%',single_line=False))
        self.add("menu",Menu(root=self,width = self.width,height=30))
        self.main.append(horizontalContainer)



        # self.table = Table2(attributes = {'id':'table'})

        #http://127.0.0.1:8082/table/api_set_text?value1=text1&value2=text2


        # appending a widget to another, the first argument is a string key
        # wid.append(self.table)

        self.thread_alive_flag = True
        
        #Here I start a parallel thread that executes my algorithm for a long time
        t = threading.Thread(target=self.my_intensive_long_time_algorithm)
        t.start()


        # returning the root widget
        return self.main



    def my_intensive_long_time_algorithm(self):
        i=1
        while self.thread_alive_flag:
            time.sleep(0.1)
            i+=1
            self.logger.log(i)

    def on_window_close(self):
        #here you can handle the unload
        self.thread_alive_flag = False
        print("app closing")
        self.close()



if __name__ == "__main__":
    # starts the webserver
    # optional parameters
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(MyApp, debug=True, address='127.0.0.1', port=8082)


#cd /Users/despiegk/code/1/remi/examples/;python3 test.py
