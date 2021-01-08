from nbautoeval import ExerciseFunction, Args, PPrintCallRenderer, ExerciseFunction
from random import randrange

def calculation(x):
    return pow((5 * x) / 2, 2)


inputs_calculation = [
    Args(randrange(100)),
    Args(randrange(100)),
    Args(randrange(100)),
    Args(randrange(100)),
    Args(randrange(100)),
    Args(randrange(100)),
    Args(randrange(100)),
    Args(randrange(100)),
    Args(randrange(100)),
    Args(randrange(100)),
]

exo_calculation = ExerciseFunction(
    calculation, inputs_calculation,
    call_renderer=PPrintCallRenderer(
        show_function=False,
        css_properties={'word-wrap': 'break-word', 'max-width': '40em'},
    ))
