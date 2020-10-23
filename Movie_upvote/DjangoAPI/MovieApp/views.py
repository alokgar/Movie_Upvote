from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from MovieApp.models import Movie
from MovieApp.serializers import MovieSerializer
# Create your views here.


@csrf_exempt
def MovieApi(request,id=0):
    if request.method=='GET':
        movies = Movie.objects.order_by('-Upvotes')
        movies_serializer = MovieSerializer(movies, many=True)
        return JsonResponse(movies_serializer.data, safe=False)
    #put api here used for upvoting
    elif request.method=='PUT':
        movie_data=JSONParser().parse(request)
        movie = Movie.objects.get(MovieId=movie_data['MovieId'])
        upvoted_movie_data = {"MovieId": movie.MovieId,
                              "MovieTitle": movie.MovieTitle,
                              "ReleaseDate":movie.ReleaseDate,
                              "Upvotes": movie.Upvotes + 1  }
        movie_serializer = MovieSerializer(movie,data=upvoted_movie_data)  
        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        print(movie_serializer.errors)
        return JsonResponse("Failed to Update.",safe=False)