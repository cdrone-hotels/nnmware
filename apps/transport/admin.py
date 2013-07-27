# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from nnmware.apps.transport.models import VehicleColor, VehicleKind, VehicleTransmission, VehicleCarcass, VehicleEngine, VehicleFeature, VehicleMark, VehicleVendor
from nnmware.core.admin import ColorAdmin


class VehicleBaseParamAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_in_list', 'slug')
    fieldsets = (
        (_('Type of vehicle'), {"fields": [('name', 'order_in_list'),
                                ('description',)]}),
        (_("English"), {"classes": ("grp-collapse grp-closed",),
                        "fields": [("name_en",), ("description_en",), ]}),)
    ordering = ('-order_in_list', 'name',)


class VehicleKindAdmin(VehicleBaseParamAdmin):
    pass


class VehicleBaseParamForAdmin(VehicleBaseParamAdmin):
    fieldsets = (
        (_('Type of vehicle'), {"fields": [('name', 'order_in_list'), ('type_vehicles', ),
                                ('description',)]}),
        (_("English"), {"classes": ("grp-collapse grp-closed",),
                        "fields": [("name_en",), ("description_en",), ]}),)


class VehicleTransmissionAdmin(VehicleBaseParamForAdmin):
    pass


class VehicleCarcassAdmin(VehicleBaseParamForAdmin):
    pass


class VehicleEngineAdmin(VehicleBaseParamForAdmin):
    pass


class VehicleFeatureAdmin(VehicleBaseParamForAdmin):
    pass


class VehicleMarkAdmin(VehicleBaseParamForAdmin):
    pass


class VehicleVendorAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Vendor'), {'fields': [('name', 'country', 'website'), ('description',)]}),
        (_('English'), {'fields': [('name_en', )]}),
    )
    list_display = ('name', 'country', 'website')


admin.site.register(VehicleColor, ColorAdmin)
admin.site.register(VehicleKind, VehicleKindAdmin)
admin.site.register(VehicleTransmission, VehicleTransmissionAdmin)
admin.site.register(VehicleCarcass, VehicleCarcassAdmin)
admin.site.register(VehicleEngine, VehicleEngineAdmin)
admin.site.register(VehicleFeature, VehicleFeatureAdmin)
admin.site.register(VehicleMark, VehicleMarkAdmin)
admin.site.register(VehicleVendor, VehicleVendorAdmin)
