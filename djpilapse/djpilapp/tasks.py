from __future__ import absolute_import

from celery import shared_task

@shared_task
def add(x, y):
    return x + y

@shared_task
def timelapse_shoot():
    print 'shoot.'
    pass
