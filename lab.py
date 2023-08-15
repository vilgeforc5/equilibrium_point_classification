
import numpy as np
import scipy.integrate as sp
import matplotlib.pyplot as plt
import sympy as sm

class System:
    def __init__(self, system, point, t):
        self.systemX = sm.sympify(system[0])
        self.systemY = sm.sympify(system[1])
        self.point = point
        self.t = t

    def f_ode(self, y, t):
        x, y = y
        return np.array([sm.lambdify('x, y', self.systemX)(x, y),         
                         sm.lambdify('x, y', self.systemY)(x, y)])

    def solve(self):
        t = np.linspace(0, self.t, 100)
        x = sp.odeint(self.f_ode, self.point, t)
        return x[:, 0], x[:, 1], t

class PlotFigure:
    def __init__(self, system, title):
        fig, ax = plt.subplots(ncols=2)
        fig.suptitle(title)

        X, Y, U, V = self.quiverField(system)
        x, y, t = system.solve()

        ax[0].quiver(X, Y, U, V, color='orange', scale=25, pivot='mid')
        ax[0].streamplot(X, Y, U, V, color='gray', arrowstyle="fancy", linewidth=1, )
        ax[0].plot(x,y, color="r")
        ax[0].set_xlim(-10, 10)
        ax[0].set_ylim(-10, 10)

        ax[1].plot(t, x, color = 'orange', label='x')
        ax[1].plot(t, y, color = 'blue', label='y')
        ax[1].legend()

        ax[1].grid()
        ax[0].grid()
        plt.show()
        
    def quiverField(self, system, botLim=-10, topLim=10, lines=15):
        x = np.linspace(botLim, topLim, lines)
        y = np.linspace(botLim, topLim, lines)
        X, Y = np.meshgrid(x, y)
        U, V = system.f_ode([X, Y], 0)
        N = np.sqrt(U**2+V**2)
        return X, Y, U/N, V/N

s1 = System( 
        ['5*x+y-5', 'x+2*y-1'], 
        [1.1, 0.6], 
        3
    )
plot1 = PlotFigure(s1, title = "First graph")

