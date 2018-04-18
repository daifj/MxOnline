from courses.models import Course, Lesson
from .models import EmailVerifyRecord, Banner
import xadmin
from xadmin import views


class BaseSetting(object):
    enable_themes = True    # 设置主题
    use_bootswatch = True


class GlobalSettings(object):
    '''设置后台标题及footer'''
    site_title = '米线后台管理系统'
    site_footer = '米线在线网'
    menu_style = 'accordion'    # 折叠菜单


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    # 修改icon
    model_icon = 'fa fa-envelope'


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)