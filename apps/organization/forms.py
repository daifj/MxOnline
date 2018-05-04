# _*_ coding: utf-8 _*_
import re

from django import forms

from operation.models import UserAsk


class UserAskForm(forms.ModelForm):
    '''用modelform'''
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        '''
        验证手机号码是否合法
        '''
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[3|4|5|7|8][0-9]{9}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError('手机号码非法', code='mobile_invalid')