import os
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(ctk.CTk):
    title_txt = """\
    \t    __________________________________________________________________________________________________________________
    \t     ____________/\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\__/\\\\\\\\\\\\_____________________________________________________________________________
    \t      ___________\\/\\\\\\///////////__\\////\\\\\\_____________________________________________________________________________
    \t       ___________\\/\\\\\\________________\\/\\\\\\_______/\\\\\\__/\\\\\\_______________/\\\\\\_________________________________________
    \t        ___________\\/\\\\\\\\\\\\\\\\\\\\\\________\\/\\\\\\______\\//\\\\\\/\\\\\\___/\\\\\\\\\\\\\\\\\\\\_\\///___/\\\\\\____/\\\\\\____/\\\\\\\\\\__/\\\\\\\\\\_________
    \t         ___________\\/\\\\\\///////_________\\/\\\\\\_______\\//\\\\\\\\\\___\\/\\\\\\//////___/\\\\\\_\\/\\\\\\___\\/\\\\\\__/\\\\\\///\\\\\\\\\\///\\\\\\_______
    \t          ___________\\/\\\\\\________________\\/\\\\\\________\\//\\\\\\____\\/\\\\\\\\\\\\\\\\\\\\_\\/\\\\\\_\\/\\\\\\___\\/\\\\\\_\\/\\\\\\_\\//\\\\\\__\\/\\\\\\_______
    \t           ___________\\/\\\\\\________________\\/\\\\\\_____/\\\\_/\\\\\\_____\\////////\\\\\\_\\/\\\\\\_\\/\\\\\\___\\/\\\\\\_\\/\\\\\\__\\/\\\\\\__\\/\\\\\\_______
    \t            ___________\\/\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\__/\\\\\\\\\\\\\\\\\\_\\//\\\\\\\\/_______/\\\\\\\\\\\\\\\\\\\\_\\/\\\\\\_\\//\\\\\\\\\\\\\\\\\\__\\/\\\\\\__\\/\\\\\\__\\/\\\\\\_______
    \t             ___________\\///////////////__\\/////////___\\////________\\//////////__\\///___\\/////////___\\///___\\///___\\///________
    \t              _____________/\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\______________________________/\\\\\\\\\\\\________________________________________________
    \t               ____________\\///////\\\\\\/////______________________________\\////\\\\\\________________________________________________
    \t                __________________\\/\\\\\\______________________________________\\/\\\\\\________________________________________________
    \t                 __________________\\/\\\\\\___________/\\\\\\\\\\________/\\\\\\\\\\_______\\/\\\\\\_____/\\\\\\\\\\\\\\\\\\\\________________________________
    \t                  __________________\\/\\\\\\_________/\\\\\\///\\\\\\____/\\\\\\///\\\\\\_____\\/\\\\\\____\\/\\\\\\//////_________________________________
    \t                   __________________\\/\\\\\\________/\\\\\\__\\//\\\\\\__/\\\\\\__\\//\\\\\\____\\/\\\\\\____\\/\\\\\\\\\\\\\\\\\\\\________________________________
    \t                    __________________\\/\\\\\\_______\\//\\\\\\__/\\\\\\__\\//\\\\\\__/\\\\\\_____\\/\\\\\\____\\////////\\\\\\________________________________
    \t                     __________________\\/\\\\\\________\\///\\\\\\\\\\/____\\///\\\\\\\\\\/____/\\\\\\\\\\\\\\\\\\__/\\\\\\\\\\\\\\\\\\\\________________________________
    \t                      __________________\\///___________\\/////________\\/////_____\\/////////__\\//////////_________________________________
    \t                       __________________________________________________________________________________________________________________\
    \n\n"""

    def __init__(self):
        super().__init__()

        # application bindings
        # self.bind("<Configure>", self.resized)

        # configure window
        self.title("IBM Testing Tools - vMin")
        self.geometry(f"{1100}x{580}")
        self.minsize(600, 400)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./")
        logo_x, logo_y = Image.open(os.path.join(image_path, 'ibm_light.png')).size

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1), weight=1)


        # create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.ibm_logo = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, 'ibm_light.png')),
                                     dark_image=Image.open(os.path.join(image_path, 'ibm_grey.png')),
                                     size=(logo_x//4, logo_y//4))
        self.ibm_logo_frame = ctk.CTkLabel(self.sidebar_frame, text="", image=self.ibm_logo)
        self.ibm_logo_frame.grid(row=0, column=0, padx=10, pady=10)

        #

        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_option_e_menu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                               command=self.change_appearance_mode_event)
        self.appearance_mode_option_e_menu.grid(row=6, column=0, padx=20, pady=(0, 10))

        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_option_e_menu = ctk.CTkOptionMenu(self.sidebar_frame,
                                                       values=["50%", "80%", "100%", "120%", "150%", "200%"],
                                                       command=self.change_scaling_event)
        self.scaling_option_e_menu.grid(row=8, column=0, padx=20, pady=(0, 20))


        # create entry box and main button
        self.entry = ctk.CTkEntry(self, placeholder_text="enter manual command")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(10, 20), sticky="nsew")
        self.main_button_1 = ctk.CTkButton(master=self, fg_color="transparent", border_width=2,
                                           text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(10, 20), sticky="nsew")

        # create display textbox
        self.textbox = ctk.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, rowspan=2, columnspan=3, padx=(20, 20), pady=(20, 0), sticky="nsew")

        # create slider and progressbar frame
        self.slider_progressbar_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=2, column=1, columnspan=3, padx=(20, 20), pady=(0, 0), sticky="nsew")
        self.slider_progressbar_frame.columnconfigure(0, weight=1)
        self.progressbar_1 = ctk.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 0), sticky="nsew")


        # set default values
        self.appearance_mode_option_e_menu.set("Dark")
        self.scaling_option_e_menu.set("100%")

        self.textbox.insert("0.0", self.title_txt)
        self.textbox.configure(state="disabled")

        self.progressbar_1.configure(mode="indeterminnate")

        self.main_button_1.configure(text='execute')
        self. main_button_1.configure(command=self.execute_button_event)
        # self.textbox.configure(state="disabled")

    # noinspection PyMethodMayBeStatic
    def open_input_dialog_event(self):
        dialog = ctk.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    # noinspection PyMethodMayBeStatic
    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    # noinspection PyMethodMayBeStatic
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def execute_button_event(self):
        cli_command = self.entry.get()
        self.textbox.configure(state="normal")
        if cli_command:
            self.textbox.insert(ctk.END, cli_command)
        else:
            self.textbox.insert(ctk.END, 'Lorem Ipsum ')
        self.textbox.configure(state="disabled")

        # print(self.textbox.__dict__)
        if not self.progressbar_1.__dict__['_loop_running']:
            self.progressbar_1.start()
        else:
            self.progressbar_1.stop()

    # noinspection PyMethodMayBeStatic
    def resized(self, winfo):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
