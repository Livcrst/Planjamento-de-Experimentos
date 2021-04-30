import numpy as np
import statsmodels.api as st
from statsmodels.sandbox.regression.predstd import wls_prediction_std

Lenght = [128, 256, 384, 512, 640, 768, 896, 1024]
ob2 = [375, 805, 1644, 3123, 6839, 14567, 27439, 52129]
x = np.array(Lenght)
y = np.array(ob2)

xc = st.add_constant(x)

model = st.OLS(y, xc)

result = model.fit()

sb0, sb1 = result.conf_int(alpha=0.1) #Onde define são definidos os 90% de confiança de minha estimativa
print(sb0, sb1) #intervalo de confiança