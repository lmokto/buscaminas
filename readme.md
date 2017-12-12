1. Iniciar API Rest


```
cd buscaminas/api
mkvirtualenv --python=python3.5 buscaminas
pip install -r requirements.txt
curl http://127.0.0.1:5000/api/generate/beginner
```

2.  Iniciar Cliente Web
```

1. cd buscaminas/client
2. python -m SimpleHTTPServer
3. http://127.0.0.1:8000/index.html
```


*  Analisis basico

> API REST - flask python
> Cliente - JavaScript angular, jquery y CSS
> Base de datos - sqlite

> Nivel principiante: 8 × 8 casillas y 10 minas.
> Nivel intermedio: 16 × 16 casillas y 40 minas.
> Nivel experto: 16 × 30 casillas y 99 minas.

1. ingreso y se dibuja el buscamina

    Get endpoint generate/beginner
    Get endpoint generate/intermediate

	endpoint generate de buscamina con id
	```
		{
			dimension: {
				clm: 8,
				row: 8
			},
			id: 1,
			mines: {
				1: [{
					1:true,
					...,
					...
				}],
				2: [],
				...,
				...
			},
			numbers: {
				1: [{
					2:1,
					...,
					...
				}],
				2: [],
				...,
				...
			},
			spaces: {
				1: [{
					3:'space',
					...,
					...
				}],
				2: [],
				...,
				...
			}
		}
    ```

	endpoint tiempo de la partida con id del buscamina
    ```
		{
			id:1,
			start: 16:16:07,
			end : 16:15:30
		}
    ```

2. incio el juego al dar click sobre el buscamina (inicia el tiempo al comenzar el juego)

3. itero sobre el juego (el tiempo continua corriendo)

4. tengo un resultado , ganar o perder, (finaliza el tiempo del juego)
	actualizo endpoint (id buscamina, inicio, fin)
