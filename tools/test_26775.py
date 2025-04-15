import numpy as np

impurities = np.random.random(5*4).astype("f8,S3")["f0"][::4]
print("f8 alignment:", np.dtype("f8").alignment)
print(impurities, impurities.flags)
print(-impurities)
