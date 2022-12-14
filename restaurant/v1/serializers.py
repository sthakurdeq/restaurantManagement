from rest_framework import serializers

from restaurant.models import Item, Menu, Ratings, Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    """
    Restaurant serializer with fields to controll displayed fields
    fields: id, name, state, city, country, street
    """

    class Meta:
        model = Restaurant
        fields = ["id", "name", "state", "city", "country", "street"]


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop("fields", None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class MenuSerializer(DynamicFieldsModelSerializer):
    """
    Menu serializer with fields to controll displayed fields
    fields: id, restaurants, day, vote, item, items
    """

    items = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ["id", "restaurants", "day", "item", "items"]

    def get_items(self, obj):
        """
        Method that returns id,name of items
        """
        return obj.item.all().values("id", "name")


class ItemSerializer(serializers.ModelSerializer):
    """
    Item serializer with fields to controll displayed fields
    fields: id, name, type, descripion
    """

    class Meta:
        model = Item
        fields = ["id", "name", "type", "description"]


class RatingSerializer(serializers.ModelSerializer):
    """
    Rating serializer with fields to controll displayed fields
    fields: menu, timestamp, user, rating
    """

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    vote_value = serializers.IntegerField(source="vote")

    class Meta:
        model = Ratings
        fields = ["id", "menu", "user", "vote_value"]


class ListRatingSerializer(serializers.ModelSerializer):
    """
    Rating serializer with fields to controll displayed fields.
    fields: id, menu, user, rating
    """

    # user = serializers.CharField(source="user.username")
    menu_id = serializers.CharField(source="menu")
    total_vote = serializers.IntegerField()

    class Meta:
        model = Ratings
        fields = ["id", "menu_id", "total_vote"]
