%% getGenNN

fprintf('testing getGenNN...\n\n')

%%% preamble

% number of examples
n = 1000;
% input dimension
d = 10;
% number of different labels values, they will be taken from the interval
% [1,l]
l = 10;
% number of neighbours
k = 5;

%%% test

% generate feature vectors randomly
x = rand(d, n);
% genrate labels randomly
y = randi(l, [1,n]);

% result using the function to test
gen = getGenNN(x,y,k);

% result computed manually

% result memory pre-allocation
NN = zeros(n, k);

for c = 1:l % for each possible label value
    ic = find(y==c);
    xc = x(:, ic);
    % number of examples labelled as c
    nc = size(xc,2);
    % compute pairwise distances in xc
    Dist = pdist2(xc',xc');
    % ensure that the matrix is symmetric
    assert(all(vec(Dist) == vec(Dist')))

    %FIXME this look could be avoided somehow
    for i = 1:nc % for every example labelled as c
        % get the closest examples
        [~,nn] = sort(Dist(i,:));
        nn = nn(2:k+1);
        nn = ic(nn);
        NN(ic(i), :) = nn;
    end
end

% check the results
for i = 1:n
    assert(all(NN(i,:) == gen(1,gen(2,:)==i)));
end

fprintf('\t[OK]\n')

%% lmnn

fprintf('testing lmnn...\n\n')

%%% preamble

% number of examples
n = 100;
% input dimension
d = 5;
% number of different labels values, they will be taken from the interval
% [1,l]
l = 4;
% number of neighbours
k = 3;

%%% test

% generate feature vectors randomly
x = rand(d, n);
% genrate labels randomly
y = randi(l, [n,1]);

lmnn(x,y,k)

%% target neighbours simple data

x=[0 0; 0 -1; 1 1; -1 1]';
y=[0 0 1 1];
k=1;
disp('feature_matrix='), disp(x);
disp('labels vector='), disp(y);

gen = getGenNN(x,y,k);
disp('target neighbors'), disp(gen)

%% LMNN simple data

x=[0 0; 0 -1; 1 1; -1 1]';
y=[0 0 1 1];
k=1;
disp('feature_matrix='), disp(x);
disp('labels vector='), disp(y);

L = lmnn(x,y,k);
disp('L='), disp(L);

%% graphical insight

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

%% diagonal mode
% (the linear transformation L is forced to be a diagonal matrix)

%load data/wine.data;
load G:/�����ڼ�/��ѧǰ��ҵ/������/code/lmnn-master/lmnn-master/data/Wine/wine.tsv;
x = wine(:,2:end)';
y = wine(:,1)';
L = lmnn(x,y,1,'diagonal');
