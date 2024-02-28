# This program is free software: you can redistribute it and/or modify it under the terms of the license, subject to the author's approval.
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


# 这个程序是自由软件，你可以经作者同意后重新发布和/或修改它
# 根据自由软件基金会发布的GNU通用公共许可证的规定，
# 不论是该许可证的第3版或者是之后的版本。

# 这个程序是基于免责条款发布的，我们提供的软件没有任何担保，
# 也没有隐含的担保条件，包括但不限于适销性或特定用途适用性的担保。
# 有关更多详情，请参阅GNU通用公共许可证。

# 你应该已经收到了GNU通用公共许可证的副本，
# 如果没有，请参阅 <https://www.gnu.org/licenses/>。

# e-mail : mcyyds1145141919810@outlook.com
# QQ : 2940206071

# Copyright (c) 2023, 2024 POINT Org. All Rights Reserved.

import os
from os import name as osname
from os import system
from sys import exit as exit_

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import ttk

from shutil import rmtree

from PIL import Image 
from PIL import ImageTk

from SuperDelSoftwareTemsOfUse import SOFTWARETERMSOFUSE
from SuperDelSoftwareTemsOfUse import USERGUIDE


VERSION = 'Version 1.1.3' # 每次更新记得改


class Windows:
    def __init__(self, master):
        self.master = master
        self.master.title('Super_Deleter')
        self.master.geometry('900x800')
        self.master.configure(bg='#0078D7')
 

        # 创建菜单栏
        self.menu_bar = tk.Menu(self.master)

        # 创建文件处理类实例
        self.file_handler = FileHandler(self.master)
        self.view_handler = ViewHandler(self.master)
        self.help_handler = HelpHandler(self.master)
        self.deldisplay = DelDisplay(self.master)
        self.delhander = DelHander(self.master)
        self.option = Option(self.master)
        self.thanks = Thanks(self.master)
        self.gnuv3 = ShowGNUv3(self.master)

        # 创建文件菜单
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label='打开(Open)     ', command=self.file_handler.open_file)
        file_menu.add_separator()
        
        # 创建删除子菜单
        del_sub_menu = tk.Menu(file_menu, tearoff=0)
        del_keyword_menu = tk.Menu(file_menu, tearoff=0)
        del_sub_keyword_menu1 = tk.Menu(file_menu, tearoff=0)
        del_sub_keyword_menu1.add_command(label='递归子目录(包括子目录)', command=self.deldisplay.d_1)
    
        del_sub_keyword_menu1.add_command(label='不递归子目录(不包括子目录)', command=self.deldisplay.d_2)
        del_sub_keyword_menu2 = tk.Menu(file_menu, tearoff=0)
        del_sub_keyword_menu2.add_command(label='递归子目录(包括子目录)', command=self.deldisplay.d_3)
        del_sub_keyword_menu2.add_command(label='不递归子目录(不包括子目录)', command=self.deldisplay.d_4)
        del_keyword_menu.add_cascade(label='删除文件名包含关键词的文件', menu=del_sub_keyword_menu1)
        del_keyword_menu.add_cascade(label='删除文件名不包含关键词的文件', menu=del_sub_keyword_menu2)
        del_sub_menu.add_cascade(label='按关键词删除  ', menu=del_keyword_menu)
        del_extension_menu = tk.Menu(file_menu, tearoff=0)
        del_sub_extension_menu1 = tk.Menu(file_menu, tearoff=0)
        del_sub_extension_menu1.add_command(label='递归子目录(包括子目录)', command=self.deldisplay.d_5)
        del_sub_extension_menu1.add_command(label='不递归子目录(不包括子目录)', command=self.deldisplay.d_6)
        del_sub_extension_menu2 = tk.Menu(file_menu, tearoff=0)
        del_sub_extension_menu2.add_command(label='递归子目录(包括子目录)', command=self.deldisplay.d_7)
        del_sub_extension_menu2.add_command(label='不递归子目录(不包括子目录)', command=self.deldisplay.d_8)
        del_extension_menu.add_cascade(label='删除指定后缀文件', menu=del_sub_extension_menu1)
        del_extension_menu.add_cascade(label='删除非指定后缀文件', menu=del_sub_extension_menu2)
        del_sub_menu.add_cascade(label='按文件后缀删除', menu=del_extension_menu)

        file_menu.add_cascade(label='SuperDeleter         ', menu=del_sub_menu)
        del_sub_menu.add_command(label='删除选定文件(夹)    ', command=self.delhander.delete_one_file_or_folder)
        file_menu.add_separator()
        file_menu.add_command(label='退出(Exit)     ', command=self.exit_app)

        # 创建视图菜单
        view_menu = tk.Menu(self.menu_bar, tearoff=0)
        view_menu.add_command(label='全屏模式(Fullscreen)       ', command=self.view_handler.view_fullscreen)
        view_menu.add_command(label='视窗模式(Windows)          ', command=self.view_handler.view_windows_mode)
        view_menu.add_command(label='刷新(update)              ', command=self.update)

        # 创建帮助菜单
        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label='查看帮助(For help)     ', command=self.help_handler.show_help)
        help_menu.add_command(label='反馈                   ', command=self.option.UesrsReturn)

        # 创建关于菜单
        option_menu = tk.Menu(self.menu_bar, tearoff=0)
        option_menu.add_command(label='关于Super_Deleter     ', command=self.option.init)
        option_menu.add_command(label='鸣谢                  ', command=self.thanks.init)
        option_menu.add_command(label='查看GNU通用公共许可协议', command=self.gnuv3.init)

        # 将文件、视图、帮助菜单添加到菜单栏
        self.menu_bar.add_cascade(label='文件(File)', menu=file_menu)
        self.menu_bar.add_cascade(label='视图(View)', menu=view_menu)
        self.menu_bar.add_cascade(label='帮助(Help)', menu=help_menu)
        self.menu_bar.add_cascade(label='关于(Option)', menu=option_menu)

        # 将菜单栏配置到主窗口
        self.master.config(menu=self.menu_bar)
        self.init_explorer('/home') if osname != 'nt' else self.init_explorer('C:\\Users\\')


    def exit_app(self):
        result = messagebox.askquestion('退出', '是否结束本次会话?')
        if result == 'yes':
            self.master.destroy()
    
    # 创建文件浏览器
    def init_explorer(self, folder_path):
        self.tree = ttk.Treeview(self.master)
        self.tree['columns'] = ('full_path',)
        self.tree.heading('#0', text='您将操作这些文件/文件夹')
        self.tree.column('#0', width=200)
        self.tree.heading('full_path', text='完整路径')
        self.tree.column('full_path', width=400)
        
        self.folder_path = folder_path

        self.show_folder_contents(self.folder_path)
        

        self.tree.bind('<Double-1>', self.on_double_click)
        self.tree.bind('<ButtonRelease-1>', self.on_item_click)

        self.tree.pack(expand=True, fill='both')


    def show_folder_contents(self, folder_path):
        try:
            self.tree.delete(*self.tree.get_children())
            self.folder_path_out = folder_path
            print(folder_path)
            if folder_path != '/':
                self.tree.insert('', 'end', text='..', values=(os.path.abspath(os.path.join(folder_path, '..')),))
            files = os.listdir(folder_path)
            for item in files:
                full_path = os.path.join(folder_path, item)
                if os.path.isdir(full_path):
                    self.tree.insert('', 'end', text=item, values=(full_path,))
                elif os.path.isfile(full_path):
                    self.tree.insert('', 'end', text=item, values=(full_path,))
        except PermissionError:
            if osname != 'nt':
                messagebox.showerror('权限不足', '如果你要访问这些文件,并且明白操作这些文件的后果,请用root用户打开')
            else:
                messagebox.showerror('权限不足', '如果你要访问这些文件,并且明白操作这些文件的后果,请用管理员用户打开')

    # 监测单击事件
    def on_item_click(self, event):
        item_id = self.tree.selection()
        if item_id:
            item_id = item_id[0]
            item_values = self.tree.item(item_id, 'values')
            if item_values:
                selected_file = item_values[0]
                self.sf = selected_file
                print(f'选中文件： {selected_file}')

    # 监测双击事件
    def on_double_click(self, event):
        item_id = self.tree.selection()
        if item_id:
            item_id = item_id[0]
            item_values = self.tree.item(item_id, 'values')
            if item_values:
                selected_item = item_values[0]
                if os.path.isdir(selected_item):
                    self.show_folder_contents(selected_item)
                else:
                    print(f'打开文件： {selected_item}')
                    system(selected_item)
    

    def update(self):
        self.show_folder_contents(self.folder_path_out)

    
