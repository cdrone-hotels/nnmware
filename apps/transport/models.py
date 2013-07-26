# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from nnmware.apps.address.models import Country
from nnmware.core.abstract import AbstractColor, AbstractName, AbstractVendor, AbstractDate
from nnmware.apps.business.models import AbstractSeller


class VehicleColor(AbstractColor):
    pass


class VehicleKind(AbstractName):
    pass

    class Meta:
        verbose_name = _('Vehicle type')
        verbose_name_plural = _('Vehicle types')


class VehicleTransmission(AbstractName):
    type_vehicles = models.ManyToManyField(VehicleKind, verbose_name=_('Using in vehicles'), blank=True, null=True)

    class Meta:
        verbose_name = _('Transmission type')
        verbose_name_plural = _('Transmission types')


class VehicleCarcass(AbstractName):
    type_vehicles = models.ManyToManyField(VehicleKind, verbose_name=_('Using in vehicles'), blank=True, null=True)

    class Meta:
        verbose_name = _('Vehicle carcass type')
        verbose_name_plural = _('Vehicle carcass types')


class VehicleEngine(AbstractName):
    type_vehicles = models.ManyToManyField(VehicleKind, verbose_name=_('Using in vehicles'), blank=True, null=True)

    class Meta:
        verbose_name = _('Vehicle carcass type')
        verbose_name_plural = _('Vehicle carcass types')


class VehicleVendor(AbstractVendor):
    country = models.ForeignKey(Country, verbose_name=_('Country'), null=True, blank=True, on_delete=models.SET_NULL)


class Vehicle(AbstractName, AbstractDate, AbstractSeller):
    expiration_date = models.DateTimeField(_("Date of expiration"), null=True, blank=True)
    kind = models.ForeignKey(VehicleKind, verbose_name=_('Type of vehicle'))
    color = models.ForeignKey(VehicleColor, verbose_name=_('Vehicle color'))
    transmission = models.ForeignKey(VehicleTransmission, verbose_name=_('Type of transmission'))
    carcass = models.ForeignKey(VehicleCarcass, verbose_name=_('Carcass of vehicle'))
    engine = models.ForeignKey(VehicleEngine, verbose_name=_('Engine of vehicle'))
    vendor = models.ForeignKey(VehicleVendor, verbose_name=_('Vendor of vehicle'))
    mileage = models.IntegerField(verbose_name=_('Mileage'), max_length=10, null=True, blank=True)
    vin = models.CharField(verbose_name=_('VIN-code'), max_length=100, blank=True)
    horsepower = models.IntegerField(verbose_name=_('Horsepower'), max_length=10, null=True, blank=True)


    class Meta:
        verbose_name = _('Vehicle')
        verbose_name_plural = _('Vehicles')