import logging

from django.shortcuts import render
from django.utils.crypto import get_random_string

logger = logging.getLogger(__name__)


def get_referal_code():
    random = get_random_string(length=10)
    ref_code = 'TP-REF-' + str(random)
    return ref_code