class FileHandler:
    def __init__(self, master):
        self.master = master


    def open_file(self):
        self.file_path = filedialog.askdirectory(title='选择操作文件夹')
        if self.file_path:
            try:
                software.tree.destroy()
                print(self.file_path)
                software.init_explorer(self.file_path)
            except PermissionError:
                messagebox.showerror('Error', '无权访问文件！')
            except Exception as e:
                messagebox.showerror('Error', f'没有定义的错误{e}')


class ViewHandler:
    def __init__(self, master):
        self.master = master


    def view_fullscreen(self):
        if self.master.attributes('-fullscreen'):
            messagebox.showinfo('提示', '已处于全屏状态')
        else:
            self.master.attributes('-fullscreen', True)


    def view_windows_mode(self):
        if self.master.attributes('-fullscreen'):
            self.master.attributes('-fullscreen', False)
        else:
            messagebox.showinfo('提示', '已处于窗口状态')


class HelpHandler:
    def __init__(self, master):
        self.master = master

    def show_help(self):
        ug = tk.Tk()
        user_guide = UserGuide(ug, '继续', ug.destroy, USERGUIDE, '取消')
        ug.mainloop()


class DelHander:
    def __init__(self, root_dir):
        self.root_dir = root_dir


    def _delete_files_with_extension(self, extension, include_subfolders=True, exclude=False):
        for root, dirs, files in os.walk(self.root_dir):
            if not include_subfolders:
                dirs.clear()
            for file in files:
                file_path = os.path.join(root, file)
                if file.endswith(extension) != exclude:
                    os.remove(file_path)
                    print(f'Deleted file: {file_path}')

    def delete_files_with_extension_including_subfolders(self, extension):
        self._delete_files_with_extension(extension)


    def delete_files_with_extension_excluding_subfolders(self, extension):
        self._delete_files_with_extension(extension, include_subfolders=False)


    def delete_files_without_extension_including_subfolders(self, extension):
        self._delete_files_with_extension(extension, exclude=True)


    def delete_files_without_extension_excluding_subfolders(self, extension):
        self._delete_files_with_extension(extension, include_subfolders=False, exclude=True)


    def _delete_files_by_filesname(self, keyword, include_subfolders=True, exclude=False):
        for root, dirs, files in os.walk(self.root_dir):
            if not include_subfolders:
                dirs.clear()  # 清空 dirs 列表,以停止 os.walk 递归到子目录
            for file in files:
                file_path = os.path.join(root, file)
                if (keyword in file) != exclude:
                    os.remove(file_path)
                    print(f'Deleted file: {file_path}')


    def delete_files_with_keyword_including_subfolders(self, keyword):
        self._delete_files_by_filesname(keyword)


    def delete_files_with_keyword_excluding_subfolders(self, keyword):
        self._delete_files_by_filesname(keyword, include_subfolders=False)


    def delete_files_without_keyword_including_subfolders(self, keyword):
        self._delete_files_by_filesname(keyword, exclude=True)


    def delete_files_without_keyword_excluding_subfolders(self, keyword):
        self._delete_files_by_filesname(keyword, include_subfolders=False, exclude=True)
    

    def delete_one_file_or_folder(self):
        rusult = messagebox.askokcancel('警告', '此操作为不可撤销永久的删除(真的很久),因此在执行之前请确保你真的想要删除这些文件!')
        if rusult:
            if os.path.isfile(software.sf):
                os.remove(software.sf)
                print(f'Deleted File:{software.sf}')
                messagebox.showinfo('成功', '文件操作操作成功')
                software.update()
            elif os.path.isdir(software.sf):
                rmtree(software.sf)
                print(f'Deleted File:{software.sf}')
                messagebox.showinfo('成功', '文件操作操作成功')
                software.update()
            else:
                messagebox.showerror('ERROR', '文件(夹)不存在')
                software.update()


