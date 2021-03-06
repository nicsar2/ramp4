import setuptools as st

st.setup(
    name='ramp4',
    version='1.0  ',
    description='A simple library to make mp4 movies with matplotlib.pyplot. It use RAM instead of disk storage for the temporary images.',
    long_description="""
=====
RAMP4
=====

INTRODUCTION
------------
A simple library to make mp4 movies with matplotlib.pyplot. It use RAM instead of disk storage for the temporary images.

INSTALLATION
------------
.. code-block:: sh
    :name: test.sh

    pip install ramp4

GET STARTED
-----------
1) Get an instance of ramp4.
2) Add image with matplotlib using the 'add' method.
3) Render the video using the 'render' method.
4) Done


EXAMPLE 1
---------
.. code-block:: python
    :name: test.py

    import numpy as np
    import matplotlib.pyplot as plt
    from ramp4 import ramp4

    X = np.linspace(0, 5, 250)

    movie = ramp4()
    for i in np.linspace(0, 3.14, 200):
        plt.plot(X, np.cos(X+i))
        plt.xlim(0, 5)
        plt.ylim(-1, 1)
        plt.xlabel("x")
        plt.ylabel("cos(x+t)")
        movie.add(dpi=200)
        plt.close()

    movie.render(outfile="video_example_2a.mp4", fps=50, close=False)
    movie.render(outfile="video_example_2b.mp4", fps=100)

EXAMPLE 2
---------
.. code-block:: python
    :name: test2.py

    import numpy as np
    import matplotlib.pyplot as plt
    from ramp4 import ramp4

    X = np.linspace(0, 5, 250)

    movie = ramp4()
    for i in np.linspace(0, 3.14, 200):
        fig, ax = plt.subplots(1, 1)
        ax.plot(X, np.sin(X+i))
        ax.set_xlim(0, 5)
        ax.set_ylim(-1, 1)
        ax.set_xlabel("x")
        ax.set_ylabel("sin(x+t)")
        movie.add(fig=fig, dpi=200)
        plt.close(fig=fig)

        movie.render(outfile="video_example1.mp4", fps=50)
""",
    long_description_content_type='text/x-rst',
    author='Nicsar',
    author_email='nicolas.sartore@ens.psl.eu',
    license='MIT',
    install_requires=['opencv-python==4.5.3.56',
                      'fs==2.4.13',
                      'numpy',
                      'matplotlib'],
    python_requires='>=3',
)
