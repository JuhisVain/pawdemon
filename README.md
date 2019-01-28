PAWDEMON
========

A (vanilla) Doom 1/2 level editor thing or library


The 'Abstract_sector' class is supposed to be the main user interface which you add into instances of class 'Level', which you will add into an instance of class 'Project'. Call project's method compile to cerate a raw WAD-file, which will need to be fed to a nodebuilder such as BSP to produce an iwad usable in a vanillaish doom port.

Currently you'll also need to create instances of "lower" level classes such as things and vertices. The doomwad-like classes could also be used to implement your own abstractions.