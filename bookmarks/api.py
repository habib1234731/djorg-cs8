from rest_framework import serializers, viewsets
from .models import Bookmark,PersonalBookmark

class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('title','note','url')


class BookmarkViewSet(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()

class PersonalBookmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalBookmark
        fields = ('title', 'note','url')

    def create(self, validated_data):
        #import pdb: pdb.set_trace()
        user = self.context['request'].user
        personal_bookmark = PersonalBookmark.objects.create(user=user, **validated_data)
        return personal_bookmark

class PersonalBookmarkViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalBookmarkSerializer
    queryset = PersonalBookmark.objects.none()

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return PersonalBookmark.objects.none()
        else:
            return PersonalBookmark.objects.filter(user=user)