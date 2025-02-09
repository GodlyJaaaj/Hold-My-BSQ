# Disclaimer

Altough this is a competition, the main goal is to have fun and learn something new. The competition is not about winning, but about participating and learning.
So, if you are a beginner, don't be afraid to participate. You will learn a lot by doing so 🚀.

---

# Competition rules

- all languages are allowed
- it must work on ubuntu 24.04
- no multi-threading
- no map error handling - all maps are valid by default
- the map generation part is not necessary
- you must provide a Makefile if needed to compile your code: must be as easy as `make`
- you must provide a README.md with the following information:
  - how to compile your code if needed
  - dependencies if needed and how to install them
- you must provide a public repository with your code
- your program must be named `bsq`
- tested only on 10k x 10k maps

---

# Map format

## Example

````text
5
oo.oo
o....
....o
..o..
..ooo
````
See [example.txt](example.txt)

The first line is the size of the map. The following lines are the map itself. `o` is a wall, `.` is a free space.

---

# How your program must work

```bash
./bsq example.txt
```

`example.txt` is the path to the map file.

---

# How to test your program

We provide a generator that you can use to generate maps.
### Requirements
- python3

```bash
./generator.py [width] [height] [density] [seed] --auto-save
```

### Example

```bash
./generator.py 10 10 0.1 10 --auto-save
```

This will generate a map of size 10x10 with a density of 0.1 and a seed of 10. The map will be saved in `map_10x10_r10_s10.txt` if you use the `--auto-save` option.
