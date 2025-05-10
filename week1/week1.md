# Week 1

The first goal is to become familiar with the Windows and Linux Command Line Interface (CLI). The CLI allows you to perform tasks that you would normally do through a Graphical User Interface (GUI), such as creating directories, moving between directories, creating text files, and removing directories or files. As you progress through the course, the command line interface will become more intuitive. For now, focus on learning the basic commands.

## Windows

### Command
  A command is a compiled program. Microsoft has written the commands using C/C++, converted it into machine code and then placed the commands in the `C:\Windows\System32` directory. Normally it is not possible to run a command from another location than it's own. But as we saw `cd` works everywhere in the filesystem. This is possible because of Operating System Environment Variables. Read more about it online.

### Basic Commands
To open the Windows Command Prompt (cmd), go to the Windows search menu at the bottom left of the screen and type `cmd`. A black terminal icon will appear. Click on it to open the Command Prompt.

| Command     | Description                                           |
|-------------|-------------------------------------------------------|
| `dir`       | Lists the contents of the current directory           |
| `cd`        | Changes the current directory                         |
| `mkdir`     | Creates a new directory                               |
| `rmdir`     | Removes an existing directory                         |
| `notepad`   | Opens Notepad to create or edit a text file           |
| `del`       | Deletes a text file                                   |

**Note:** Some commands, like `dir`, do not require additional information to execute. Others, like `cd`, `mkdir`, `rmdir`, and `del`, require extra information (e.g., directory or file names) to function properly.

### Practice Tasks

Follow these exercises to get hands-on experience with basic commands:

1. **Open Windows Command Prompt**  
   - Follow the steps above to open `cmd`.

2. **Create a Directory**  
   - Use the `mkdir` command to create a directory named `practice`.

3. **Navigate into the Directory**  
   - Use the `cd` command to move into the `practice` directory.

4. **Create Multiple Directories in One Command**  
   - Inside `practice`, create two directories named `dir1` and `dir2` using a single `mkdir` command.  
   - You may use Google or ChatGPT to search how to do this.  
   - Please read the explanation for each part of the command so you don’t need to search for again, when doing the same task next time.

5. **Move into `dir1`**  
   - Use `cd` to enter the `dir1` directory.

6. **From `dir1`, Navigate to `dir2` in One Command**  
   - Without returning to the parent folder, move directly into `dir2` using a single command.  
   - Ask ChatGPT for help if needed, and request an explanation for each part of the command.

That’s enough for the Windows Command Prompt. Now let’s move to Linux.

## Linux

Linux is an **open-source operating system kernel**. The **kernel** is the core component of any operating system. It manages communication between software and hardware, including tasks such as:

- Allocating memory to applications (e.g., Chrome, YouTube)
- Handling input/output devices (keyboard, mouse, monitor)
- Managing processes and multitasking

You can explore the Linux kernel source code here:  
[Linux Kernel Source Code](https://github.com/torvalds/linux)

### Kernel vs Full Operating System

While the **kernel** is essential, it’s not enough to make a complete operating system. A full Linux OS combines the kernel with various **open-source software components**, including:

- **GNU utilities** (like `ls`, `cd`, `mkdir`, etc.)
- **X11 Display Server** (used for graphical interfaces)

> Without X11, Linux can still run — but it won’t have a GUI (Graphical User Interface).

Learn more about X11:  
[X11 Wiki](https://x.org/wiki/)

Commands we are going to use come under the hood of GNU (GNU Not Unix) Project. This is an Open-Source project. I am putting a link (for those who are curious) of a gnu package that contains the source code of `cd`, `ls` and a lot of other commands.

https://mirror.truenetwork.ru/gnu/coreutils/coreutils-9.4.tar.xz

### Linux Commands

Linux commands are very similar to Windows Commands. They are compiled, machine code. You can find most of the linux command under `/bin/` directory. Just as `C:\` is the starting location in Microsoft Windows, `/` is the starting location in Linux.

### Practice Tasks

Follow these exercises to get hands-on experience with basic commands:

1. **Open Linux Terminal**  
   - Opening a Terminal varies according to the distro you are using. A general procedure would be to press the window button on your keyboard and search for terminal. A black window like icon will appear. Open it.
   ![Alt text](terminal.png)

2. **Print Working Directory**  
   - Enter `pwd` to print current working directory. The output will be similar to `/home/your_username`.

3. **Make Directory**
   - Make a directory named project using `mkdir` command exactly like windows.

4. **Change Directory**
   - Move into `practice` using `cd`.

5. **Make two directories**
   - Make two directories named `dir1`, `dir2` using `mkdir` command.

6. **Change Directory**
   - Move into dir1.

7. **Print Current Directory**
   - Enter `pwd` command to see your current location. It should be something like `/home/yourusername/project/dir1/`

8. **Change Directory**
   - Change your directory to `dir2` using `cd` command. You must do it in single command, not three.

After completing these steps you can stop.

# Linux Virtual Machine
It is highly recommended to install a Linux virtual machine using `VirtualBox`. But if you are not able to do that or your machine can't afford to run a virtual machine. There are couple of other ways, you can try.

**Google Cloud**
Please Create an account on Google Cloud. Google Cloud offers a limited VM to manage the cloud infrastructure. You can use that machine to perform tasks.

**NDG**
Register yourself at Linux Essentials Source at NDG website. You will be given a Linux machine.

**Termux**
Although I don't recommend it at all but you can install termux application on your andriod based smart phone. It will give you access to a Linux environment. But you cannot use it in long term.


Please install a personal Linux virtual machine on your local computer. It's better. On all other platforms, you can get issues.
If any of you have any difficulties, feel free to ask me.