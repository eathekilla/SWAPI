import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Planet,People,Film,Director,Producer
from graphene import Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField



class Connection(graphene.Connection):
    class Meta:
        abstract = True

    total_count = graphene.Int()

    def resolve_total_count(self, info):
        return self.length


###############Director and Producer##############
class DirectorType(DjangoObjectType):
    class Meta:
        model = Director
        interfaces = (Node,)
        
        filter_fields = {'name': ['exact', 'icontains', 'istartswith']}
        connection_class = Connection
        fileds = "__all__"


class ProducerInput(graphene.InputObjectType):
    id = graphene.ID()
    name =  graphene.String()

class ProducerType(DjangoObjectType):
    class Meta:
        model = Producer
        interfaces = (Node,)
        
        filter_fields = {'name': ['exact', 'icontains', 'istartswith']}
        connection_class = Connection
        fileds = "__all__"


class DirectorInput(graphene.InputObjectType):
    id = graphene.ID()
    name =  graphene.String()



################Planet###########################

class PlanetType(DjangoObjectType):
    class Meta:
        model = Planet
        fields = "__all__"
        # filter_fields = ('name')
        connection_class = Connection
        filter_fields = {'name': ['exact', 'icontains', 'istartswith']}
        exclude_fields = ('created', 'modified')


class PlanetInput(graphene.InputObjectType):
    id = graphene.ID()
    created =  graphene.String()
    modified =  graphene.String()
    name =  graphene.String()
    rotation_period =  graphene.String()
    orbital_period =  graphene.String()
    diameter =  graphene.String()
    climate =  graphene.String()
    gravity =  graphene.String()
    terrain =  graphene.String()
    surface_water =  graphene.String()
    population =  graphene.String()


class CreatePlanet(graphene.Mutation):
    class Arguments:
        planet_data = PlanetInput(required=True)

    planet = graphene.Field(PlanetType)

    @staticmethod
    def mutate(root, info, planet_data=None):
        planet_instance = Planet( 
            created =  planet_data.created,
            modified =  planet_data.modified,
            name =  planet_data.name,
            rotation_period =  planet_data.rotation_period,
            orbital_period =  planet_data.orbital_period,
            diameter =  planet_data.diameter,
            climate =  planet_data.climate,
            gravity =  planet_data.gravity,
            terrain =  planet_data.terrain,
            surface_water =  planet_data.surface_water,
            population =  planet_data.population
        )
        planet_instance.save()
        return CreatePlanet(planet=planet_instance)

class UpdatePlanet(graphene.Mutation):
    class Arguments:
        planet_data = PlanetInput(required=True)

    planet = graphene.Field(PlanetType)

    @staticmethod
    def mutate(root, info, planet_data=None):

        planet_instance = Planet.objects.get(pk=planet_data.id)

        if planet_instance:
            planet_instance.created =  planet_data.created,
            planet_instance.modified =  planet_data.modified,
            planet_instance.name =  planet_data.name,
            planet_instance.rotation_period =  planet_data.rotation_period,
            planet_instance.orbital_period =  planet_data.orbital_period,
            planet_instance.diameter =  planet_data.diameter,
            planet_instance.climate =  planet_data.climate,
            planet_instance.gravity =  planet_data.gravity,
            planet_instance.terrain =  planet_data.terrain,
            planet_instance.surface_water =  planet_data.surface_water,
            planet_instance.population =  planet_data.population
            return UpdatePlanet(planet=planet_instance)
        return UpdatePlanet(planet=None)

