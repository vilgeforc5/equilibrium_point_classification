# Equilibrium Points Classification
# Классификация точек равновесия системы диф.уравнений второго порядка

Simple Python script to vizualize behavior of Equilibrium Points in Two-Dimensional Systems of Differential Equations.
Using numpy, scipy, matplotlib, sympy.
Try to play with inner presets to achieve best result


```
s1 = System( 
                ['5*x+y-5', 'x+2*y-1'],  #system of equations
                [1.1, 0.6],              # point
                3                        # "step"
           )
plot1 = PlotFigure(s1, title = "First graph")
```

<img width="1030" alt="Screenshot 2023-08-15 at 17 37 22" src="https://github.com/vilgeforc5/equilibrium_point_classification/assets/57109127/8dd3e5ca-f2c9-4273-a173-504a31385fdf">


```
s2 = System(['3*x-4*y-3', '4*x+3*y-4'], [1.1, 2], 3)
plot2 = PlotFigure(s2, title = "Second graph")
```
<img width="884" alt="Screenshot 2023-08-15 at 17 49 35" src="https://github.com/vilgeforc5/equilibrium_point_classification/assets/57109127/f4152a5f-4230-42de-847a-76cabfb341aa">


