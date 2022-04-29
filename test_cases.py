



#|%%--%%| <FCXglLHwTU|2BShAsWM7q>
"""°°°
## Test Cases for Acoustic inversion
°°°"""
#|%%--%%| <2BShAsWM7q|xcJT3wzdbH>
"""°°°
### 1D Case
°°°"""
#|%%--%%| <xcJT3wzdbH|Jm1q1Tbh15>

import numpy as np
import matplotlib.pyplot as plt

#|%%--%%| <Jm1q1Tbh15|dtKEgEI44k>
### monotonic linear speed function 
max_speed = 1.5
min_speed = 0.5
NN = 100 

linear_test = np.linspace(min_speed, max_speed, NN) 
#|%%--%%| <dtKEgEI44k|E04g3KfLfC>
### step speed function
step_test = np.zeros_like(linear_test)
step_test[0:40] = 0.5
step_test[61:99] = 0.5
step_test[41:60] = 0.5

#|%%--%%| <E04g3KfLfC|a0ykRqVkiG>
### sin low freq speed function
sin_low_test = np.sin(linear_test*np.pi)
plt.plot(linear_test, sin_test)
plt.show()

#|%%--%%| <a0ykRqVkiG|Sm7hxnGAJH>
### sin high freq speed function
sin_high_test = np.sin(linear_test*6*np.pi)
plt.plot(linear_test, sin_high_test)
plt.show()


#|%%--%%| <Sm7hxnGAJH|f5KxbYtoKo>
"""°°°
### 2D Case
°°°"""
#|%%--%%| <f5KxbYtoKo|jHxyr4XvfN>

xx,yy= np.meshgrid(linear_test, linear_test)
plane_test = xx+yy
plane_test.shape
plt.imshow(plane_test)
plt.show()

#|%%--%%| <jHxyr4XvfN|w63WnFmNoh>

hill_test = np.sin(yy*np.pi)*np.cos(xx*np.pi)
hill_test
plt.imshow(hill_test)
plt.show()
#|%%--%%| <w63WnFmNoh|vX2fuoQ699>



