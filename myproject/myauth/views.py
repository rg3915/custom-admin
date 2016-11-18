from registration.views import RegistrationView


class MyView(RegistrationView):

    def post(self, request):
        request.form['username'] = request.form.get('email')
        super().RegistrationView()
    # mudar o atributo do formulário
    # estender o form tb.
