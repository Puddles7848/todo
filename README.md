# Todo (Description, not project to-do list.)
This is a personal project & challenge. The conditions are:
- stdlib only.
- two files max.
- - one for the main script
- - another for the data


## Why?
It was because I occasionally add things like
```
echo "Do xyz"
```
to my `~/.zshrc`, and I thought, "maybe i should make it real :3"


## Why 8 length max (by default)?
Eight is a nice power of two (2^3)...
And also so it doesn't get cluttered.
Anyway, you can change it in the data yourself in the data file. In it, you can go to the `config` section and change the `max_length` value. I have no clue what happens when it's negative or 0 :3

# Docs?
Read [DOCS.md](DOCS.md) (-_-)

## To-do (the actual to-do list for this project)
1. Stop line 77 and 88 from crying—too lazy to TypedDict
2. Add a feature where setting the max length to a negative number disables the cap
3. Make `rmALL` delete the entire list (with confirmation and not in the main rm so it's harder to oopsie)
