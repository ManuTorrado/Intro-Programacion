-- 1)

longitud :: [t] -> Integer
longitud [] =   0
longitud (_:xs) = 1 + longitud xs  

-- 2) 
ultimo :: [t] -> t
ultimo  [x] = x -- El [x] significa que tiene un solo elemento
ultimo (x:xs)	=  ultimo (xs)

-- 3) 
principio :: [t] -> [t] 
principio [x] = [x]
principio (x:xs) =  [x]

-- 4)
reverso :: [t] -> [t]
reverso [x] = [x]
reverso (x:xs) = reverso xs ++ [x]

-- Ejercicio 2), 1
pertenece ::  (Eq t) => t -> [t] -> Bool
pertenece x [] = False
pertenece x [y]    | (x == y) = True
pertenece x [y]    | not (x == y) = False
pertenece x (y:ys) | y == x = True 
pertenece x (y:ys) | otherwise = pertenece x ys

-- Ejercicio 2), 2
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = False
todosIguales [x] =  True 
todosIguales (x:xs) | not (x == (head xs)) = False
todosIguales (x:xs) | otherwise = todosIguales xs

-- Ejercicio 3), 3

-- Esto iba a ser una funcion auxiliar
esIgualAlResto :: (Eq t) => t -> [t] -> Bool
esIgualAlResto x (y:ys) | not (x==y) = False
esIgualAlResto x [y]    | x == y = True
esIgualAlResto x (y:ys) | otherwise = esIgualAlResto x ys

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:xs)   | (pertenece x xs) = False
                        | otherwise = todosDistintos xs


-- 3,3)
maximo :: [Integer] -> Integer 
maximo [x] = x
maximo (x:xs) | maximo (xs) <= x = x
maximo (x:xs) | otherwise = maximo xs



-- 3, 9) Ordenar
maximoDe :: Integer -> [Integer] -> Bool
maximoDe x y = (maximo y) == x 

--Borra el primer elemento que encuentra
borrar :: Integer -> [Integer] -> [Integer]
borrar x y      | not (pertenece x y) = y 
borrar x (y:ys) | x == y = ys
               	| otherwise =  [y] ++ borrar x ys

 
ordenar :: [Integer] -> [Integer]
ordenar xs | xs == [] = []
	         | otherwise = ordenar (borrar (maximo xs) xs) ++ [maximo xs]



-- 4. 4 

primeraPalabra :: [Char] -> [Char]
primeraPalabra [] = []
primeraPalabra (x:xs) | not (x == ' ') = x : primeraPalabra xs
                      | otherwise = []

--palabras :: [Char] -> [[Char]]
--palabras [] = []
--palabras (x:xs) | not (x == ' ') = x + palabras xs 
--              | otherwise = x : 
                 

-- 4, 5)
aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (x:xs) = x ++ aplanar xs
