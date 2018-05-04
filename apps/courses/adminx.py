# _*_ coding: utf-8 _*_
from .models import Course, Video, Lesson, CourseResource, BannerCourse
from organization.models import CourseOrg
import xadmin


class LessonInline(object):
    '''章节嵌套'''
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
                    'click_nums','get_zj_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'add_time']
    # 默认排序设置
    ordering = ['-click_nums']
    # 设置只读字段
    readonly_fields = ['click_nums']
    # 隐藏字段
    exclude = ['fav_nums']
    # 设置搜索
    relfield_style = 'fk-ajax'
    # 编辑
    list_editable = ['degree', 'desc']
    inlines = [LessonInline, CourseResourceInline]
    # 设置自动刷新
    refresh_times = [3, 5]
    style_fields = {'detail': 'ueditor'}
    import_excel = True

    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()

    def post(self, request, *args, **kwargs):
        # 导入excel文件
        if 'excel' in request.FILES:
            pass
        return super(CourseAdmin, self).post(request, args, kwargs)


class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'add_time']
    # 默认排序设置
    ordering = ['-click_nums']
    # 设置只读字段
    readonly_fields = ['click_nums']
    # 隐藏字段
    exclude = ['fav_nums']
    # 设置搜索
    relfield_style = 'fk-ajax'
    inlines = [LessonInline, CourseResourceInline]
    style_fields = {'detail': 'ueditor'}

    # 过滤轮播图
    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()

class LessonAdmin(object):
    list_display = ['course', 'name', 'learn_times', 'add_time']
    search_fields = ['course', 'name', 'learn_times']
    list_filter = ['course__name', 'name','learn_times', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name','learn_times', 'add_time']
    search_fields = ['lesson', 'name', 'learn_times']
    list_filter = ['lesson__name', 'name','learn_times', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name','download',  'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)