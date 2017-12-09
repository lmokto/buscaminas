cd buscaminas/api
mkvirtualenv --python=python3.5 buscaminas
pip install -r requirements.txt
curl http://127.0.0.1:5000/generate/beginner

cd buscaminas/client
python -m SimpleHTTPServer
http://127.0.0.1:8000/index.html

"""
Analisis basico

API REST - flask python
Cliente - JavaScript angular, jquery y CSS
Base de datos - sqlite

Nivel principiante: 8 × 8 casillas y 10 minas.
Nivel intermedio: 16 × 16 casillas y 40 minas.
Nivel experto: 16 × 30 casillas y 99 minas.

1. ingreso y se dibuja el buscamina

    get endpoint generate/beginner
    get endpoint generate/intermediate

	endpoint generate de buscamina con id
		{
			id: 1,
			dimension: {'row':8 , 'clm':8}
			mines: [
				{ 'row': 1, 'clm:' [4] },
				{ 'row': 2, 'clm:' [4, 5, 7] },
				{ 'row': 3, 'clm:' [4, 5, 7] },
				{ 'row': 4, 'clm:' [4, 5, 7] },
				{ 'row': 5, 'clm:' [4, 5, 7] },
				{ 'row': 6, 'clm:' [4, 5, 7] },
				{ 'row': 7, 'clm:' [4, 5, 7] },
				{ 'row': 8, 'clm:' [4, 5, 7] },
				{ 'row': 9, 'clm:' [4, 5, 7] }
			],
			numbers: [
				{ 'row': 1, 'clm:' [] },
				{ 'row': 2, 'clm:' [] },
				{ 'row': 3, 'clm:' [4, 5, 7] },
				{ 'row': 4, 'clm:' [4, 5, 7] },
				{ 'row': 5, 'clm:' [4, 5, 7] },
				{ 'row': 6, 'clm:' [4, 5, 7] },
				{ 'row': 7, 'clm:' [4, 5, 7] },
				{ 'row': 8, 'clm:' [4, 5, 7] },
				{ 'row': 9, 'clm:' [4, 5, 7] }
			],
			spaces: [
				{ 'row': 1, 'clm:' [1,2,3,] },
				{ 'row': 2, 'clm:' [4, 5, 7] },
				{ 'row': 3, 'clm:' [4, 5, 7] },
				{ 'row': 4, 'clm:' [4, 5, 7] },
				{ 'row': 5, 'clm:' [4, 5, 7] },
				{ 'row': 6, 'clm:' [4, 5, 7] },
				{ 'row': 7, 'clm:' [4, 5, 7] },
				{ 'row': 8, 'clm:' [4, 5, 7] },
				{ 'row': 9, 'clm:' [4, 5, 7] }
			]
		}

	endpoint tiempo de la partida con id del buscamina

		{
			id:1,
			start: 16:16:07,
			end : 16:15:30
		}

2. incio el juego al dar click sobre el buscamina (inicia el tiempo al comenzar el juego)
3. itero sobre el juego (el tiempo continua corriendo)

4. tengo un resultado , ganar o perder, (finaliza el tiempo del juego)
	actualizo endpoint (id buscamina, inicio, fin)

"""


