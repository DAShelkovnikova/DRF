from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from materials.models import Course, Lesson



class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    lesson_course_count = SerializerMethodField()

    def get_lesson_course_count(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ('title', 'description', 'lesson_course_count')


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


