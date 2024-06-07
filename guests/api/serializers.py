from rest_framework import serializers

from guests.models import Entry, User


class EntryItemSerializer(serializers.Serializer):  # serializer for Entry
    subject = serializers.CharField(max_length=255, required=True)
    message = serializers.CharField(max_length=255, required=True)


class CreateEntrySerializer(serializers.Serializer):  # serializer for Creating Entry
    username = serializers.CharField(max_length=127)
    user_entry = EntryItemSerializer()  # using nested serializer

    def create(self, validated_data):
        user, _ = User.objects.get_or_create(username=validated_data["username"])
        return Entry.objects.create(
            user=user,
            subject=validated_data["user_entry"]["subject"],
            message=validated_data["user_entry"]["message"],
        )


class EntrySerializer(serializers.ModelSerializer):  # serializer for list entries

    username = serializers.CharField(source="user.username")
    # to show user's username

    class Meta:
        model = Entry
        fields = ["username", "subject", "message"]
        # take Entry model and return its all fields to the json format


class UserSerializer(serializers.ModelSerializer):
    # user can be created without entry

    class Meta:
        model = User
        fields = ["username"]
        # take User model and return its all fields to the json format