class DelDisplay:
    def __init__(self, master):
        self.master = master

    def create_gui(self, title, description, action_func):
        
        try:
            window = tk.Toplevel(self.master)
            window.title(title)
            window.geometry('500x309')
            window.iconphoto(False, tk.PhotoImage(file='SuperDel.png'))

            tk.Label(window, text=description).pack()

            entry = tk.Entry(window)
            entry.pack()

            def handle_button_click():
                user_input = entry.get()

                    # 检查根目录路径是否已定义
                if not hasattr(software, 'folder_path_out'):
                    messagebox.showerror('错误', '未定义根目录路径！')
                    return
                
                rusult = messagebox.askokcancel('警告', '此操作为不可撤销永久的删除(真的很久),因此在执行之前请确保你真的想要删除这些文件!')
                if not rusult:
                    return

                try:
                    file_manipulator = DelHander(software.folder_path_out)
                    action_func(file_manipulator, user_input)
                    messagebox.showinfo('成功', '文件操作成功！')
                    software.update()
                except Exception as e:
                    messagebox.showerror('错误', f'执行文件操作时出错：{str(e)}')

            tk.Button(window, text='提交', command=handle_button_click).pack()

        except Exception as e:
            messagebox.showerror('错误', f'发生错误：{str(e)}')


    def d_1(self):
        self.create_gui(
    title='删除包括子目录中文件名包含关键词的文件',
    description='输入要搜索的文件名关键词：',
    action_func=lambda file_manipulator, 
    keyword: file_manipulator.delete_files_with_keyword_including_subfolders(keyword)
)


    def d_2(self):
        self.create_gui(
    title='删除不包括子目录中文件名包含关键词的文件',
    description='输入要搜索的文件名关键词：',
    action_func=lambda file_manipulator, 
    keyword: file_manipulator.delete_files_with_keyword_excluding_subfolders(keyword)
)
    

    def d_3(self):
        self.create_gui(
    title='删除包括子目录中文件名不包含关键词的文件',
    description='输入要避免的文件名关键词：',
    action_func=lambda file_manipulator, 
    keyword: file_manipulator.delete_files_without_keyword_including_subfolders(keyword)
)


    def d_4(self):
        self.create_gui(
    title='删除不包括子目录中文件名不包含关键词的文件',
    description='输入要避免的文件名关键词：',
    action_func=lambda file_manipulator, 
    keyword: file_manipulator.delete_files_without_keyword_excluding_subfolders(keyword)
)


    def d_5(self):
        self.create_gui(
    title='删除包括子目录中指定后缀名的文件',
    description='输入要删除文件的后缀名（包括点号）：',
    action_func=lambda file_manipulator, 
    extension: file_manipulator.delete_files_with_extension_including_subfolders(extension)
)
    

    def d_6(self):
        self.create_gui(
    title='删除不包括子目录中指定后缀名的文件',
    description='输入要删除文件的后缀名（包括点号）：',
    action_func=lambda file_manipulator, 
    extension: file_manipulator.delete_files_with_extension_excluding_subfolders(extension)
)
    

    def d_7(self):
        self.create_gui(
    title='删除包括子目录中没有指定后缀名的文件',
    description='输入要保留文件的后缀名（包括点号）：',
    action_func=lambda file_manipulator, 
    extension: file_manipulator.delete_files_without_extension_including_subfolders(extension)
)
        

    def d_8(self):
        self.create_gui(
    title='删除不包括子目录中没有指定后缀名的文件',
    description='输入要保留文件的后缀名（包括点号）：',
    action_func=lambda file_manipulator, 
    extension: file_manipulator.delete_files_without_extension_excluding_subfolders(extension)
)