class DeletePlanet(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    planet = graphene.Field(PlanetType)

    @staticmethod
    def mutate(root, info, id):
        planet_instance = Planet.objects.get(pk=id)
        planet_instance.delete()

        return None
####################################3

class PeopleType(DjangoObjectType):
    class Meta:
        model = People
        interfaces = (Node,)
        exclude_fields = ('created', 'modified')
        filter_fields = {'name': ['exact', 'icontains', 'istartswith']}
        connection_class = Connection
        fileds = "__all__"


class PeopleInput(graphene.InputObjectType):
    id = graphene.ID()
    created =  graphene.String()
    modified =  graphene.String()
    name =  graphene.String()
    height =  graphene.String()
    mass =  graphene.String()
    hair_color =  graphene.String()
    skin_color =  graphene.String()
    eye_color =  graphene.String()
    birth_year =  graphene.String()
    gender =  graphene.String()
    homeworld = graphene.Int()

class CreatePeople(graphene.Mutation):
    class Arguments:
        people_data = PeopleInput(required=True)
    people = graphene.Field(PeopleType)
    

    @staticmethod
    def mutate(root, info, people_data=None):
        homeworld= int(people_data.homeworld)
        homeworld = Planet._meta.model.objects.get(id=homeworld)
        people_instance = People( 
            created =  people_data.created,
            modified =  people_data.modified,
            name =  people_data.name,
            height =  people_data.height,
            mass =  people_data.mass,
            hair_color =  people_data.hair_color,
            skin_color =  people_data.skin_color,
            eye_color =  people_data.eye_color,
            birth_year =  people_data.birth_year,
            gender =  people_data.gender,
            homeworld =  homeworld
        )
        people_instance.save()
        return CreatePeople(people=people_instance)

class UpdatePeople(graphene.Mutation):
    class Arguments:
        people_data = PeopleInput(required=True)

    people = graphene.Field(PeopleType)

    @staticmethod
    def mutate(root, info, people_data=None):
        homeworld= int(people_data.homeworld)
        homeworld = Planet._meta.model.objects.get(id=homeworld)
        people_instance = People.objects.get(pk=people_data.id)

        if people_instance:
            people_instance.created =  people_data.created,
            people_instance.modified =  people_data.modified,
            people_instance.name =  people_data.name,
            people_instance.height =  people_data.height,
            people_instance.mass =  people_data.mass,
            people_instance.hair_color =  people_data.hair_color,
            people_instance.skin_color =  people_data.skin_color,
            people_instance.eye_color =  people_data.eye_color,
            people_instance.birth_year =  people_data.birth_year,
            people_instance.gender =  people_data.gender,
            people_instance.homeworld =  homeworld
            return UpdatePeople(people=people_instance)
        return UpdatePeople(people=None)



class DeletePeople(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    people = graphene.Field(PeopleType)

    @staticmethod
    def mutate(root, info, id):
        people_instance = People.objects.get(pk=id)
        people_instance.delete()

        return None


#####################Films#################
class FilmType(DjangoObjectType):
    class Meta:
        model = Film
        interfaces = (Node,)
        exclude_fields = ('created', 'modified')
        filter_fields = {'title': ['exact', 'icontains', 'istartswith']}
        connection_class = Connection
        fileds = "__all__"

class FilmInput(graphene.InputObjectType):
    id = graphene.ID()
    created =  graphene.String()
    modified =  graphene.String()
    title = graphene.String()
    episode_id = graphene.Int()
    opening_crawl = graphene.String()
    director = graphene.List(DirectorInput)
    producer = graphene.List(ProducerInput)
    release_date = graphene.String()
    characters = graphene.List(PeopleInput)
    planets = graphene.List(PlanetInput)

class CreateFilm(graphene.Mutation):
    class Arguments:
        film_data = FilmInput(required=True)
    film = graphene.Field(FilmType)
    

    @staticmethod
    def mutate(root, info, film_data=None):
        director = int(film_data.director)
        director = Director._meta.model.objects.get(id=director)
        producer = int(film_data.producer)
        producer = Director._meta.model.objects.get(id=producer)
        film_instance = Film( 
            created =  film_data.created,
            modified =  film_data.modified,
            title =  film_data.title,
            episode_id =  film_data.episode_id,
            opening_crawl =  film_data.opening_crawl,
            director =  director,
            producer =  producer,
            release_date =  film_data.release_date,
            characters =  film_data.characters,
            planets =  film_data.planets,
        )
        film_instance.save()
        film_instance.characters.set()
        return CreateFilm(film=film_instance)


class UpdateFilm(graphene.Mutation):
    class Arguments:
        film_data = FilmInput(required=True)

    film = graphene.Field(FilmType)

    @staticmethod
    def mutate(root, info, film_data=None):
        director = int(film_data.director)
        director = Director._meta.model.objects.get(id=director)
        producer = int(film_data.producer)
        producer = Director._meta.model.objects.get(id=producer)
        film_instance = Film.objects.get(pk=film_data.id)

        if film_instance:
            film_instance.created =  film_data.created,
            film_instance.modified =  film_data.modified,
            film_instance.title =  film_data.title,
            film_instance.episode_id =  film_data.episode_id,
            film_instance.opening_crawl =  film_data.opening_crawl,
            film_instance.director =  director,
            film_instance.producer =  producer,
            film_instance.release_date =  film_data.release_date,
            film_instance.characters =  film_data.characters,
            film_instance.planets =  film_data.planets,
            return UpdateFilm(film=film_instance)
        return UpdateFilm(film=None)


class DeleteFilm(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    people = graphene.Field(FilmType)

    @staticmethod
    def mutate(root, info, id):
        people_instance = Film.objects.get(pk=id)
        people_instance.delete()

        return None

#############################################33
class Query(graphene.ObjectType):
    all_planets = graphene.List(PlanetType)
    planet = graphene.Field(PlanetType, planet_id = graphene.Int())

    def resolve_all_planets(self,inf, **kwargs):
        return Planet.objects.all()
    
    def resolve_planet(self,info,planet_id):
        return Planet.object.get(pk=planet_id)

    all_people = graphene.List(PeopleType)
    flt_name = DjangoFilterConnectionField(PeopleType)#graphene.List(PeopleType)
    people = graphene.Field(PeopleType,people_id=graphene.Int())

    def resolve_all_people(self,inf, **kwargs):
        return People.objects.all()
    
    def resolve_people(self,info,people_id):
        return People.objects.get(pk=people_id)

    all_film = graphene.List(FilmType)
    film = graphene.Field(FilmType,film_id=graphene.Int())

    def resolve_all_film(self,inf, **kwargs):
        return Film.objects.all()
    
    def resolve_film(self,info,people_id):
        return Film.objects.get(pk=people_id)

class Mutation(graphene.ObjectType):
    create_planet = CreatePlanet.Field()
    delete_planet= DeletePlanet.Field()
    update_planet = UpdatePlanet.Field()

    create_people = CreatePeople.Field()
    update_people = UpdatePeople.Field()
    delete_people = DeletePeople.Field()

    create_film = CreateFilm.Field()
    update_film  = UpdateFilm.Field()
    delete_film  = DeleteFilm.Field()

schema = graphene.Schema(query=Query,mutation=Mutation)