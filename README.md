Click here to start the notebook:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sunfishstanford/manimjupyter/HEAD?filepath=notebook)

To create animations:
1. Use Jupyter notebook R1CS_explain.ipynb to experiment
2. Copy/paste final code into R1CS.py
3. manim -pql R1CS.py Formula (assuming that Formula = class name)
4. ffmpeg -i ./media/videos/R1CS/480p15/Formula.mp4 -loop 0 fig1.gif