class ShowGNUv3:
    def __init__(self, master):
        self.master = master
    

    def init(self):
        self.window = tk.Toplevel(self.master)
        self.window.title('GNUv3协议')
        self.scroll_txt = scrolledtext.ScrolledText(self.window, wrap=tk.WORD)
        self.scroll_txt.pack(fill=tk.BOTH, expand=True)
        self.scroll_txt.insert(tk.INSERT, gnu_3)
        self.scroll_txt.configure(state='disabled')
        self.window.overrideredirect(True)
        self.center_window(self.window)
        ok_button = tk.Button(self.window, text='ok', command=self.window.destroy)
        ok_button.pack(padx=10)
        cancel_button = tk.Button(self.window, text='cancel', command=exit_)
        cancel_button.pack(padx=10) 
    
    
    def center_window(self, window):
        window.update_idletasks()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        
        window_width = window.winfo_width()
        window_height = window.winfo_height()
        
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        window.geometry(f'+{x}+{y}')


class SoftwareTermsOfUse:
    def __init__(self, master, ok_buttom_text, ok_command, body_text, cancel_text):
        self.master = master 
        self.master.title('声明')
        self.scroll_txt = scrolledtext.ScrolledText(self.master, wrap=tk.WORD)
        self.scroll_txt.pack(fill=tk.BOTH, expand=True)
        self.scroll_txt.insert(tk.INSERT, body_text)
        self.scroll_txt.configure(state='disabled')
        self.master.overrideredirect(True)
        self.center_window(self.master)
        ok_button = tk.Button(self.master, text=ok_buttom_text, command=ok_command)
        ok_button.pack(padx=10)
        cancel_button = tk.Button(self.master, text=cancel_text, command=exit_)
        cancel_button.pack(padx=10) 


    def center_window(self, window):
        window.update_idletasks()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        
        window_width = window.winfo_width()
        window_height = window.winfo_height()
        
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        window.geometry(f'+{x}+{y}')


