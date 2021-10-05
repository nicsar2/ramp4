import io
import cv2
import fs
import fs.memoryfs
import numpy as np
import matplotlib.pyplot as plt


class ramp4():
    """
    INTRODUCTION
    ------------
    A simple library to make mp4 movies with matplotlib.pyplot. It use RAM instead of disk storage for the temporary images.

    HOW TO USE
    -----------
    1) Get an instance of ramp4.
    2) Add image with matplotlib using the 'add' method.
    3) Render the movie using the 'render' method.
    4) Done

    """

    def __init__(self):
        self.cpt = 1
        self.mem = fs.memoryfs.MemoryFS()

    def add(self, figure=None, dpi=150):
        """
            Add the following image to the movie. The image has to be previously generated with matplotlib.pyplot using pyplot method or OOP.

            Parameters:
            -----------
            fig : None or matplotlib.pyplot.figure
                If matplotlib.pyplot OOP is used then put the figure object in this parameter.
                If None is provided, the matplotlib.pyplot's method 'pyplot.savefig' will be use to get the byte of the image.
                The correct way should be selected depending of the way matplotlib is used.
            dpi : int
                The pixel density of the image. Should be a positive integer.
        """

        buf = io.BytesIO()

        if figure is None:
            plt.savefig(buf, format="jpg", dpi=dpi)
        else:
            figure.savefig(buf, format="jpg", dpi=dpi)

        buf.seek(0)
        self.mem.writebytes("{:0>25}".format(self.cpt), buf.read())
        self.cpt += 1

    def render(self, outfile="movie.mp4", fps=20, close=True):
        """
            Render the final movie and save it.

            Parameters:
            -----------
            outfile : string
                The path and name of the movie. The extension should be 'mp4'.
            fps : int
                Frames per second. Should be a positive integer.
            close : bool
                If True, close the RAM filesystem after rendering.

        """
        images = self.mem.listdir(".")
        height, width, _ = self.bytes2img(self.mem.getbytes(images[0])).shape
        movie = cv2.movieWriter(outfile, cv2.movieWriter_fourcc(*'mp4v'), fps, (width, height))

        for image in images:
            print("{0} / {1}".format(int(image), len(images)))
            movie.write(self.bytes2img(self.mem.getbytes(image)))

        cv2.destroyAllWindows()
        if close:
            self.close()

    def close(self):
        """
            Close the RAM filesystem.
        """
        self.mem.close()

    @staticmethod
    def bytes2img(bytes):
        """Convert a bytes image to openCV image.

            Parameters:
            -----------
            bytes : bytes
                Input containing the image bytes.
        """
        return cv2.imdecode(np.frombuffer(bytes, dtype='uint8'), cv2.IMREAD_UNCHANGED)
