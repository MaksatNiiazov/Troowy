from rest_framework import serializers

from apps.pages.models import StaticPage, WelcomeProperty, WelcomeCars, WelcomeTours, WelcomeInternationalTours, \
    WelcomeMedicalTours, WelcomePropertyImage, WelcomeCarsImage, WelcomeToursImage, WelcomeInternationalToursImage, \
    WelcomeMedicalToursImage


class StaticPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaticPage
        fields = ['title', 'slug', 'content', 'image']


class WelcomePropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WelcomePropertyImage
        fields = ['id', 'image', ]


class WelcomeBaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'title', 'content', 'images']


class WelcomePropertySerializer(WelcomeBaseSerializer):
    images = WelcomePropertyImageSerializer(many=True, read_only=True)

    class Meta(WelcomeBaseSerializer.Meta):
        model = WelcomeProperty
        fields = '__all__'


class WelcomeCarsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WelcomeCarsImage
        fields = ['id', 'image', ]


class WelcomeCarsSerializer(WelcomeBaseSerializer):
    images = WelcomeCarsImageSerializer(many=True, read_only=True)

    class Meta(WelcomeBaseSerializer.Meta):
        model = WelcomeCars
        fields = '__all__'


class WelcomeToursImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WelcomeToursImage
        fields = ['id', 'image', ]


class WelcomeToursSerializer(WelcomeBaseSerializer):
    images = WelcomeToursImageSerializer(many=True, read_only=True)

    class Meta(WelcomeBaseSerializer.Meta):
        model = WelcomeTours
        fields = '__all__'


class WelcomeInternationalToursImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WelcomeInternationalToursImage
        fields = ['id', 'image', ]


class WelcomeInternationalToursSerializer(WelcomeBaseSerializer):
    images = WelcomeInternationalToursImageSerializer(many=True, read_only=True)

    class Meta(WelcomeBaseSerializer.Meta):
        model = WelcomeInternationalTours
        fields = '__all__'


class WelcomeMedicalToursImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WelcomeMedicalToursImage
        fields = ['id', 'image', ]


class WelcomeMedicalToursSerializer(WelcomeBaseSerializer):
    images = WelcomeMedicalToursImageSerializer(many=True, read_only=True)

    class Meta(WelcomeBaseSerializer.Meta):
        model = WelcomeMedicalTours
        fields = '__all__'
