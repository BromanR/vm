import sympy as sp
import pandas as pd
import matplotlib

x, y = sp.symbols('x y')
f = sp.sin(x - 0.4 * y) - x +y**2
g = (y+0.1)**2 + x**2 - 0.7

plot = sp.plot_implicit(sp.Eq(f, 0), show=False, line_color='blue')
plot.extend(sp.plot_implicit(sp.Eq(g, 0), show=False, line_color='green'))
plot.show()

def newton_system(x, y, f, g, x0, y0):
    dfdx = f.diff(x)
    dfdy = f.diff(y)
    dgdx = g.diff(x)
    dgdy = g.diff(y)
    
    d = dfdx * dgdy - dgdx * dfdy
    dx = f * dgdy - g * dfdy
    dy = dfdx * g - dgdx * f

    xs, ys, norms, fs, gs = [], [], [], [], []
    xk, yk = x0, y0
    while True:    
        new_x = xk - (dx / d).evalf(subs={x: xk, y: yk})
        new_y = yk - (dy / d).evalf(subs={x: xk, y: yk})
        xs.append(new_x)
        ys.append(new_y)

        norm = sp.sqrt((new_x - xk) ** 2 + (new_y - yk) ** 2)
        norms.append(norm)
        fs.append(f.evalf(subs={x: new_x, y: new_y}))
        gs.append(g.evalf(subs={x: new_x, y: new_y}))

        xk, yk = new_x, new_y

        if norm < 1e-5 and len(xs) > 1:
            break
    return pd.DataFrame(list(zip(xs, ys, norms, fs, gs)), columns=['x', 'y', 'норма', 'f', 'g'])


print (newton_system(x, y, f, g, 1, 1))
print (newton_system(x, y, f, g, 1, -1))
