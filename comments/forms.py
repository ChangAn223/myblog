
# Create your models here.
from django import forms

class RegisterForm(forms.Form):
    nickname = forms.CharField(
        label="用户名",
        required=True,
        min_length=2,
        max_length=20,
        error_messages={
            'required': "不给自己起个名字？",
            'min_length': "用户名长度必须大于2位！",
            'max_length': "用户名长度不能超过20位！",
        },
        widget=forms.TextInput(
            attrs={
                "placeholder": "用户名",
            }
        )
    )
    pwd = forms.CharField(
        label="评论",
        required=True,
        error_messages={
            'required': "你经常不给帐号上锁吗？",
        },
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "密码",
            }
        )
    )
    repwd = forms.CharField(
        label="评论",
        required=True,
        error_messages={
            'required': "再重复输入你的密码",
        },
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "再次输入密码",
            }
        )
    )
    email = forms.EmailField(
        label="邮箱",
        required=True,
        error_messages={
            'required': "留下邮箱，晚上才好找你～",
        },
        widget=forms.TextInput(
            attrs={
                "placeholder": "邮箱",
            }
        )
    )
    # choices = [(type.id, type.name) for type in UserType.objects.all()]
    # type = forms.IntegerField(
    #     label="身份",
    #     required=True,
    #     error_messages={
    #         'required': "挑选你的身份哟～",
    #     },
    #     widget=forms.Select(
    #         choices=[choices]
    #     )
    # )


class LoginForm(forms.Form):
    user = forms.CharField(
        label="用户名",
        required=True,
        min_length=2,
        max_length=20,
        error_messages={
            'required': "你的帐号呢？",
            'min_length': "用户名长度必须大于2位！",
            'max_length': "用户名长度不能超过20位！",
        },
        widget=forms.TextInput(
            attrs={
                "placeholder": "用户名",
            }
        )
    )
    pwd = forms.CharField(
        label="评论",
        required=True,
        error_messages={
            'required': "忘记了帐号的密码吗？",
        },
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "密码",
            }
        )
    )


class CommentForm(forms.Form):
    nickname = forms.CharField(
        label="昵 称",
        required=True,
        min_length=2,
        max_length=20,
        error_messages={
            'required': "我怎么知道你是哪位呢？",
            'min_length': "用户名长度必须大于2位！",
            'max_length': "用户名长度不能超过20位！",
        },
        widget=forms.TextInput(
            attrs={
                "placeholder": "昵 称",
                "name": "nickname",
                "class": "inputText",
                "size": "16",
                "id": "username",
            }
        )
    )
    email = forms.EmailField(
        label="邮 箱",
        required=True,
        error_messages={
            'required': "留下邮箱，晚上才好找你～",
        },
        widget=forms.TextInput(
            attrs={
                "placeholder": "邮 箱",
                "name": "email",
                "class": "inputText",
                "size": "16",
                "id": "email",
            }
        )
    )
    content = forms.CharField(
        label="评 论",
        required=True,
        error_messages={
            'required': "来都来了，说两句？",
        },
        widget=forms.Textarea(
            attrs={
                "placeholder": "评论一下～",
                "name": "saytext",
                "rows": "6",
                "id": "saytext",
            }
        )
    )

