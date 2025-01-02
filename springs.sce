clear;
clc;

elements = input('No. de resortes: ');
while %t
	nodes = input('No. de nodos: ');
	if nodes > 1 then
		break
	end
end

P = input('Fuerza: ');
i = input('nodo: ');

k = zeros(elements, 1);
K = zeros(nodes, nodes);
U = zeros(nodes, 1);
u = zeros(2, 1);
R = zeros(nodes, 1);
R(i) = P;

mprintf('Constantes elasticas\n');
keq = convstr(input('¿Valores iguales de k? ', 'string'), 'l');
if keq == 'no' then
	for i = 1:elements ;
		mprintf('k [%d]', i);
		k(i) = input(': ');
	end
else
	k = input('k: ') * ones(elements, 1);
end

mprintf('Conexión nodal\n');
for i = 1: elements;
	Klocal = k(i) * [ 1 -1; -1 1];
	for j = 1:2 ;
		while %t
			mprintf('Nodo %d del elemento %d', j, i);
			lnode(j) = input(': ');
			if lnode(j) <= nodes then
				break
			end
		end
	end
	for j = 1:2 ;
		for l = 1:2 ;
			K(lnode(j), lnode(l)) = K(lnode(j), lnode(l)) + Klocal(j, l)
		end
	end
end

mprintf('Condiciones de frontera')
u = strsplit(input('Nodos empotrados (separados por comas): ', 'string'), ',')
bc = evstr(u)

subK = K
subK(:, bc) = []
subK(bc, :) = []
subR = R
subR(bc, :) = []

subU = subK \ subR

nobc = setdiff(1:length(U), bc)
for i = 1: length(nobc);
	U(nobc(i)) = subU(i)
end

R = K * U

clc
disp('K', K, 'U', U, 'R', R)

exit