# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Jogos(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    anoLancamento = models.PositiveSmallIntegerField() 
