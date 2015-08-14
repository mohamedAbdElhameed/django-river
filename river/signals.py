from django.dispatch import Signal

__author__ = 'ahmetdal'

workflow_is_completed = Signal(providing_args=["workflow_object", "field"])
pre_transition = Signal(providing_args=["workflow_object", "field", "source_state", "destination_state", "approvement"])
post_transition = Signal(providing_args=["workflow_object", "field", "source_state", "destination_state", "approvement"])

pre_approved = Signal(providing_args=["workflow_object", "field"])
post_approved = Signal(providing_args=["workflow_object", "field", "approvement", "track"])
