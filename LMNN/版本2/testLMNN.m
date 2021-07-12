x=[0 0; -1 -0.1; 0.3 -0.05; 0.7 0.3; -0.2 -0.6; -0.15 -0.63; -0.25 0.55; -0.28 0.67]';
y=[0 0 0 0 1 1 2 2];
subplot(121)
graphical_insight_plot(x)
title('Original data')
grid on

L = lmnn(x,y,1);
disp('L='), disp(L);

Lx = L*x;
subplot(122)
graphical_insight_plot(Lx);
title('Data transformed after LMNN')
grid on