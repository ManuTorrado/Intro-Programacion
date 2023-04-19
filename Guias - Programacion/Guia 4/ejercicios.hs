fibonacci :: Integer->Integer
fibonacci n | n == 0 = 0
	          | n == 1 = 1
					  | otherwise = fibonacci(n-1) + fibonacci(n-2) 

parteEntera :: Float -> Integer
parteEntera x | x >= 0 && x < 1 = 0    
	            | otherwise  =  1 + parteEntera(x-1) 

esDivisible :: Integer -> Integer-> Bool
esDivisible x y | x < y = False
							  | (x==y) = True
							  | otherwise = esDivisible (x-y) (y)

-- Funcion auxiliar, te devuelve el enesimo impar que le pidas
imparNumero :: Integer -> Integer 
imparNumero x | x == 1 = 1
              | otherwise = 2 + imparNumero(x-1)

sumaImpares :: Integer -> Integer 
sumaImpares x | x == 1 = 1 
	            | otherwise = imparNumero(x) + sumaImpares(x-1)


-- Ejercicio 5
factorial :: Integer -> Integer 
factorial x | x == 0 = 1
					  | otherwise = factorial(x-1) * x

medioFact :: Integer -> Integer
medioFact x | x == 0 = 1
				    | x == 1 = 1
					  | otherwise = x * medioFact(x-2)

-- Ejercicio 6
sumaDigitos :: Integer -> Integer
sumaDigitos x | x < 10 = x
	            |otherwise = x `mod` 10 + sumaDigitos(x `div` 10) 