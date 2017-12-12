Iniciar API Rest

cd buscaminas/api
mkvirtualenv --python=python3.5 buscaminas
pip install -r requirements.txt
curl http://127.0.0.1:5000/generate/beginner

Iniciar Cliente Web
cd buscaminas/client
python -m SimpleHTTPServer
http://127.0.0.1:8000/index.html

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
				3: [],
				4: [],
				5: [],
				6: [],
				7: [],
				8: []
			},
			numbers: {
				1: [{
					2:1,
					...,
					...
				}],
				2: [],
				3: [],
				4: [],
				5: [],
				6: [],
				7: [],
				8: []
			},
			spaces: {
				1: [{
					3:'space',
					...,
					...
				}],
				2: [],
				3: [],
				4: [],
				5: [],
				6: [],
				7: [],
				8: []
			}
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
