# -*- coding: utf-8 -*-
"""
    Blueprint Example Tests
    ~~~~~~~~~~~~~~

    Tests the Blueprint example app
"""
import pytest

import starfighter


@pytest.fixture
def client():
    return starfighter.app.test_client()


def test_urls(client):
    r = client.get('/')
    assert r.status_code == 200

    r = client.get('/hello')
    assert r.status_code == 200

    r = client.get('/world')
    assert r.status_code == 200
