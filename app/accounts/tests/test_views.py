from django.urls import reverse


def test_view_login(client): # test widoku
    url = reverse('accounts:login')
    response = client.get(url)

    assert response.status_code == 200
    assert 'Login' in response.content.decode('UTF-8')  # bo moze załadować inną strone, uwaga lepiej <h1>Login.. bo moze byc inny login na stronie