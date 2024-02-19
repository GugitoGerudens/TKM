import math
import pandas
def interpol(x, lstx, lsty, create_table=False):
    n = len(lstx)-1
    tmi=[round((x-i)/0.005,2) for i in lstx]
    Ci=[round((pow(-1, n-i)*math.factorial(i)*math.factorial(n-i))) for i in range(n+1)]
    tmiCi=[round(tmi[i]*Ci[i],2) for i in range(n+1)]
    yidtmiCi=[round(lsty[i]/tmiCi[i],7) for i in range(n+1)]
    Pnp1t=math.prod(tmi)
    rsum=sum(yidtmiCi)
    result = rsum*Pnp1t
    if create_table:
        df = pandas.DataFrame([lstx, lsty, tmi, Ci, tmiCi, yidtmiCi], index=['x_i', 'y_i', 't-i', 'C_i', '(t-i)C_i', 'y_i/((t-i)C_i)'])
        df = df.T
        df.to_excel("output.xlsx");
    return result