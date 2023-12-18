# Functions
There are 2 functions currently.
`coloured(text:string,colour: tuple)`
and
`cprint(text:string,colour: tuple)`<br>
...
yes, there are the same (on a writing pov) but cprint will print coloured text, and coloured will return coloured text
# why did i make this?
because termcolor only supports not many colours.

# details
I am not from the US. so you cant perfectly pick up terminalRGB from termcolor, especially if you're a user of eng-us.

# extra
there is an extra option on all functions: `force=False`<br>
what does it do?<br>
from using macOS i've noticed that i cant display most colours using ANSI. so enabling `force` will force return the data. (as the name implies)