class UserGuide(SoftwareTermsOfUse):
    def __init__(self, master, ok_buttom_text, ok_command, body_text, cancel_text):
        super().__init__(master, ok_buttom_text, ok_command, body_text, cancel_text)
        self.master.title('用户指南')


class Option:
    def __init__(self, master):
        self.master = master 
        self.photo = None

    def init(self):
        window = tk.Toplevel(self.master)
        window.title('关于SuperDeleter')
        window.geometry('409x525')
        window.iconphoto(False, tk.PhotoImage(file='SuperDel.png'))

        tk.Label(window, text='SuperDeleter', font=('Verdana', 24)).pack()
        # 加载图片文件
        image = Image.open('SuperDel.png')
        self.photo = ImageTk.PhotoImage(image)

        # 获取图像的宽度和高度
        img_width, img_height = image.size

        # 创建一个标签，显示加载的图片
        label_i = tk.Label(window, image=self.photo)
        label_i.pack()
        self.center_image(window, img_width, img_height, label_i)

        tk.Label(window, text=f'''\n\n{VERSION}\n\n选择性删除文件程序\n\n遵循GNU GPL Version 3.0自由软件协议\n\n 详见http://www.gnu.org/licenses/ \n\n 本程序不含任何担保\n\n\n\n Copyright (c) 2023, 2024 POINT Org. All Rights Reserved.''').pack()
        window.bind('<Configure>', lambda event: self.center_image(window, img_width, img_height, label_i))
    

    def UesrsReturn(self):
        window = tk.Toplevel(self.master)
        window.title('反馈')
        window.geometry('409x309')
        window.iconphoto(False, tk.PhotoImage(file='SuperDel.png'))

        tk.Label(window, text='反馈到POINT团队', font=('Verdana', 24)).pack()
        # 加载图片文件
        image = Image.open('POINTLOGO.png')
        self.photo = ImageTk.PhotoImage(image)

        tk.Label(window, text='若有任何关于程序的问题, 欢迎访问QQ:2940206071\ne-mail:mcyyds1145141919810@outlook.com').pack()

        # 获取图像的宽度和高度
        img_width, img_height = image.size

        # 创建一个标签，显示加载的图片
        label_i = tk.Label(window, image=self.photo)
        label_i.pack()
        self.center_image(window, img_width, img_height, label_i)

        window.bind('<Configure>', lambda event: self.center_image(window, img_width, img_height, label_i))



    def center_image(self, window, img_width, img_height, label):
        window_width = window.winfo_width()
        window_height = window.winfo_height()
        y = window_height - img_height
        x = (window_width - img_width) // 2
        label.place(x=x, y=y)


class Thanks:
    def __init__(self, master):
        self.master = master 
    

    def init(self):
        window = tk.Toplevel(self.master)
        window.title('鸣谢')
        window.geometry('500x309')
        window.iconphoto(False, tk.PhotoImage(file='SuperDel.png'))
        tk.Label(window, text='鸣谢', font=('Verdana', 24)).pack()
        tk.Label(window, text='\n\n\n\n开发人员:XYG_Cat\n翻译:ChatGPT').pack()


def main():
    global software, gnu_3, config

    with open('COPYING', 'r', encoding='utf-8') as file:
        gnu_3 = file.read()

    root = tk.Tk()
    software_terms_of_use = SoftwareTermsOfUse(root, '我同意该协议  ', root.destroy, SOFTWARETERMSOFUSE, '我不同意该协议')
    root.mainloop()
    root = tk.Tk()
    user_guide = UserGuide(root, '确定', root.destroy, USERGUIDE, '取消')
    root.mainloop()
    root = tk.Tk()
    software = Windows(root)
    root.iconphoto(False, tk.PhotoImage(file='SuperDel.png'))
    root.mainloop()


if __name__ == '__main__':
    main()
