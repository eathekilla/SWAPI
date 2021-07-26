# SWAPI
StarWars API

## Instalar Dependencias
```
pip install -r requirements.txt
```
Crear un archivo .env

```
virtualenv env
```
```
env\Scripts\activate
```
Ejecutar migraciones
```
python manage.py makemigrations
python manage.py migrate
```
Cargar fixtures
```
python manage.py loaddata planets
python manage.py loaddata people
python manage.py loaddata directors
python manage.py loaddata producers
python manage.py loaddata films
```

Correr el servidor

```
python manage.py runserver
```

### Nota
Se puede filtrar por nombre y agregar, planetas y personajes, sin embargo no realicé pruebas unitarias debido a que no tengo conocimientos en pruebas unitarias con este framewokrk

### Ejemplos de querys y mutaciones.
```
mutation createmutation{
  createPlanet(planetData:{id:400,created: "2014-12-09T13:50:49.641Z",
            modified: "2014-12-20T20:58:18.411Z",
            name: "La Tierra",
            rotationPeriod: "24",
            orbitalPeriod: "364",
            diameter: "10465",
            climate: "humedo",
            gravity: "1 standard",
            terrain: "desert",
            surfaceWater: "1",
            population: "200000"}){
    planet{
      id,
      name,
      rotationPeriod,
      orbitalPeriod,
      diameter,
      climate,
      gravity,
      terrain,
      surfaceWater,
      population
    }
  }
}
```


```
mutation createmutation{
  updatePlanet(planetData:{id:60,created: "2014-12-09T13:50:49.641Z",
            modified: "2014-12-20T20:58:18.411Z",
            name: "La Tierra",
            rotationPeriod: "24",
            orbitalPeriod: "364",
            diameter: "10465",
            climate: "humedo",
            gravity: "1 standard",
            terrain: "desert",
            surfaceWater: "1",
            population: "200000"}){
    planet{
      id,
      name,
      rotationPeriod,
      orbitalPeriod,
      diameter,
      climate,
      gravity,
      terrain,
      surfaceWater,
      population
    }
  }
}
```



```
mutation createmutation{
  createPeople(peopleData:{
    id:40,
    name:"Esteban",
    height:  "100"
    mass:  "100"
    hairColor:  "gray"
    skinColor: "blue"
    eyeColor: "blue"
    birthYear: "2000"
    gender:  "male"
    homeworld: 3}){
    people{
      id,
      name,
      height,
      mass,
      hairColor,
      skinColor,
      eyeColor,
      birthYear,
      gender,
      homeworld{
        id
      }
    }
  }
}
```
```
mutation createmutation{
  updatePeople(peopleData:{
    id:2,
    name:"Esteban",
    height:  "100"
    mass:  "100"
    hairColor:  "gray"
    skinColor: "blue"
    eyeColor: "blue"
    birthYear: "2000"
    gender:  "male"
    homeworld: 3}){
    people{
      id,
      name,
      height,
      mass,
      hairColor,
      skinColor,
      eyeColor,
      birthYear,
      gender,
      homeworld{
        id
      }
    }
  }
}
```

```
mutation createmutation{
  deletePeople(id:2){
    people{
      id
    }
  }
}
```
```
query{
  fltName(name_Icontains: "luke") {
    edges {
      node {
        id,
        name
      }
    }
  }
}
```
```
query{
  allPeople{
    name,
    films {
      edges {
        node {
          title
        }
      }
    }
  }
}
```
