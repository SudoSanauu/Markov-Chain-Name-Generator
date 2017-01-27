This is a simple tool for generating names based on an input file using a [Markov Chain](https://en.wikipedia.org/wiki/Markov_chain).

##Input File Format:
The input file should be a plain text file consisting of a number of names each separated by a single newline character.
```
DAVID
RICHARD
CHARLES
JOSEPH
THOMAS
PATRICIA
CHRISTOPHER
LINDA
BARBARA
DANIEL
PAUL
MARK
```
An example input file is included in the directory. Inputting different name lists will result in a different Markov Chain and hence a different output.

##How To Use:
As a simple python 3 script with no dependencies, you should be able to run this from your terminal with.
```
python3 markov.py
```
If run this way, you will be prompted for the input file path, the Markov Chain Seed Length, and then how many characters you wish to output. Alternatively, all of these parameters can be defined when running the program.
```
python3 markov.py ./name_list.txt 3 1000
```

###What is Chain Seed Length?
A Markov Chain can be described as a series of nodes which each contain a value and edges which represent the probability that one node leads to another node. In our program, each node holds a series of characters, and the edges represent the probability of other characters following those characters. 
Chain Seed Length determines how many characters in a row are taken into account when determining the next character.
For instance, a CSL of 1 would result in a Markov Chain which only looks at the previous character to determine the next one. In this case, the probability of `stev` being followed by an `e` is the same as `eiv`, `asdfv`, or even just `v`.
If the CSL were 2, then the chance of `stev` being followed by `e` would be the same as any name ending in, `ev`, but different from any other two letter combination, such as `iv`, `fv`, or `\nv`.
Practically, increasing the CSV will result in names which are closer to exact copies of the input names, while decreasing it will result in names which are closer to gibberish. I have found the most success with a CSL of 2 or 3, but this may change with the length and contents of your input file.
Also, I was unable to find an official name for CSL, so if anyone knows a better name, please email me at jacobson.s.aaron@gmail.com .
