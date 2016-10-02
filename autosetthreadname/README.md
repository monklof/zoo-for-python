# Auto set thread name

Python's `threading.Thread` instance can have a `name`, which is just a concept inside python, it can't be seen from the OS. In linux, every thread can have a `command name` itself(see the `/proc/[pid]/comm` part of [man proc][comm]), We can use this attribute to identify a thread for better debugging.

This module will automatic set the `comm` attribute of the thread when a Thread starts. You can use the `ps` command to look the attribute, for example: 

```bash
$ ps H ax -o start_time,pid,tid,cmd,comm -q 
```

![](http://7lrwkm.com1.z0.glb.clouddn.com/threadname.png)

## Usage

1. Install [python-prctl](https://github.com/seveas/python-prctl) first.
2. Just import this module before you create your thread.

## Note

* Only work in linux.


Copied from [stackoverflow][stack].

[stack]: http://stackoverflow.com/questions/34361035/python-thread-name-doesnt-show-up-on-ps-or-htop
[comm]: 
