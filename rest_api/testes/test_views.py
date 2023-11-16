import pytest
from rest_framework.test import APIClient
from model_bakery import barker
from reserva.models import ReservaDeBanho, Petshop
from rest_api.serializers import PetshopModelSerializer

