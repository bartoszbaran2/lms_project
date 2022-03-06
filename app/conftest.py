import pytest


@pytest.fixture(scope='function')
def user(db, django_user_model):
    """Default django user
    """
    user_ = django_user_model.objects.create_user(
        email='a@a.pl',
        fullname='ala',
        password='roman'
    )
    print('before')
    print('-' * 20)

    yield user_

    print('after')
    print('-' * 20) # nie przerywa funkcji, jak w returnie, czyli po skonczeniu np mozna posprzątać