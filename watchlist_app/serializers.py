from datetime import datetime

from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import Review, StreamPlatform, WatchList


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ['watchlist', ]


class WatchListSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)
    created = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S.%f', input_formats=['%Y-%m-%d %H:%M:%S.%f'])

    class Meta:
        model = WatchList
        fields = "__all__"

    @staticmethod
    def validate_name(value):
        if len(value) < 2:
            raise ValidationError('too short name')
        else:
            return value

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            datetime.strptime(representation['created'], '%Y-%m-%d %H:%M:%S.%f')
        except ValueError:
            representation['created'] = "Invalid datetime"
        return representation

    @staticmethod
    def validate_created(value):
        # Convert datetime object to string if necessary.
        value_str = value.strftime('%Y-%m-%d %H:%M:%S.%f') if isinstance(value, datetime) else value

        # Validate the string format
        try:
            datetime.strptime(value_str, '%Y-%m-%d %H:%M:%S.%f')
            return value_str
        except ValueError:
            raise serializers.ValidationError("Incorrect data format, should be YYYY-MM-DD HH:MM:SS.ssssss")

    def validate(self, data):
        if data['title'] == data['storyline']:
            raise serializers.ValidationError('not be same')
        else:
            return data

    @staticmethod
    def get_len_name(obj):
        length = len(obj.title)
        return length


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movie_detail')

    class Meta:
        model = StreamPlatform
        fields = "__all__"
