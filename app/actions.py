# coding:utf-8
import objectpack.actions
from objectpack.actions import ObjectPack
from django.contrib.auth.models import User, ContentType, Permission, Group
from objectpack.ui import ModelEditWindow
from objectpack.slave_object_pack.actions import SlavePack
from .ui import UserAddWindow, PermissionAddWindow


class UserPack(ObjectPack):
    model = User
    add_to_desktop = True
    add_window = edit_window = UserAddWindow

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
    columns = [
        {
            'data_index': 'app_label',
            'header': 'Label',
        },
        {
            'data_index': 'model',
            'header': 'Model',
        },
        {
            'data_index': 'name',
            'header': 'Name',
        }
    ]


class TetstPack(SlavePack):
    model = Permission



class PermissionPack(ObjectPack):
    model = Permission
    add_to_desktop = True
    add_window = edit_window = ModelEditWindow.fabricate(model)
    # add_window = edit_window = PermissionAddWindow


class GroupPack(ObjectPack):
    model = Group
    add_to_desktop = True
    add_window = edit_window = ModelEditWindow.fabricate(model)
