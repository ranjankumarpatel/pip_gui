import tkinter as tk
from tkinter import ttk

class WelcomePage(ttk.Frame):
    """
    Ask user about what to do :
    1. Install
    2. Uninstall or Update
    """

    def __init__(self, root, controller):
        ttk.Frame.__init__(self, root)
        self.parent = root
        self.controller = controller

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        self.container = ttk.Frame(self)
        self.container.grid(
            row=0,
            column=1,
            sticky='nsew',
            padx=(1,1),
            pady=(1,1))
        self.container.columnconfigure(0, weight=1)
        self.container.rowconfigure(0, weight=1)
        self.create_welcome_page()

    def create_welcome_page(self):
        """
        Add content to welcome page and radio buttons for selecting among
        two tasks :

        1. Search and Install Package
        2. Manage already installed packages
        """

        #Create side frame
        self.side_frame = ttk.Frame(
            self.container,
            borderwidth=3,
            padding=0.5,
            relief='ridge')
        self.side_frame.grid(
            row=0,
            column=0,
            sticky='nsw',
            pady=(1,1),
            padx=(1,1))
        self.side_frame.rowconfigure(0, weight=1)
        #self.side_frame.columnconfigure(0, weight=1)

        #Insert appropriate image in left side in side frame
        '''
        import base64
        import os
        import pkg_resources
        resource_package = __name__
        resource_path = os.path.join('sideimage.gif')
        data = pkg_resources.resource_string(resource_package, resource_path)
        side_image = base64.b64encode(data)
        s1 = tk.PhotoImage('side_image', data=side_image)
        self.side_label = tk.Label(self.side_frame, image='side_image')
        '''
        #self.side_label.grid(row=0, column=0, sticky='nsew')

        #Create another child frame
        self.welcome_frame = ttk.Frame(
            self.container,
            borderwidth=3,
            padding=0.5,
            relief='ridge')
        self.welcome_frame.grid(
            row=0,
            column=1,
            sticky='nse',
            pady=(1,1),
            padx=(1,1))
        self.welcome_frame.rowconfigure(1, weight=1)

        #Create welcome text
        self.welcome_text = tk.StringVar()
        self.welcome_text.set("Welcome to GUI for PIP")
        self.welcome_label = tk.Label(
            self.welcome_frame,
            textvariable=self.welcome_text,
            font=('Helvetica',22,'bold'),
            justify='center',
            padx=20,
            pady=20)
        self.welcome_label.grid(
            row=0,
            column=0,
            sticky='nwe',
            pady=(5,10),
            padx=(1,1))

        #Create labelled frame for option
        self.options_frame = tk.LabelFrame(
            self.welcome_frame,
            text='Do you want to :',
            font=('Helvetica',16),
            padx=5,
            pady=5)
        self.options_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky='nwe',
            padx=(4,1),
            pady=(8,2))
        self.options_frame.rowconfigure(0, weight=1)

        #Create radio buttons
        self.radio_var = tk.IntVar()
        self.radio_var.set(1)
        self.first_button = tk.Radiobutton(
            self.options_frame,
            text='Search and Install Packages',
            font=('Helvetica',10),
            wraplength=300,
            variable=self.radio_var,
            value=1,
            justify='left')
        self.first_button.grid(row=0, column=0, pady=(35,10), sticky='w')
        self.second_button = tk.Radiobutton(
            self.options_frame,
            text='Manage Installed Packages (Update/Uninstall)',
            font=('Helvetica',10),
            wraplength=300,
            variable=self.radio_var,
            value=2,
            justify='left')
        self.second_button.grid(row=1, column=0, pady=(10,35), sticky='w')

        #Create 'next' navigation button
        self.next_button = ttk.Button(
            self.options_frame,
            text='Next',
            command=lambda: self.navigate_next_frame())
        self.next_button.grid(row=2, column=1, sticky='se')

    def navigate_next_frame(self):
        """
        Navigate to next frame in response to event generated by the next
        button
        """

        if self.radio_var.get()==1:
            self.controller.show_frame('InstallPage')

        elif self.radio_var.get()==2:
            self.controller.show_frame('ManageInstalledPage')

if __name__ == "__main__":

    # If you want to check GUI
    root = tk.Tk()
    # root.resizable(width='false', height='false')
    welcome_app = WelcomePage(root)
    root.mainloop()
