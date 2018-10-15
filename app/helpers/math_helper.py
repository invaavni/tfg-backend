"""Helper which makes math calcs"""

import scipy

class MathHelper():
    """Class which makes math calcs"""

    def rsquared(self, real_data, prediction):
        """ Return R^2 where x and y are array-like."""

        slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(real_data, prediction)
        return r_value**2
