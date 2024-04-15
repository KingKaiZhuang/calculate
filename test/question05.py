from sympy import symbols, Function, sqrt, diff, solve

# 定義符號
t = symbols('t')
x = Function('x')(t)  # x 是關於 t 的函數
dx_dt = 0.2  # x 的變化率

# 梯子的長度，一個常數
L = 10

# 定義 y 也是 t 的函數，但是這裡我們不需要直接定義 y(t)，因為我們將用 x 和 L 來表示 y
y = sqrt(L**2 - x**2)

# 計算 dy/dt
dy_dt = diff(y, t)

# 代入 x 的變化率 dx/dt
dy_dt_evaluated = dy_dt.subs(diff(x, t), dx_dt)

# 將 x = 6 代入到 dy/dt 中
dy_dt_at_x_6 = dy_dt_evaluated.subs(x, 6)

print(f'當梯子的底部與牆角相距 6 米時，梯子的上端沿牆壁下滑的速率為 {dy_dt_at_x_6:.2f} 米/秒。')
