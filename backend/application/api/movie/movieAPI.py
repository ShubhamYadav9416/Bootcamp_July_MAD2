from flask import request, jsonify
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from flask_jwt_extended import jwt_required


from application.data.model import db, Movie

movie_post_args = reqparse.RequestParser()
movie_post_args.add_argument('movie_name', type= str, required = True, help = "Movie name is required")
movie_post_args.add_argument('movie_tag', type= str, required = True, help = "Movie tag is required")

movie_put_args = reqparse.RequestParser()
movie_put_args.add_argument('movie_name', type= str)
movie_put_args.add_argument('movie_tag', type= str)


resource_fields = {
    'movie_id' : fields.Integer,
    'movie_name' : fields.String,
    'movie_tag' : fields.String
}


class AllMovieAPI(Resource):
    @marshal_with(resource_fields)
    @jwt_required()
    def get(resourse):
        movies = Movie.query.all()
        return movies, 200
     
    @marshal_with(resource_fields)
    @jwt_required()
    def post(resource):
        args = movie_post_args.parse_args()
        movie = Movie.query.filter_by(movie_name = args['movie_name']).first()
        if movie:
            abort(409, message = "movie is already exist")
        input = Movie(movie_name = args["movie_name"], movie_tag = args["movie_tag"])
        db.session.add(input)
        db.session.commit()
        return input,201



class MovieAPI(Resource):
    @marshal_with(resource_fields)
    @jwt_required()
    def get(self,movie_id):
        movie = Movie.query.filter_by(movie_id = movie_id).first()
        if not movie:
            abort(404, message="Could not found movie with this id")
        return movie, 200
    
    @marshal_with(resource_fields)
    @jwt_required()
    def put(self,movie_id):
        args = movie_put_args.parse_args()
        movie = Movie.query.filter_by(movie_id = movie_id).first()
        if not movie:
            abort(404, message="Could not found movie with this id")
        if args["movie_name"]:
            movie.movie_name = args["movie_name"]
        if args["movie_tag"]:
            movie.movie_tag = args["movie_tag"]
        db.session.commit()
        return movie
            
        
    @jwt_required()
    def delete(self,movie_id):
        args = movie_put_args.parse_args()
        movie = Movie.query.filter_by(movie_id = movie_id).first()
        if not movie:
            abort(404, message="Could not found movie with this id") 
        db.session.delete(movie)
        db.session.commit()
        return jsonify({'message' : 'Movie has been deleted'})
    
        