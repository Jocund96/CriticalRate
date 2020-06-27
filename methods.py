import math as m


def strToFloat(text):
    try:
        text_dot = text.replace(",",  ".")
        chislo = float(text_dot)
        return chislo
    except Exception:
        return False


def chaperon(b, kv, kh, h, myu, row, roo, re):
    # b, kv, kh, h, myu, row, roo, re b=1.19, kv=0, kh=112, h=110, myu=1.12, row=1.14, roo=0.88, re=400
    try:
        alfa = re / h * m.sqrt(kv / kh)
        qc = 0.731 + (1.9434 / alfa)
        q = (3.486 * 10 ** -5 * kh * h ** 2 * m.fabs(row - roo) * qc * 24) / (b * myu)
        return q
    except ZeroDivisionError:
        return 0


def meyergardner(b, kh, h, myu, row, roo, re, hp, rw):
    try:
        mtof = 3.28084           # metertofeet
        q = 0.158987 * (0.001535 * (row - roo) * kh * ((h * mtof) ** 2 - (hp * mtof) ** 2) / (m.log(re / rw) * myu * b))
        return q
    except ZeroDivisionError:
        return 0


def schols(b, kh, h, myu, row, roo, re, hp, rw):
    try:
        mtof = 3.28084
        q = 0.158987*((row - roo)*kh*((h*mtof)**2-(hp*mtof)**2)/(2049*myu*b)*(0.432+(3.1415/m.log(re/rw)))*(h/re)**0.14)
        return q
    except ZeroDivisionError:
        return 0


def hoyland(b, kh, h, myu, row, roo, re, hp):
     try:
        mtof = 3.28084
        q = 0.158987*(kh*(row - roo)/(173.35*b*myu)*(1-((hp*mtof)/(h*mtof))**2)**1.325*(h*mtof)**2.238*(m.log(re*mtof))**-1.99)
        return q
     except ZeroDivisionError:
         return 0


def hor_chaperon(b, kv, kh, h, myu, row, roo, re, l):
    try:
        mtof = 3.28084
        lam = (re*mtof)/(h*mtof)*m.sqrt(kv/kh)
        f = 3.9624955+0.0616438*lam-0.00054*lam**2
        q = 0.158987 * (4.888*10**-4*(l*mtof)/(re*mtof)*(row - roo)*(kh*(h*mtof)**2/(myu*b))*f)
        return q
    except ZeroDivisionError:
        return 0


def hor_efors(b, kh, h, myu, row, roo, re, l):
    try:
        mtof = 3.28084
        q = 0.158987 * (4.888*10**-4*(l*mtof)*kh*(h*mtof)**2*(row - roo)/(myu*b*(re*2*mtof)*(1+m.sqrt(1+((h*mtof)**3/3)*(1/(re*2*mtof)**2)))))
        return q
    except ZeroDivisionError:
        return 0


def hor_giger(b, kh, h, myu, row, roo, re, l):
    try:
        mtof = 3.28084
        q = 0.158987 * (4.888*10**-4*(kh/(myu*b))*((row - roo)*(h*mtof)**2/(re*2*mtof))*(1-1/6*((h*mtof)/(re*2*mtof))**2)*(l*mtof))
        return q
    except ZeroDivisionError:
        return 0
