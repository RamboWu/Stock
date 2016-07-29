import seaborn as sns
import numpy as np
from numpy.random import randn
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats


# style set 这里只是一些简单的style设置
sns.set_palette('deep', desat=.6)
sns.set_context(rc={'figure.figsize': (8, 5) } )
np.random.seed(1425)
# figsize是常用的参数.
data = randn(75)
plt.hist(data)

sns.plt.show()
