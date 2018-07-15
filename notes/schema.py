from graphene_django import DjangoObjectType
import graphene
from .models import Note as NoteModel
from django.conf import settings

class Note(DjangoObjectType):
    class Meta:
        model = NoteModel
        #Describing the data as a note in a graph for GraphQL
        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):
    notes = graphene.List(Note)

    def resolve_notes(self, info):
        """Decide what notes to return"""
        user = info.context.user
        # import pdb;pdb.set_trace();
        if settings.DEBUG:
            return NoteModel.objects.all()
        elif user.is_anonymous:
            return NoteModel.objects.none()
        else:
            return NoteModel.objects.filter(user=user)

schema = graphene.Schema(query=Query)