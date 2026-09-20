# Documentation
So you came here to read, eh? Well I'll try not to bore you and actually get to the point. **To-do has 4 subcommands.** And yes, I named 3/4 after system utilities.

1. touch
2. rm
3. ls
4. config

Why config and not something like... `vim`? Because nobody can agree on the text editor (╥﹏╥) It could be `ed`, `nano`, `pico`, `vim`, `nvim`.

Now lets get into them.

## Touch
Like `touch`, it well... creates things.
```
$ todo touch "Write the documentation for this program"
```
It will fail if that item already exists. It is case-sensitive. It also fails if the list is at maximum capacity. This cap can be changed by the user.

## Rm
Rm is basically `rm`. If you don't know
```
$ todo rm "Write the documentation for this program"
```
It will fail if the item doesn't exist. It is just as case-sensitive as `touch`.

## Ls
```
$ todo ls
```
It's just ls... it lists what you have in your to-do list...

## Config
Now this one is not self-explanatory. It just executes `$EDITOR /path/to/config/file`. Yes. Bring Your Own Editor. If `$EDITOR` is not set, it will fail with `OSError`. If you want to know where is it? Or maybe just want to cat it? Hear me out:
```
$ export EDITOR=ls
$ todo config
$ export EDITOR=cat
$ todo config
```
Don't forget to change your editor back okay (╥﹏╥)
AND DON'T BREAK THE JSON
Scroll down if you did :3

## Changing the cap
Run `todo config`. It's literal json.
```
{"config": {"maxlen": 8}, "data": []}
```
It should look something like that. The json has a key called `config`, that's a dictionary with another key called `maxlen`. It should be a positive integer. If it is 0, the cap is literally 0 and you can't create anything (╥﹏╥) If it's negative, you still can't create anything (╥﹏╥)

## Help I broke the json (╥﹏╥)
I told you not to break it... fine...
So you can temporarily set your editor to either `ls` or `rm` (dangerous). If it's `ls`, just use that path next to `rm`. Delete the file any way actually. If there is no file, it regenerates itself. And yes **YOU LOSE YOUR DATA AND CONFIG.**

## You made it to the end :3
That's it.
