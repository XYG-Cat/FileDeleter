# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


# 这个程序是自由软件，你可以自由地重新发布和/或修改它
# 根据自由软件基金会发布的GNU通用公共许可证的规定，
# 不论是该许可证的第3版或者是之后的版本。

# 这个程序是基于免责条款发布的，我们提供的软件没有任何担保，
# 也没有隐含的担保条件，包括但不限于适销性或特定用途适用性的担保。
# 有关更多详情，请参阅GNU通用公共许可证。

# 你应该已经收到了GNU通用公共许可证的副本，
# 如果没有，请参阅 <https://www.gnu.org/licenses/>。


SOFTWARETERMSOFUSE = '''声明：

    尊敬的用户,

    感谢您选择使用我们开发的批量选择性删除文件的程序。在使用我们的程序时,请您务必谨慎操作,确保您删除的文件符合您的意图。

    我们理解在使用任何软件时,误操作是难免的。然而,我们需要明确声明,对于由于误操作而导致的文件删除,我们无法承担任何责任或赔偿责任。无论是因为技术问题还是操作失误,我们都无法对您的文件损失负责。

    因此,请在使用我们的程序时,务必审慎确认您的操作,特别是在进行批量删除或选择性删除操作时。我们建议您在进行任何重要操作之前备份您的文件,以免发生意外损失。

    我们将继续努力改进我们的程序,以提供更好的用户体验和更高的可靠性,但对于误操作造成的文件损失,我们无法承担责任。

    为了避免使用程序误操作产生损失,请您在详细阅读操作说明后使用该程序！

    感谢您的理解和支持。

    此致,

    [POINT/XYG_Cat]
--------------------------------------------------------------------------------
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.


    这个程序是自由软件，你可以自由地重新发布和/或修改它
    根据自由软件基金会发布的GNU通用公共许可证的规定,
    不论是该许可证的第3版或者是之后的版本。

    这个程序是基于免责条款发布的，我们提供的软件没有任何担保，
    也没有隐含的担保条件，包括但不限于适销性或特定用途适用性的担保。
    有关更多详情,请参阅GNU通用公共许可证。

    你应该已经收到了GNU通用公共许可证的副本,
    如果没有，请参阅 <https://www.gnu.org/licenses/>。
--------------------------------------------------------------------------------

'''


USERGUIDE = '''
### 操作说明

1. **文件操作菜单(File):**
   - **打开(Open):** 点击该选项以打开文件选择对话框,选择要操作的文件。
   - **批量删除(del):** 该选项包含多个子选项,用于按关键词或文件后缀进行批量删除。
      - **按关键词删除:**
        可以删除包含指定关键词的文件或不包含指定关键词的文件,可以选择递归子目录或不递归
      - **按文件后缀删除:**
        可以删除包含指定后缀的文件或不包含指定后缀的文件,可以选择递归子目录或不递归
   - **删除选定文件(夹):** 选择文件或文件夹后点击该选项以删除选定的文件或文件夹。
   - **退出(Exit):** 点击该选项以退出应用程序。

2. **视图操作菜单(View):**
   - **全屏模式(Fullscreen):** 切换应用程序窗口到全屏模式。
   - **视窗模式(Windows):** 切换应用程序窗口到普通视窗模式。

3. **帮助菜单(Help):**
   - **查看帮助(For help):** 点击该选项以查看帮助文档。

4. **关于菜单(Option):**
   - **关于作者:** 点击该选项以获取有关作者的信息。

5. **文件/文件夹浏览器:**
   - 双击文件或文件夹以打开或进入。
   - 单击文件或文件夹以查看选中的项目的完整路径。

6. **注意事项:**
   - 如果在执行文件操作时出现权限问题,可能需要以管理员或root用户身份打开应用程序。

### 使用说明

1. 运行程序后,您将看到一个具有文件操作、视图和帮助菜单的GUI界面。上面显示的文件(夹)就是待操作的文件，您可以双击文件夹打开，双击'..'回到上级目录，直到找到你想要操作的文件夹。
2. 找到你想要操作的文件夹后，您先要双击打开它，而不是单击选中它
3. 使用文件菜单进行文件操作,视图菜单可以调整应用程序窗口的显示模式。
4. 在文件/文件夹浏览器中,双击文件或文件夹以打开或进入,可以查看完整路径。
5. 关于作者的信息可以在关于菜单中找到。
6. 如果执行文件操作时遇到权限问题,请以管理员或root用户身份运行应用程序。

### 特别说明

1. 当您在进行文件操作时,可能会遇到“递归子目录”，“递归子目录”意味着操作不仅会在您指定的文件夹中进行,还会在该文件夹内的所有子文件夹中进行,以及子文件夹的子文件夹中进行,依此类推,直到达到最深层的文件夹。
例如,如果您选择“递归子目录”来删除包含特定关键词的文件,那么系统将会检查您指定的文件夹以及其内部的所有子文件夹,并删除所有包含该关键词的文件,无论这些文件位于多深的子目录中。


'''
