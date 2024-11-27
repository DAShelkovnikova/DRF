from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from materials.models import Course, Lesson,Subscription
from materials.validators import YouTubeValidator



class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [YouTubeValidator(field="url_video")]



class CourseDetailSerializer(ModelSerializer):
    lesson_course_count = SerializerMethodField()

    def get_lesson_course_count(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_subscription(self, course):
        user = self.context['request'].user
        return Subscription.objects.all().filter(user=user).filter(course=course).exists()

    class Meta:
        model = Course
        fields = ('title', 'description', 'lesson_course_count', 'lessons', 'subscription')


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = ("sign_of_subscription",)
