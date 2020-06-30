Add the following to your ~/.Xmodmap file:

clear control
clear mod4

keycode 105 =
keycode 206 =

keycode 133 = Control_L NoSymbol Control_L
keycode 134 = Control_R NoSymbol Control_R
keycode 37 = Super_L NoSymbol Super_L

add control = Control_L
add control = Control_R
add mod4 = Super_L
To test this right now, just do xmodmap ~/.Xmodmap

Now, to have this happen every time at startup, add to the end of your (and/or create a new) ~/.xinitrc file the following:

xmodmap ~/.Xmodmap

