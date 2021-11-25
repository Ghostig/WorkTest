# coding:utf-8
from objectpack.actions import ObjectPack
from django.contrib.auth.models import User, ContentType, Permission, Group
from objectpack.ui import ModelEditWindow
import app.ui
from app.controller import observer


class UserPack(ObjectPack):
    model = Usergit
    add_to_desktop = True
    add_window = edit_window = app.ui.UserAddWindow

    columns = [
        {
            'data_index': 'username',
            'header': u'Username',
        },
        {
            'data_index': 'first_name',
            'header': u'First name',
        },
        {
            'data_index': 'last_name',
            'header': u'Last name',
        }
    ]


class ContentTypePack(ObjectPack):
    model = ContentType
    add_to_desktop = True
    add_window = edit_window = ModelEditWindow.fabricate(model)


class PermissionPack(ObjectPack):
    model = Permission
    _is_primary_for_model = True
    add_to_desktop = True
    parents = ['content type']
    add_window = edit_window = ModelEditWindow.fabricate(
        model,
        model_register=observer
    )


class GroupPack(ObjectPack):
    model = Group
    add_to_desktop = True
    add_window = edit_window = ModelEditWindow.fabricate(model)
